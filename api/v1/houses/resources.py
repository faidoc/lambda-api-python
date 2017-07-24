from botocore.exceptions import ClientError
from flask import jsonify, request
from flask_restful import Api, Resource
from pynamodb.exceptions import PutError

from api.v1.blueprints import house_endpoint

from api.v1.houses.model import House
from api.v1.houses.schema import house_schema
from api.v1.houses.schema import houses_schema


class HouseList(Resource):

    def get(self):
        result = houses_schema.dump(house.scan())
        return jsonify(result.data)

    def post(self):
        input_data = request.get_json()

        try:
            if not input_data:
                return {"success": False, "msg": "malformed request"}, 400
            else:
                house_object = house_schema.load(input_data).data
                house_object.save(name__null=True)

                return {"success": True}, 201
        except AssertionError as a_error:
            return {"success": False, "msg": str(a_error)}, 400
        except PutError as e:
            if isinstance(e.cause, ClientError):
                code = e.cause.response['Error'].get('Code')
                message = e.cause.response['Error'].get('Message')
                return {"success": False, "msg": str(message), "code": str(code)}, 400

api = Api(house_endpoint)
house = House()
api.add_resource(HouseList, '')
