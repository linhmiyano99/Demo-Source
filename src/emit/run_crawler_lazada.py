import configparser

from src.emit.crawler_lazada import CrawlerLazada

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    crawler = CrawlerLazada()

    crawler.crawl_by_url(
        url=config['CRAWLER_PATH']['URL_LAZADA'],
        queue=config['DEFAULT_QUEUE']['QUEUE_LAZADA'],
        durable=True
    )
