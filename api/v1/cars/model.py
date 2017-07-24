import logging
from datetime import datetime
from os import environ

from application import app
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute
)

if environ.get('APP_ENV') == 'DEVELOPMENT':
    logging.basicConfig()
    log = logging.getLogger("pynamodb")
    log.setLevel(logging.DEBUG)
    log.propagate = True


class Car(Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "cars"

        if environ.get('APP_ENV') == 'PRODUCTION':
            region = app.config.get('DYNAMO_REGION')

        if environ.get('APP_ENV') == 'DEVELOPMENT':
            host = "http://localhost:8000"

    brand = UnicodeAttribute(hash_key=True)
    capacity = NumberAttribute(default=4)
    year_manufacture = NumberAttribute(null=True)
    updated_at = UTCDateTimeAttribute(default=datetime.now())
    created_at = UTCDateTimeAttribute(default=datetime.now())


# Create the table
if not Car.exists():
    Car.create_table(wait=True)
