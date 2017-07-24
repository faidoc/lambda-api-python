from marshmallow import post_load

from api.extensions import ma

from api.v1.houses.model import House


class HouseSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'capacity')

    @post_load
    def make_object(self, data):
        assert 'name' in data and 'capacity' in data, "Must specify name and capacity in request"

        return House(name=data['name'], capacity=data['capacity'])

house_schema = HouseSchema()
houses_schema = HouseSchema(many=True)

