import requests
import json
import pika
from crawler import Crawler
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class CrawlerShopee(Crawler):
    def __init__(self):
        super().__init__()

    def crawl_by_url(self, url, queue, durable=True):

        page = requests.get(url)
        html = page.text
        raw_data = json.loads(html)['data']['sections'][0]['data']['item']
        i = 0
        self.channel.queue_declare(queue=queue, durable=durable)
        list_url = []
        for row in raw_data:
            i += 1
            body = {'itemid': row['itemid'], 'shopid': row['shopid']}
            list_url.append(body)
            if i % 20 == 0:
                self.channel.basic_publish(
                    exchange='',
                    routing_key=queue,
                    body=json.dumps(list_url),
                    properties=pika.BasicProperties(
                        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
                    ))
                list_url = []
        self.close_connection()
