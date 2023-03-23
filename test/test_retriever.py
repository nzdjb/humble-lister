from string import ascii_lowercase
from unittest import TestCase
from unittest.mock import Mock, call
from humble_lister.retriever import Retriever
import requests


class TestRetriever(TestCase):
    def test_create(self) -> None:
        r = Retriever()
        self.assertIsInstance(r, Retriever)
        self.assertIsInstance(r._session, requests.Session)

    def test_create_with_mock(self) -> None:
        session = Mock()
        r = Retriever(session)
        self.assertIsInstance(r, Retriever)
        self.assertEqual(r._session, session)

    def test_get_order_ids(self) -> None:
        session = Mock()
        session.get.return_value.text = (
            '<script id="user-home-json-data" >{"gamekeys":["abc", "def"]}</script>'
        )
        r = Retriever(session)
        orders = r._get_order_ids()
        session.get.assert_called_once_with(
            "https://www.humblebundle.com/home/library",
        )
        self.assertEqual(orders, ["abc", "def"])

    def test_get_order_ids_error_on_data_missing(self) -> None:
        session = Mock()
        session.get.return_value.text = ""
        r = Retriever(session)
        with self.assertRaises(ValueError) as ve:
            r._get_order_ids()
        self.assertEqual(str(ve.exception), "Could not find user-home-json-data tag.")

    def test_group_list(self) -> None:
        session = Mock()
        r = Retriever(session)
        groups = r._group_list(list(range(10)), 3)
        self.assertEqual(groups, [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]])

    def test_group_list_default_size(self) -> None:
        session = Mock()
        r = Retriever(session)
        groups = r._group_list(list(range(1000)))
        self.assertEqual(len(groups), 25)
        self.assertEqual(len(groups[9]), 40)

    def test_get_data(self) -> None:
        session = Mock()
        session.get.side_effect = map(
            lambda x: Mock(text='{"' + x + '": 1}'), list(ascii_lowercase)
        )
        r = Retriever(session)
        r._get_order_ids = lambda: ["a"] * 405
        data = r.get_data()
        self.assertEqual(session.get.call_count, 11)
        calls = [
            call(
                "https://www.humblebundle.com/api/v1/orders?all_tpkds=true&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a"
            )
        ] + [
            call(
                "https://www.humblebundle.com/api/v1/orders?all_tpkds=true&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a&gamekeys=a"
            )
        ] * 10
        session.get.assert_has_calls(calls, any_order=True)
        self.assertEqual(
            data,
            {
                "a": 1,
                "b": 1,
                "c": 1,
                "d": 1,
                "e": 1,
                "f": 1,
                "g": 1,
                "h": 1,
                "i": 1,
                "j": 1,
                "k": 1,
            },
        )
