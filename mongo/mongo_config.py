"""Contains setup and configuration data for MongoDB instance."""
from pymongo import MongoClient, GEOSPHERE
import os

CLIENT = MongoClient(
    "mongodb://{0}:{1}@{2}/leagueside-interview".format(
        os.environ.get("MONGO_USERNAME"),
        os.environ.get("MONGO_PASSWORD"),
        os.environ.get("MONGO_HOST"),
    )
)

DB = CLIENT["leagueside-interview"]

LEAGUES_COLLECTION = DB["test-collection"]

# Indexing coordinates as a GEOSPHERE instance allows querying by radial distance from central point
LEAGUES_COLLECTION.create_index([("coordinates", GEOSPHERE)])
