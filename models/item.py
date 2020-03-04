import requests
from bs4 import BeautifulSoup

class Item:
    def __init__(self, url, tag, query):
        self.url = url
        self.tag = tag
        self.query = query

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