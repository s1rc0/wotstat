from WotBlitz import WotBlitz
from pymongo import MongoClient
import math

START_ID = 1
END_ID = 100

wot = WotBlitz()
wot.application_id = '6c8058cb8dadba5f30be5439d9d15490'

client = MongoClient()
db = client.stat


def filling_gamer_ids(start_id, end_id, ids_per_request):
    if start_id > end_id:
        return print('End ID cant be more then Start ID')
    a = (end_id - start_id) / ids_per_request
    number_of_iter = math.ceil(a)
    for iteration in range(number_of_iter):
        if ids_per_request < (end_id - start_id):
            ids_list = str(list(range(start_id, start_id+ids_per_request)))[1:-1]
        else:
            ids_list = str(list(range(start_id, end_id)))[1:-1]
        stats = wot.get_player_personal_data(ids_list)  # JSON with Users from WG API
        for item in stats['data'].items():  # item = one user from WG API
            if item[1] is not None:  # item[1] = json data of one user
                if db.users.find({'account_id': item[1]['account_id']}).count() > 0:
                    print('FOUNDED, will REPLACE')
                else:
                    print('Cant search USER in Database, will ADD')
                    res = db.users.insert_one(item[1])
        start_id += ids_per_request
    return print("------------------------- Finished filling")

filling_gamer_ids(200, 220, 10)

