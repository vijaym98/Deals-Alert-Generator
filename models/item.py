import requests
from bs4 import BeautifulSoup
import uuid
from storage.database import Database
from typing import Dict,List

class Item:
    def __init__(self, url, tag, query):
        self.url = url
        self.tag = tag
        self.query = query
        self.collection = "items"
        self.itemid = uuid.uuid4().hex

    def price_of_item(self) -> float:
        rq = requests.get(self.url)
        page_details = rq.content
        soup = BeautifulSoup(page_details, "html.parser")
        element = soup.find(self.tag, self.query)
        currency_price = element.text.strip()
        only_price = currency_price[1:]
        final_value = only_price.replace(",", "")
        self.price = float(final_value)
        return self.price

    def json(self) -> Dict:
        return {
            "item_id": self.itemid,
            "url": self.url,
            "tag": self.tag,
            "query": self.query
        }

    @classmethod
    def all(cls):
        items_from_db = Database.findall("items", {})
        return [item for item in items_from_db]

    def save_to_mongo(self) -> None:
        Database.insert(self.collection, self.json())