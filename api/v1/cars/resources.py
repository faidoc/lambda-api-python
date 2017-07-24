from botocore.exceptions import ClientError
from flask import jsonify, request
from flask_restful import Api, Resource
from pynamodb.exceptions import PutError

from api.v1.blueprints import car_endpoint

from api.v1.cars.model import Car
from api.v1.cars.schema import car_schema
from api.v1.cars.schema import cars_schema


class CarList(Resource):

    def get(self):
        result = cars_schema.dump(house.scan())
        return jsonify(result.data)

    def post(self):
        input_data = request.get_json()

        try:
            if not input_data:
                return {"success": False, "msg": "malformed request"}, 400
            else:
                house_object = car_schema.load(input_data).data
                house_object.save(brand__null=True)

                return {"success": True}, 201
        except AssertionError as e:
            return {"success": False, "msg": str(e)}, 400
        except PutError as e:
            if isinstance(e.cause, ClientError):
                code = e.cause.response['Error'].get('Code')
                message = e.cause.response['Error'].get('Message')
                return {"success": False, "msg": str(message), "code": str(code)}, 400

api = Api(car_endpoint)
house = Car()
api.add_resource(CarList, '')
