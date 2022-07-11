import configparser

from receiver_lazada import ReceiverLazada

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from receiver_shopee import ReceiverShopee

config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__)
api = Api(app)


class EmitLazada(Resource):

    def post(self):
        # Step 1 get the posted data
        postedData = request.get_json()
        queue = config['DEFAULT_QUEUE']['QUEUE_LAZADA'] if "queue" not in postedData else postedData["queue"]

        lazada = ReceiverLazada()

        lazada.start_receiver(queue=queue, prefetch_count=100, durable=True)

        retJson = {
            "status": 200,
            "sentence": "lazada crawl completed"
        }
        return jsonify(retJson)


class EmitShopee(Resource):

    def post(self):
        # Step 1 get the posted data
        postedData = request.get_json()
        queue = config['DEFAULT_QUEUE']['QUEUE_SHOPEE'] if "queue" not in postedData else postedData["queue"]
        shopee = ReceiverShopee()
        shopee.start_receiver(queue=queue, prefetch_count=100, durable=True)

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
