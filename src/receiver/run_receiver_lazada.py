from receiver_lazada import ReceiverLazada
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    receiver = ReceiverLazada()
    receiver.start_receiver(queue=config['DEFAULT_QUEUE']['QUEUE_LAZADA'], prefetch_count=100, durable=True)
