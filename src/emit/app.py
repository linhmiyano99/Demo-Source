import configparser

from lazada import CrawlerLazada

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from crawler_shopee import CrawlerShopee

config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__)
api = Api(app)
lazada = CrawlerLazada()
shopee = CrawlerShopee()


class EmitLazada(Resource):
    def post(self):
        # Step 1 get the posted data
        postedData = request.get_json()
        url = config['CRAWLER_PATH']['URL_LAZADA'] if "url" not in postedData else postedData["url"]
        queue = config['DEFAULT_QUEUE']['QUEUE_LAZADA'] if "queue" not in postedData else postedData["queue"]

        lazada.crawl_by_url(
            url=url,
            queue=queue,
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
        postedData = request.get_json()
        url = config['CRAWLER_PATH']['URL_SHOPEE'] if "url" not in postedData else postedData["url"]
        queue = config['DEFAULT_QUEUE']['QUEUE_SHOPEE'] if "queue" not in postedData else postedData["queue"]

        shopee.crawl_by_url(
            url=url,
            queue=queue,
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
