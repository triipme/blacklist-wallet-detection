from flask import Flask, jsonify
from flask_restful import Api, Resource
from request import get_all_relatives

class Relatives(Resource):
    def get(self):
        try:
            relatives_json = get_all_relatives()
            return jsonify(relatives_json)
        except:
            return {'msg': "Something's happened"}, 500