from pymongo import MongoClient

from mongo.config_variables import MONGO_CONFIG


"""Contains setup and configuration data for MongoDB instance."""

client = MongoClient(
    f"mongodb://{MONGO_CONFIG['username']}:{MONGO_CONFIG['password']}@ds155086.mlab.com:55086/leagueside-interview"
)

db = client["leagueside-interview"]

leagues_collection = db["test-collection"]
