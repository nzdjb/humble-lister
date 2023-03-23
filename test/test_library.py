from unittest import TestCase
from humble_lister.library import Library


class TestLibrary(TestCase):
    def test_create_empty_with_list(self) -> None:
        library = Library([])
        self.assertEqual(library._library, [])

    def test_create_with_list_of_one(self) -> None:
        library = Library(["one"])
        self.assertEqual(library._library, ["one"])

    def test_create_with_dict_of_one(self) -> None:
        library = Library({"one": {"tpkd_dict": {"all_tpks": ["two"]}}})
        self.assertEqual(library._library, ["two"])

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

    def test_get_unclaimed(self) -> None:
        with open("test/files/sample.json") as s:
            library = Library(s.read())
        unclaimed = library._get_unclaimed()
        self.assertIsInstance(unclaimed, list)
        self.assertEqual(len(unclaimed), 6)

    def test_unclaimed(self) -> None:
        with open("test/files/sample.json") as s:
            library = Library(s.read())
        unclaimed = library.unclaimed
        self.assertIsInstance(unclaimed, Library)
        self.assertEqual(len(unclaimed._library), 6)

    def test_get_steam(self) -> None:
        with open("test/files/sample.json") as s:
            library = Library(s.read())
        steam = library._get_steam()
        self.assertIsInstance(steam, list)
        self.assertEqual(len(steam), 6)

    def test_steam(self) -> None:
        with open("test/files/sample.json") as s:
            library = Library(s.read())
        steam = library.steam
        self.assertIsInstance(steam, Library)
        self.assertEqual(len(steam._library), 6)

    def test_missing_attribute(self) -> None:
        library = Library([])
        with self.assertRaises(AttributeError):
            library.bob

    def test_len(self) -> None:
        library = Library(["a", "b", "c"])
        self.assertEqual(len(library), 3)

    def test_iter(self) -> None:
        library = Library(["a", "b", "c"])
        it = iter(library)
        self.assertEqual(next(it), "a")
        self.assertEqual(next(it), "b")
        self.assertEqual(next(it), "c")
        with self.assertRaises(StopIteration):
            next(it)
