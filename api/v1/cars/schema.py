from marshmallow import post_load

from api.extensions import ma

from api.v1.cars.model import Car


class CarSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('brand', 'capacity', 'year_manufacture')

    @post_load
    def make_object(self, data):
        assert 'brand' in data and 'year_manufacture' in data, "Must specify brand and year_manufacture in request"

        return Car(data['brand'], capacity=data['capacity'], year_manufacture=data['year_manufacture'])

car_schema = CarSchema()
cars_schema = CarSchema(many=True)

