import datetime
import pprint

from pymongo import MongoClient

DB_NAME = "drinen-mlb-feed"
DB_HOST = "ds031203.mlab.com"
DB_PORT = 31203
DB_USER = "raspberrypi"
DB_PASS = "Test1234"

client = MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

games_collection = db.games

found_gd2_ids = {}
duplicates = 0
start_date = datetime.datetime(2019, 3, 16)
for game in games_collection.find({"date": {"$gt": start_date}}).sort("date"):
    gd2_id = game["gd2_id"]
    if found_gd2_ids.get(gd2_id) is None:
        found_gd2_ids[gd2_id] = gd2_id
        continue

    duplicates += 1
    print(gd2_id)
    print("Duplicates: " + str(duplicates))
    # games_collection.delete_one({"gd2_id": gd2_id})


#for key, value in found_gd2_ids.items():
#   game = games_collection.find_one({"gd2_id": key})
#   games_collection.delete_one({"_id": game["_id"]})