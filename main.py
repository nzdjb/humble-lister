from humble_lister.library import Library
from humble_lister.retriever import Retriever
from requests import Session

with open("humble.cookie", encoding="utf-8") as c:
    sess = Session()
    sess.cookies.set("_simpleauth_sess", str(c.read().strip()))

retriever = Retriever(sess)
data = retriever.get_data()
library = Library(data)

unclaimed = library.unclaimed.steam

for title in unclaimed:
    redeemed = len(
        [
            x
            for x in library
            if x.get("steam_app_id", False) == title.get("steam_app_id")
            and x.get("redeemed_key_val")
        ]
    )
    if title["steam_app_id"] is None or redeemed < 1:
        print(title["human_name"])
