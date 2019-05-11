"""Contains setup and configuration data for MongoDB instance."""
from pymongo import MongoClient

from mongo.config_variables import MONGO_CONFIG


CLIENT = MongoClient(
    "mongodb://{0}:{1}@ds155086.mlab.com:55086/leagueside-interview".format(
        MONGO_CONFIG["username"], MONGO_CONFIG["password"]
    )
)

DB = CLIENT["leagueside-interview"]

LEAGUES_COLLECTION = DB["test-collection"]
