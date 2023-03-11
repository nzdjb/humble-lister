from json import loads


class Library:
    def __init__(self, library: str) -> None:
        self._library = self._parse_library_json(library)

    def _parse_library_json(self, json_input: str):
        purchases = [val for group in loads(json_input) for _, val in group.items()]
        library = [
            item
            for group in purchases
            for item in group.get("tpkd_dict", {}).get("all_tpks", [])
        ]
        return library
