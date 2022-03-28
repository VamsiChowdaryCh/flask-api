from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

source_data = {"abc-1" : "I am abc-1", "abc-2" : "I am abc-2",
            "xyz-1" : "I am xyz-1", "xyz-2" : "I am xyz-2"}

parser = reqparse.RequestParser()

class GetSourceData(Resource):
    def get(self, key):
        return source_data[key]
        

class SetSourceData(Resource):
    def post(self):
        parser.add_argument("key")
        parser.add_argument("value")
        args = parser.parse_args()
        source_data[args["key"]] = args["value"]
        return source_data[args["key"]], 201
    
class SearchPrefix(Resource):
    def get(self):
        parser.add_argument("prefix")
        args = parser.parse_args()
        return_prefix_list = []
        for key in source_data.keys():
            ind = len(args["prefix"])
            if args["prefix"] == key[:ind]:
                return_prefix_list.append(key)
        return return_prefix_list

class SearchSuffix(Resource):
    def get(self):
        parser.add_argument("suffix")
        args = parser.parse_args()
        return_suffix_list = []
        for key in source_data.keys():
            key_len = len(key)
            ind = key_len - len(args["suffix"])
            if args["suffix"] == key[ind:]:
                return_suffix_list.append(key)
        return return_suffix_list

api.add_resource(GetSourceData, '/get/<key>')
api.add_resource(SetSourceData, '/set/')
api.add_resource(SearchPrefix, '/searchPrefix')
api.add_resource(SearchSuffix, '/searchSuffix')


if __name__ == "__main__":
  app.run(debug=True)
