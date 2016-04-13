from WotBlitz import WotBlitz
from pymongo import MongoClient
import math
import argparse

wot = WotBlitz()
wot.application_id = '6c8058cb8dadba5f30be5439d9d15490'

client = MongoClient()
db = client.stat

total = db.users.find().count()
latest_account_list = db.users.find().limit(1)


for li in latest_account_list:
    #print(li['created_at'])
    print(li['statistics']['all'])


# filling_gamer_ids(1, 1000, 100)