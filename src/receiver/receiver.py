import abc
import pika
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class Receiver:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=config['HOST']['LOCAL_HOST']
            )
        )
        self.channel = self.connection.channel()

    def start_receiver(self, queue=config['DEFAULT_QUEUE']['QUEUE_LAZADA'], prefetch_count=100, durable=True):
        self.channel.queue_declare(queue=queue, durable=durable)
        self.channel.basic_qos(prefetch_count=prefetch_count)
        self.channel.basic_consume(queue=queue, on_message_callback=self.callback)
        self.channel.start_consuming()

    @abc.abstractmethod
    def callback(self, ch, method, properties, body):
        pass
