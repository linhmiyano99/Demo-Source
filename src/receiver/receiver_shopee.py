# import requests
import json
from receiver import Receiver
from csv import writer
from urllib.request import Request, urlopen

import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class ReceiverShopee(Receiver):
    def __init__(self):
        super().__init__()

    def callback(self, ch, method, properties, body):

        print("Start queue")
        list_id = json.loads(body.decode())
        list_item = []
        for item_id in list_id:
            url = config['CRAWLER_PATH']['URL_PDF_SHOPEE'].format(item_id['itemid'],
                                                                  item_id['shopid'])
            req = Request(url,
                          headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})
            raw_data = json.loads(urlopen(req).read().decode('utf-8'))['data']
            title = raw_data['name']
            brand_name = raw_data['brand']
            selling_price = int(raw_data['price_max'] / 100000)
            recommend_price = int(raw_data['price_max_before_discount'] / 100000)
            sold = raw_data['sold']
            list_item.append([title, brand_name, selling_price, recommend_price, sold])

        with open('output/crawler_shopee.csv', 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            for item in list_item:
                csv_writer.writerow(item)
        print("End queue")
