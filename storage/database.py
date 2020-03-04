from typing import Dict
import pymongo


class Database:
    URI = "mongodb://127.0.0.1:27017/deals"
    DATABASE = pymongo.MongoClient(URI).get_default_database()

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def findall(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def findone(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].findone(query)