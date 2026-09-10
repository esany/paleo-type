#!/usr/bin/env python3
"""Explicit same-source visual-candidate retrieval for Reg. Ii 5 (#141).

This bounded research-support helper receives an already-rendered exact Reg. Ii 5
page pool and a target rectangle. It returns only ranked image locations and
technical similarity scores. It does not load diplomatic readings, infer words,
claim same hand, adjudicate comparanda, or promote a reading.

The first experiment is intentionally limited to Source
THHSTAW-EGA-REG-II-5-STAT-VIS-00000129, fol. 55v-66v. Pool availability does
not activate retrieval: callers must pass --activate-same-source-pool.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

SOURCE_ID = "THHSTAW-EGA-REG-II-5-STAT-VIS-00000129"
FILE_ID = "FILE-REG-II-5-00000129-EXCERPT"
CROSSWALK_REL = Path("corpus/source-data") / SOURCE_ID / "crosswalk.tsv"
FILES_REL = Path("corpus/files.tsv")
METHOD_ID = "opencv.matchTemplate/TM_CCOEFF_NORMED/raw-grayscale/v1"


class RetrievalError(RuntimeError):
    """The bounded retrieval cannot be run under the requested conditions."""


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise RetrievalError(f"missing canonical metadata file {path}")
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_file_row(root: Path) -> dict[str, str]:
    rows = [row for row in read_tsv(root / FILES_REL) if row.get("file_id") == FILE_ID]
    if len(rows) != 1:
        raise RetrievalError(f"expected one canonical File row for {FILE_ID}, found {len(rows)}")
    row = rows[0]
    if row.get("source_id") != SOURCE_ID:
        raise RetrievalError(f"canonical File {FILE_ID} is not bound to {SOURCE_ID}")
    return row


def authorized_pool(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in read_tsv(root / CROSSWALK_REL):
        if row.get("source_id") != SOURCE_ID:
            continue
        try:
            pdf_page = int(row.get("pdf_page", ""))
        except ValueError as exc:
            raise RetrievalError(
                f"invalid pdf_page in {CROSSWALK_REL}: {row.get('pdf_page')!r}"
            ) from exc
        # The canonical Source coverage is fol. 55v-66v / PDF pp. 2-24.
        # PDF p. 25 / fol. 67r is adjacent File context and is not admitted.
        if 2 <= pdf_page <= 24:
            rows.append(
                {
                    "source_id": SOURCE_ID,
                    "folio": row.get("archival_folio", ""),
                    "pdf_page": pdf_page,
                    "mapping_status": row.get("mapping_status", ""),
                }
            )
    rows.sort(key=lambda row: row["pdf_page"])
    expected = list(range(2, 25))
    got = [row["pdf_page"] for row in rows]
    if got != expected:
        raise RetrievalError(
            f"authorized same-source pool must resolve PDF pages 2-24 exactly; got {got}"
        )
    return rows


def parse_box(text: str) -> tuple[int, int, int, int]:
    try:
        values = tuple(int(value) for value in text.split(","))
    except ValueError as exc:
        raise RetrievalError("target box must be x,y,w,h integers") from exc
    if (
        len(values) != 4
        or values[0] < 0
        or values[1] < 0
        or values[2] <= 0
        or values[3] <= 0
    ):
        raise RetrievalError("target box must be non-negative x,y and positive w,h")
    return values  # type: ignore[return-value]


def iou(
    first: tuple[int, int, int, int], second: tuple[int, int, int, int]
) -> float:
    ax, ay, aw, ah = first
    bx, by, bw, bh = second
    x0 = max(ax, bx)
    y0 = max(ay, by)
    x1 = min(ax + aw, bx + bw)
    y1 = min(ay + ah, by + bh)
    intersection = max(0, x1 - x0) * max(0, y1 - y0)
    union = aw * ah + bw * bh - intersection
    return intersection / union if union else 0.0


def candidate_record(
    rank: int,
    pool_row: dict[str, Any],
    box: tuple[int, int, int, int],
    score: float,
    render_sha256: str,
) -> dict[str, Any]:
    x, y, width, height = box
    return {
        "rank": rank,
        "source_id": SOURCE_ID,
        "file_id": FILE_ID,
        "pool": "same-source",
        "folio": pool_row["folio"],
        "pdf_page": pool_row["pdf_page"],
        "crop_box": {"x": x, "y": y, "w": width, "h": height},
        "render_sha256": render_sha256,
        "similarity_score": round(float(score), 6),
        "score_role": "technical ranking only",
        "scholarly_inspected": False,
        "comparator_accepted": False,
        "reading_promoted": False,
    }


def describe_contract() -> dict[str, Any]:
    return {
        "view": "DERIVED_REGII5_VISUAL_RETRIEVAL_CONTRACT",
        "canonical": False,
        "generator": "same-source visual template retrieval",
        "pool_available": True,
        "pool_activated": False,
        "authorized_source_id": SOURCE_ID,
        "authorized_folia": "55v-66v",
        "candidate_text_generated": False,
        "reading_owner_loaded": False,
        "same_hand_inferred": False,
        "reading_promotion_possible": False,
        "method": METHOD_ID,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    if not args.activate_same_source_pool:
        raise RetrievalError(
            "same-source pool is available but not activated; "
            "pass --activate-same-source-pool explicitly"
        )

    try:
        import cv2  # type: ignore
        import numpy as np  # type: ignore
    except ImportError as exc:
        raise RetrievalError("OpenCV + NumPy are required for the local #141 spike") from exc

    root = Path(args.root).resolve()
    source_file = Path(args.source_file).resolve()
    pages_dir = Path(args.pages_dir).resolve()

    file_row = canonical_file_row(root)
    expected_sha = file_row.get("sha256", "")
    actual_sha = sha256_file(source_file)
    if actual_sha != expected_sha:
        raise RetrievalError(
            f"source-file SHA mismatch: canonical {expected_sha}, local {actual_sha}"
        )

    pool = authorized_pool(root)
    by_page = {row["pdf_page"]: row for row in pool}
    target_page = args.target_page
    if target_page not in by_page:
        raise RetrievalError(
            f"target PDF page {target_page} is outside authorized same-source pool"
        )
    target_box = parse_box(args.target_box)

    page_paths: dict[int, Path] = {}
    for row in pool:
        path = pages_dir / f"page-{row['pdf_page']}.png"
        if not path.is_file():
            raise RetrievalError(f"missing authorized render {path}")
        page_paths[row["pdf_page"]] = path

    target_image = cv2.imread(str(page_paths[target_page]), cv2.IMREAD_GRAYSCALE)
    if target_image is None:
        raise RetrievalError(f"cannot decode target render {page_paths[target_page]}")

    x, y, width, height = target_box
    if x + width > target_image.shape[1] or y + height > target_image.shape[0]:
        raise RetrievalError("target box exceeds target render bounds")
    query = target_image[y : y + height, x : x + width]
    query_sha = hashlib.sha256(query.tobytes()).hexdigest()

    raw: list[dict[str, Any]] = []
    started = time.perf_counter()
    for page, row in by_page.items():
        image = cv2.imread(str(page_paths[page]), cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise RetrievalError(f"cannot decode render {page_paths[page]}")
        if query.shape[0] > image.shape[0] or query.shape[1] > image.shape[1]:
            raise RetrievalError(f"query larger than render page {page}")

        scores = cv2.matchTemplate(image, query, cv2.TM_CCOEFF_NORMED)
        flat = scores.ravel()
        peak_count = min(args.raw_peaks_per_page, flat.size)
        indexes = np.argpartition(flat, -peak_count)[-peak_count:]
        indexes = indexes[np.argsort(flat[indexes])[::-1]]

        page_kept: list[dict[str, Any]] = []
        render_sha = sha256_file(page_paths[page])
        for index in indexes:
            py, px = np.unravel_index(index, scores.shape)
            box = (int(px), int(py), width, height)
            if page == target_page and iou(box, target_box) > args.target_exclusion_iou:
                continue
            if any(iou(box, kept["box"]) > args.nms_iou for kept in page_kept):
                continue
            page_kept.append(
                {
                    "page": page,
                    "row": row,
                    "box": box,
                    "score": float(scores[py, px]),
                    "render_sha": render_sha,
                }
            )
            if len(page_kept) >= args.per_page_limit:
                break
        raw.extend(page_kept)

    runtime = time.perf_counter() - started
    raw.sort(key=lambda item: item["score"], reverse=True)

    selected: list[dict[str, Any]] = []
    for item in raw:
        if any(
            item["page"] == kept["page"]
            and iou(item["box"], kept["box"]) > args.nms_iou
            for kept in selected
        ):
            continue
        selected.append(item)
        if len(selected) >= args.top_k:
            break

    candidates = [
        candidate_record(
            rank + 1,
            item["row"],
            item["box"],
            item["score"],
            item["render_sha"],
        )
        for rank, item in enumerate(selected)
    ]

    return {
        "status": "OK",
        "view": "DERIVED_REGII5_VISUAL_RETRIEVAL",
        "canonical": False,
        "candidate_selection_state": {
            "pool_available": True,
            "pool_activated": True,
            "crop_returned": len(candidates),
            "crop_scholarly_inspected": 0,
            "comparator_accepted": 0,
            "reading_promoted": 0,
        },
        "authority_boundary": {
            "candidate_text_generated": False,
            "reading_owner_loaded": False,
            "same_hand_inferred": False,
            "similarity_is_reading_evidence": False,
            "target_return_required_for_reading_consequence": True,
        },
        "provenance": {
            "source_id": SOURCE_ID,
            "file_id": FILE_ID,
            "source_file_sha256": actual_sha,
            "source_file_sha_matches_canonical": True,
            "render_dpi": args.render_dpi,
            "renderer": args.renderer,
            "renderer_version": args.renderer_version,
            "feature_method": METHOD_ID,
            "opencv_version": cv2.__version__,
            "opencv_package_license": (
                "Apache-2.0; exact installed package metadata belongs in the evaluation record"
            ),
        },
        "query": {
            "folio": by_page[target_page]["folio"],
            "pdf_page": target_page,
            "crop_box": {"x": x, "y": y, "w": width, "h": height},
            "query_pixel_sha256": query_sha,
        },
        "pool": {
            "folio_range": "55v-66v",
            "pdf_pages": [row["pdf_page"] for row in pool],
            "external_witnesses_activated": False,
        },
        "retrieval": {
            "top_k": args.top_k,
            "runtime_seconds": round(runtime, 6),
            "candidates": candidates,
        },
        "human_review_required": (
            "Inspect returned crops directly; rank/score alone cannot accept a comparator "
            "or change a reading."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explicit same-source visual candidate retrieval for Reg. Ii 5."
    )
    parser.add_argument("--describe-contract", action="store_true")
    parser.add_argument("--activate-same-source-pool", action="store_true")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--source-file")
    parser.add_argument("--pages-dir")
    parser.add_argument("--target-page", type=int)
    parser.add_argument("--target-box", help="x,y,w,h in rendered-page pixels")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--render-dpi", type=int, default=180)
    parser.add_argument("--renderer", default="pdfium via render_pdf.py")
    parser.add_argument("--renderer-version", default="UNSPECIFIED")
    parser.add_argument("--raw-peaks-per-page", type=int, default=250)
    parser.add_argument("--per-page-limit", type=int, default=20)
    parser.add_argument("--nms-iou", type=float, default=0.25)
    parser.add_argument("--target-exclusion-iou", type=float, default=0.25)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.describe_contract:
        print(json.dumps(describe_contract(), ensure_ascii=False, indent=2))
        return 0

    required = ("source_file", "pages_dir", "target_page", "target_box")
    missing = [name for name in required if getattr(args, name) in (None, "")]
    if missing:
        print(
            json.dumps(
                {"status": "ERROR", "error": "missing required retrieval args: " + ", ".join(missing)},
                ensure_ascii=False,
                indent=2,
            ),
            file=sys.stderr,
        )
        return 2

    try:
        result = run(args)
    except RetrievalError as exc:
        print(
            json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False, indent=2),
            file=sys.stderr,
        )
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
