from WotBlitz import WotBlitz
from pymongo import MongoClient
import pymongo
import math
import argparse

wot = WotBlitz()
wot.application_id = '6c8058cb8dadba5f30be5439d9d15490'

client = MongoClient()
db = client.stat

# total = db.users.find().count()
# latest_account_list = db.users.find({'losses': 100000}).limit(5)

#for acc in db.users.find({"statistics.all.xp": 5}).sort([
#        ('account_id', pymongo.ASCENDING)]).limit(100):
#    print(acc['account_id'])

for acc in db.users.find().sort().limit(100):
    print(acc['wins'])

# filling_gamer_ids(1, 1000, 100)