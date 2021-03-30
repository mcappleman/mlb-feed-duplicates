import datetime
import pprint

from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser(description='Pass DB Connection URL and DB_NAME')
parser.add_argument('-n', '--db_name', help='The name of the database', required=True)
parser.add_argument('-u', '--db_url', help='full connection string url', required=True)
parser.add_argument('-y', '--year_start', help='The year to start looking for duplicates', default=2021)
parser.add_argument('-m', '--month_start', help='The month to start looking for duplicates', default=3)
parser.add_argument('-d', '--date_start', help='The day of the month to start looking for duplicates', default=21)

args = vars(parser.parse_args())

DB_NAME = args['db_name']
DB_URL = args['db_url']
start_date = datetime.datetime(args['year_start'], args['month_start'], args['date_start'])

print("Connecting to MongoClient")
# client = MongoClient(DB_HOST, DB_PORT)
client = MongoClient(DB_URL)
db = client[DB_NAME]
print("Authenticating to MongoClient")
# db.authenticate(DB_USER, DB_PASS)
print("Authenticated to MongoClient")

games_collection = db.games

found_gd2_ids = {}
duplicates = 0
for game in games_collection.find({"date": {"$gt": start_date}}).sort("date"):
    print(game["gd2_id"])
    gd2_id = game["gd2_id"]
    if found_gd2_ids.get(gd2_id) is None:
        found_gd2_ids[gd2_id] = gd2_id
        continue

    duplicates += 1
    print(gd2_id)
    print("Duplicates: " + str(duplicates))
    # games_collection.delete_one({"gd2_id": gd2_id})
