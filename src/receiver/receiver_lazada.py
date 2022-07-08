import requests
import json
from csv import writer
import re
from receiver import Receiver


class ReceiverLazada(Receiver):
    def __init__(self):
        super().__init__()

    def callback(self, ch, method, properties, body):

        print("Start queue")
        list_url = json.loads(body.decode())
        list_item = []
        for url in list_url:
            page = requests.get(url)

            html = page.text
            data_location = re.search("__moduleData__ = .+}", html)
            raw_html = html[data_location.start() + 17: data_location.end()]
            raw_data = json.loads(raw_html)['data']['root']['fields']['skuInfos']["0"]

            title = raw_data['dataLayer']['pdt_name']
            brand_name = raw_data['dataLayer']['brand_name']
            selling_price = raw_data['price']['salePrice']['value']
            recommend_price = raw_data['price']['originalPrice']['value']
            sold = None
            list_item.append([title, brand_name, selling_price, recommend_price, sold])

        with open('output/crawler_lazada.csv', 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            for item in list_item:
                csv_writer.writerow(item)
        print("End queue")
