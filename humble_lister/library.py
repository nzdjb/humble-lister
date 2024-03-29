from json import loads
from typing import Any


class Library:
    def __init__(self, library: str | list | dict) -> None:
        if isinstance(library, str):
            library = loads(library)
            self._library = self._parse_library(library)
        elif isinstance(library, dict):
            self._library = self._parse_library([library])
        else:
            self._library = library

    def _parse_library(self, input_list: list):
        purchases = [val for group in input_list for _, val in group.items()]
        library = [
            item
            for group in purchases
            for item in group.get("tpkd_dict", {}).get("all_tpks", [])
        ]
        return library

    def __getattr__(self, __name: str) -> Any:
        match __name:
            case "unclaimed":
                return Library(self._get_unclaimed())
            case "steam":
                return Library(self._get_steam())
            case _:
                return super(type(self), self).__getattribute__(__name)

    def _get_unclaimed(self):
        return [
            item for item in self._library if not item.get("redeemed_key_val", False)
        ]

    def _get_steam(self):
        return [item for item in self._library if item.get("key_type") == "steam"]

    def __iter__(self):
        return self._library.__iter__()

    def __len__(self):
        return self._library.__len__()
