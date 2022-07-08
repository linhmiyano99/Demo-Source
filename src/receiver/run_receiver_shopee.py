from receiver_shopee import ReceiverShopee
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    receiver = ReceiverShopee()
    receiver.start_receiver(queue=config['DEFAULT_QUEUE']['QUEUE_SHOPEE'], prefetch_count=100, durable=True)
