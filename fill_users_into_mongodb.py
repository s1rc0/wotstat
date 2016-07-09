from WotBlitz import WotBlitz
from pymongo import MongoClient
import math
import argparse

wot = WotBlitz()
wot.application_id = '6c8058cb8dadba5f30be5439d9d15490'

client = MongoClient()
db = client.stat

try:
    client.server_info()
except Exception as e:
    print("Could not connect to server: %s" % e)
    raise SystemExit


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
        stats = wot.get_player_personal_data(ids_list)
        for item in stats['data'].items():
            if item[1] is not None:
                if db.users.find({'account_id': item[1]['account_id']}).count() > 0:
                    print('User with account ID:', item[1]['account_id'], ' already present in database',
                          ' will replace')
                    pass  # need replace existing user account
                else:
                    pass
                    db.users.insert_one(item[1])  # adding user account into users collection
                    print('Adding new user account with account ID: ', item[1]['account_id'])
        start_id += ids_per_request
    return print("Finished filling")

parser = argparse.ArgumentParser(description='Worker for filling users collection.')
parser.add_argument('-s', '--start_id', required=True, type=int)
parser.add_argument('-e', '--end_id', required=True, type=int)
parser.add_argument('-id', '--ids', required=True, type=int)
args = parser.parse_args()
filling_gamer_ids(args.start_id, args.end_id, args.ids)
