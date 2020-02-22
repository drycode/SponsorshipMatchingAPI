"""Contains setup and configuration data for MongoDB instance."""

from pymongo import MongoClient, GEOSPHERE
from pymongo.errors import OperationFailure
import os
from mongo.initial_data import MONGO_DOCS

CLIENT = MongoClient(host=os.environ.get("MONGO_HOST"))

DB = CLIENT["leagueside-interview"]

LEAGUES_COLLECTION = DB["test-collection"]

# Initializes data for testing
try:
    if not LEAGUES_COLLECTION.find_one():
        for doc in MONGO_DOCS:
            LEAGUES_COLLECTION.insert(doc)

    # Indexing coordinates as a GEOSPHERE instance allows querying by radial distance from central point
    LEAGUES_COLLECTION.create_index([("coordinates", GEOSPHERE)])

except OperationFailure as err:
    pass

