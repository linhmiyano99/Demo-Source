import abc
import pika
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class Crawler:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=config['HOST']['LOCAL_HOST']
            )
        )

    @abc.abstractmethod
    def crawl_by_url(self, url, queue, durable=True):
        pass

    def close_connection(self):
        self.connection.close()

