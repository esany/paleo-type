import unittest
from edition_build import build_site

class EditionBuildTests(unittest.TestCase):
    def test_builder_exists(self):
        self.assertTrue(callable(build_site))
