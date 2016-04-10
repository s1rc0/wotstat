from WotBlitz import WotBlitz
from pymongo import MongoClient
import math
import argparse

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
        stats = wot.get_player_personal_data(ids_list)
        for item in stats['data'].items():
            if item[1] is not None:
                if db.users.find({'account_id': item[1]['account_id']}).count() > 0:
                    pass  # need replace existing user account
                else:
                    db.users.insert_one(item[1])  # adding user account into users collection
        start_id += ids_per_request
    return print("Finished filling")

# filling_gamer_ids(1, 1000, 100)
parser = argparse.ArgumentParser(description='Worker for filling users collection.')
parser.add_argument('integers', metavar='start_id', type=int, nargs='+',
                    help='integer, start id for parse WOT Blitz API')
parser.add_argument('integers', metavar='end_id', type=int, nargs='+',
                    help='integer, end id for parse WOT Blitz API')
parser.add_argument('integers', metavar='ids_per_request', type=int, nargs='+',
                    help='integer, number of getting IDs per request')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
