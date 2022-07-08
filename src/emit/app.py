import configparser

from crawler_lazada import CrawlerLazada

from flask import Flask, jsonify
from flask_restful import Api, Resource

from crawler_shopee import CrawlerShopee

config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__)
api = Api(app)
crawler = CrawlerLazada()


class EmitLazada(Resource):
    def post(self):
        # Step 1 get the posted data
        # postedData = request.get_json()
        #
        # url = postedData["url"]

        crawler.crawl_by_url(
            url=config['CRAWLER_PATH']['URL_LAZADA'],
            queue=config['DEFAULT_QUEUE']['QUEUE_LAZADA'],
            durable=True
        )
        retJson = {
            "status": 200,
            "sentence": "lazada crawl completed"
        }
        return jsonify(retJson)


class EmitShopee(Resource):
    def post(self):
        # Step 1 get the posted data
        # postedData = request.get_json()
        #
        # url = postedData["url"]

        crawler = CrawlerShopee()
        crawler.crawl_by_url(
            url=config['CRAWLER_PATH']['URL_SHOPEE'],
            queue=config['DEFAULT_QUEUE']['QUEUE_SHOPEE'],
            durable=True
        )
        retJson = {
            "status": 200,
            "sentence": "shopee crawl completed"
        }
        return jsonify(retJson)


api.add_resource(EmitLazada, "/emit_lazada")
api.add_resource(EmitShopee, "/emit_shopee")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
