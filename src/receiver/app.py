import configparser

from receiver_lazada import ReceiverLazada

from flask import Flask, jsonify
from flask_restful import Api, Resource

from receiver_shopee import ReceiverShopee

config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__)
api = Api(app)
lazada = ReceiverLazada()
shopee = ReceiverShopee()


class EmitLazada(Resource):
    def post(self):
        # Step 1 get the posted data
        # postedData = request.get_json()
        #
        # url = postedData["url"]

        lazada.start_receiver(queue=config['DEFAULT_QUEUE']['QUEUE_LAZADA'], prefetch_count=100, durable=True)

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

        shopee.start_receiver(queue=config['DEFAULT_QUEUE']['QUEUE_SHOPEE'], prefetch_count=100, durable=True)

        retJson = {
            "status": 200,
            "sentence": "shopee crawl completed"
        }
        return jsonify(retJson)


api.add_resource(EmitLazada, "/receiver_lazada")
api.add_resource(EmitShopee, "/receiver_shopee")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
