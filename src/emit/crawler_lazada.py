import requests
import json
import pika
from crawler import Crawler
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class CrawlerLazada(Crawler):
    def __init__(self):
        super().__init__()

    def crawl_by_url(self, url, queue, durable=True):

        page = requests.get(url)
        html = page.text
        raw_data = json.loads(html)['result']['data']

        i = 0
        channel = self.connection.channel()
        channel.queue_declare(queue=queue, durable=durable)
        list_url = []
        for row in raw_data:
            list_url.append(row['pdpUrl'])
            if i % 20 == 0:
                channel.basic_publish(
                    exchange='',
                    routing_key=queue,
                    body=json.dumps(list_url),
                    properties=pika.BasicProperties(
                        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
                    ))
                list_url = []
        self.close_connection()
