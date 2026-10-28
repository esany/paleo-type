"""Static repository routing guard; NOT evidence of host skill registration."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SavesaxRoutingContractTests(unittest.TestCase):
    def test_agents_forwards_archive_acquisition_to_canonical_dresden_skill(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(".agents/skills/savesax/SKILL.md", agents)
        self.assertIn("Hauptstaatsarchiv Dresden", agents)
        self.assertIn("Human need not name the skill", agents)
        self.assertIn("status-read", agents)

    def test_discovery_has_natural_german_intent_and_known_fullsize_rule(self):
        skill = (ROOT / ".agents/skills/savesax/SKILL.md").read_text(encoding="utf-8")
        meta = (ROOT / ".agents/skills/savesax/agents/openai.yaml").read_text(
            encoding="utf-8"
        )
        frontmatter = skill.split("---", 2)[1]
        for token in ("name: savesax", "Sichere", "herunterladen",
                      "Hauptstaatsarchivs Dresden", "www.archiv.sachsen.de"):
            self.assertIn(token, frontmatter)
        self.assertIn("allow_implicit_invocation: true", meta)
        self.assertIn(".digitalisat-viewer-thumbnail.loaded.active", skill)
        self.assertIn("/fullsize/../preview/", skill)
        self.assertIn("/fullsize/0001.jpg", skill)

    def test_status_only_does_not_authorize_acquisition(self):
        skill = (ROOT / ".agents/skills/savesax/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("read-only", skill)
        self.assertIn("never infer a rerun", skill)


if __name__ == "__main__":
    unittest.main()
