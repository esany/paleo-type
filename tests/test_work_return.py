"""S1 regressions from #346/#347, run 605e6a5d and #359's live T1/T2 owner.

Fixtures are deliberately scratch repositories: no manuscript reading is judged.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parents[1] / "tools" / "work_return.py"
PROJECT = "ssta-20578-nr-632"
OWNER_LINE = (
    "**Authorized current action: Issue #358 / iterative T1 + source-bounded T2** "
    "— continue T1 and the already begun locally sufficient T2 pilots concurrently; "
    "do not reimpose whole-unit T1 completion as a gate before local S3."
)


class WorkReturnS1Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.project = self.root / "projects" / PROJECT
        (self.project / "research").mkdir(parents=True)
        (self.project / "project.yml").write_text(
            "project_id: ssta-20578-nr-632\ncanonical_status_file: STATUS.md\n",
            encoding="utf-8",
        )
        self.set_status(OWNER_LINE)

    def set_status(self, content: str) -> None:
        (self.project / "STATUS.md").write_text(content + "\n", encoding="utf-8")
        self.status_sha = hashlib.sha256((content + "\n").encode()).hexdigest()

    def run_report(self, **overrides: object) -> tuple[int, dict]:
        report = {
            "run_id": "605e6a5d-4d78-8325-8cc9-3f2295efaad6",
            "run_status": "completed",
            "recorded_status_sha256": self.status_sha,
            "baseline_commit": None,
            "result_commit": None,
            "research_owner": None,
            "local_pass": False,
            "continuation_anchor": "",
            "stop_reason": "",
            "stop_evidence": "",
        }
        report.update(overrides)
        path = self.root / "report.json"
        path.write_text(json.dumps(report), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(TOOL), "--root", str(self.root),
             "--project", PROJECT, "--report", str(path)],
            capture_output=True, text=True, check=False,
        )
        self.assertTrue(proc.stdout.strip(), proc.stderr)
        return proc.returncode, json.loads(proc.stdout)

    def git(self, *args: str) -> str:
        return subprocess.check_output(
            ["git", *args], cwd=self.root, text=True, stderr=subprocess.DEVNULL
        ).strip()

    def test_completed_605e_without_research_commit_is_not_success(self) -> None:
        # #346: host said 'completed'; no image access, research owner change or commit.
        rc, out = self.run_report()
        self.assertNotEqual(0, rc)
        self.assertFalse(out["owner_change"])
        self.assertIn("keine Änderung im Forschungs-Owner", " ".join(out["findings"]))
        self.assertNotIn("Erfolg", out["result"])

    def test_stored_global_t1_gate_yields_to_current_project_owner(self) -> None:
        # #346/#359: stale 'T2 erst nach vollständigem T1' vs live parallel T1/T2.
        old_status_hash = hashlib.sha256(
            b"T2 erst nach vollstaendigem T1\n"
        ).hexdigest()
        rc, out = self.run_report(
            run_status="not-run", recorded_status_sha256=old_status_hash,
            continuation_anchor=OWNER_LINE,
        )
        self.assertNotEqual(0, rc)
        self.assertIn("Project-Owner geaendert", " ".join(out["findings"]))
        self.assertIn("Halt", out["result"])

    def test_local_pass_without_evidenced_continuation_or_stop_is_invalid(self) -> None:
        # Original #346: three small slices completed; no checked continuation/STOP.
        rc, out = self.run_report(run_status="not-run", local_pass=True)
        self.assertNotEqual(0, rc)
        self.assertIn("Fortsetzung nicht belegt", " ".join(out["findings"]))

    def test_actual_research_owner_diff_and_live_continuation_can_pass(self) -> None:
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "CI Fixture")
        research = self.project / "research" / "source-notes.md"
        research.write_text("before\n", encoding="utf-8")
        self.git("add", "projects")
        self.git("commit", "-qm", "baseline")
        baseline = self.git("rev-parse", "HEAD")
        baseline_hash = self.status_sha
        research.write_text("before\nnew source observation, with evidence locator\n", encoding="utf-8")
        new_anchor = "**Next review: source notes have been updated in this block.**"
        self.set_status(OWNER_LINE + "\n" + new_anchor)
        self.git("add", "projects")
        self.git("commit", "-qm", "research delta and STATUS return")
        result = self.git("rev-parse", "HEAD")
        rc, out = self.run_report(
            baseline_commit=baseline,
            result_commit=result,
            recorded_status_sha256=baseline_hash,
            research_owner=f"projects/{PROJECT}/research/source-notes.md",
            local_pass=True,
            continuation_anchor=new_anchor,
        )
        self.assertEqual(0, rc, out)
        self.assertTrue(out["owner_change"])
        self.assertIn("Änderung im Forschungs-Owner gespeichert; Lesegewinn nicht geprüft", out["result"])


    def init_baseline(self) -> tuple[str, Path]:
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "CI Fixture")
        research = self.project / "research" / "source-notes.md"
        research.write_text("before\n", encoding="utf-8")
        self.git("add", "projects")
        self.git("commit", "-qm", "baseline")
        return self.git("rev-parse", "HEAD"), research

    def test_same_block_status_and_research_change_passes_with_baseline_hash(self) -> None:
        baseline, research = self.init_baseline()
        baseline_hash = self.status_sha
        research.write_text("before\nnew source note\n", encoding="utf-8")
        updated_line = "**Authorized current action: continue the visible document text."
        self.set_status(updated_line)
        self.git("add", "projects")
        self.git("commit", "-qm", "research and status in same block")
        result = self.git("rev-parse", "HEAD")
        rc, out = self.run_report(
            baseline_commit=baseline, result_commit=result,
            recorded_status_sha256=baseline_hash,
            research_owner=f"projects/{PROJECT}/research/source-notes.md",
            continuation_anchor=updated_line,
        )
        self.assertEqual(0, rc, out)
        self.assertTrue(out["owner_change"])

    def test_status_hash_older_than_baseline_is_rejected(self) -> None:
        baseline, research = self.init_baseline()
        stale_hash = hashlib.sha256(b"obsolete status\n").hexdigest()
        research.write_text("before\nnew source note\n", encoding="utf-8")
        self.git("add", "projects")
        self.git("commit", "-qm", "research")
        rc, out = self.run_report(
            baseline_commit=baseline, result_commit=self.git("rev-parse", "HEAD"),
            recorded_status_sha256=stale_hash,
            research_owner=f"projects/{PROJECT}/research/source-notes.md",
            continuation_anchor=OWNER_LINE,
        )
        self.assertNotEqual(0, rc)
        self.assertIn("Project-Owner geaendert", " ".join(out["findings"]))

    def test_one_character_continuation_anchor_is_rejected(self) -> None:
        rc, out = self.run_report(run_status="not-run", continuation_anchor="A")
        self.assertNotEqual(0, rc)
        self.assertIn("Fortsetzung nicht belegt", " ".join(out["findings"]))

    def test_later_worktree_edit_does_not_invalidate_committed_owner_change(self) -> None:
        baseline, research = self.init_baseline()
        baseline_hash = self.status_sha
        research.write_text("before\nnew source note\n", encoding="utf-8")
        new_anchor = "**Return: committed research file is ready to review.**"
        self.set_status(OWNER_LINE + "\n" + new_anchor)
        self.git("add", "projects")
        self.git("commit", "-qm", "first result")
        result = self.git("rev-parse", "HEAD")
        research.write_text("before\nnew source note\nfurther local work\n", encoding="utf-8")
        rc, out = self.run_report(
            baseline_commit=baseline, result_commit=result,
            recorded_status_sha256=baseline_hash,
            research_owner=f"projects/{PROJECT}/research/source-notes.md",
            continuation_anchor=new_anchor,
        )
        self.assertEqual(0, rc, out)
        self.assertTrue(out["owner_change"])

    def test_justified_access_stop_reports_no_delta_without_claiming_success(self) -> None:
        rc, out = self.run_report(
            local_pass=True, stop_reason="original images unavailable in this run",
            stop_evidence="worker access log for the exact registered File",
        )
        self.assertEqual(0, rc, out)
        self.assertFalse(out["owner_change"])
        self.assertIn("keine Änderung im Forschungs-Owner", " ".join(out["findings"]))
        self.assertIn("Halt", out["result"])


    def test_existing_separator_cannot_be_a_new_continuation(self) -> None:
        self.set_status(OWNER_LINE + "\n---")
        baseline, research = self.init_baseline()
        baseline_hash = self.status_sha
        research.write_text("before\nchanged research owner\n", encoding="utf-8")
        self.git("add", "projects")
        self.git("commit", "-qm", "result without new status anchor")
        rc, out = self.run_report(
            baseline_commit=baseline, result_commit=self.git("rev-parse", "HEAD"),
            recorded_status_sha256=baseline_hash,
            research_owner=f"projects/{PROJECT}/research/source-notes.md",
            continuation_anchor="---",
        )
        self.assertNotEqual(0, rc, out)
        self.assertIn("Fortsetzung nicht belegt", " ".join(out["findings"]))

    def test_existing_heading_cannot_be_a_new_continuation(self) -> None:
        self.set_status(OWNER_LINE + "\n## Old next action")
        baseline, research = self.init_baseline()
        baseline_hash = self.status_sha
        research.write_text("before\nchanged research owner\n", encoding="utf-8")
        self.git("add", "projects")
        self.git("commit", "-qm", "result without newly written heading")
        rc, out = self.run_report(
            baseline_commit=baseline, result_commit=self.git("rev-parse", "HEAD"),
            recorded_status_sha256=baseline_hash,
            research_owner=f"projects/{PROJECT}/research/source-notes.md",
            continuation_anchor="## Old next action",
        )
        self.assertNotEqual(0, rc, out)
        self.assertIn("Fortsetzung nicht belegt", " ".join(out["findings"]))

    def test_new_status_line_is_a_real_continuation(self) -> None:
        baseline, research = self.init_baseline()
        baseline_hash = self.status_sha
        research.write_text("before\nchanged research owner\n", encoding="utf-8")
        new_line = "**Next review: 0104R awaits independent reading.**"
        self.set_status(OWNER_LINE + "\n" + new_line)
        self.git("add", "projects")
        self.git("commit", "-qm", "result with fresh status line")
        rc, out = self.run_report(
            baseline_commit=baseline, result_commit=self.git("rev-parse", "HEAD"),
            recorded_status_sha256=baseline_hash,
            research_owner=f"projects/{PROJECT}/research/source-notes.md",
            continuation_anchor=new_line,
        )
        self.assertEqual(0, rc, out)
        self.assertTrue(out["owner_change"])


if __name__ == "__main__":
    unittest.main()
