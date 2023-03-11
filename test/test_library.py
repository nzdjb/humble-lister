from unittest import TestCase
from humble_lister.library import Library


class TestLibrary(TestCase):
    def test_parse_empty(self) -> None:
        library = Library("[]")
        self.assertEqual(library._library, [])

    def test_parse_single(self) -> None:
        library = Library('[{"abc":{"tpkd_dict":{"all_tpks":[{"Name": "Test"}]}}}]')
        self.assertEqual(library._library, [{"Name": "Test"}])

    def test_parse_sample(self) -> None:
        with open("test/files/sample.json") as s:
            library = Library(s.read())
        self.assertEqual(len(library._library), 8)
