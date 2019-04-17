import datetime
import pprint

from pymongo import MongoClient

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
    print("Duplicates: " + str(duplicates))


# for key, value in found_gd2_ids.items():
#    game = games_collection.find_one({"gd2_id": key})
#    games_collection.delete_one({"_id": game["_id"]})