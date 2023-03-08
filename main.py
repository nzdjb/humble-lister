import json
import pprint

with open('library.json', encoding='UTF-8') as s:
    j = json.loads(s.read())

# for i in j:
#     for _, k in i.items():
#         print(k.keys())

library = [x for y in [v['tpkd_dict']['all_tpks'] for l in j for _, v in l.items()] for x in y ]


unclaimed = [x for x in library if x['key_type'] == 'steam' and not x.get('redeemed_key_val', False)]

# for bundle_id, bundle in library.items():
#     print(bundle_id)
#     print(bundle['product']['human_name'])
#     print([subproduct['human_name'] for subproduct in bundle['subproducts']])
    # print(bundle.keys())

# tpks = [product for i in library.values() for product in i]

for title in unclaimed:
    # print(title['human_name'], ':', title['steam_app_id'])
    redeemed = len([x for x in library if x.get('steam_app_id', False) == title.get('steam_app_id') and x.get('redeemed_key_val')])
    if title['steam_app_id'] is None or redeemed < 1:
        print(title['human_name'])
    # if not title['steam_app_id']:
    #     pprint.pp(title)

# pprint.pp(len(unclaimed))
