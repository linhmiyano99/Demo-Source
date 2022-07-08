from crawler_shopee import CrawlerShopee
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    crawler = CrawlerShopee()
    crawler.crawl_by_url(
        url=config['CRAWLER_PATH']['URL_SHOPEE'],
        queue=config['DEFAULT_QUEUE']['QUEUE_SHOPEE'],
        durable=True
    )
