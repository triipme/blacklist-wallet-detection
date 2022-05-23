import json
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from request import get_all_relatives
from settings import config

class Relatives(Resource):
    def get(self):
        try:
            relatives_json = get_all_relatives(config.holder)
            return jsonify(relatives_json)
        except Exception as ex:
            return {
                'msg': "Something's happened",
                'exception': ex
            }
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('holder', required=True)
            args = parser.parse_args()
            relatives_json = get_all_relatives(args['holder'])
            return jsonify(relatives_json)
        except Exception as ex:
            return {
                'msg': "Something's happened",
                'exception': ex
            }