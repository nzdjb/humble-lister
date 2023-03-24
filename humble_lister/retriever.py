from requests import Session
from bs4 import BeautifulSoup
from json import loads


class Retriever:
    BASE_URL = "https://www.humblebundle.com/"
    GROUP_SIZE = 40

    def __init__(self, session: Session = None):
        if not session:
            session = Session()
        self._session = session

    def _get_order_ids(self) -> list:
        response = self._session.get(self.BASE_URL + "home/library")
        soup = BeautifulSoup(response.text, "html.parser").find(
            "script", {"id": "user-home-json-data"}
        )
        if not soup:
            raise ValueError("Could not find user-home-json-data tag.")
        return loads(soup.text).get("gamekeys")

    def _group_list(self, l: list, n: int = None) -> list:
        if not n:
            n = self.GROUP_SIZE
        return [l[i : i + n] for i in range(0, len(l), n)]

    def get_data(self) -> dict:
        ids = self._get_order_ids()
        data = {}
        for group in self._group_list(ids):
            request = "&gamekeys=".join(
                [self.BASE_URL + "api/v1/orders?all_tpkds=true", *group]
            )
            text = self._session.get(request).text
            data |= loads(text)
        return data
