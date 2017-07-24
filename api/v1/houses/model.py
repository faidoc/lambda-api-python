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


class House(Model):
    class Meta:
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "houses"

        if environ.get('APP_ENV') == 'PRODUCTION':
            region = app.config.get('DYNAMO_REGION')

        if environ.get('APP_ENV') == 'DEVELOPMENT':
            host = "http://localhost:8000"

    name = UnicodeAttribute(hash_key=True)
    capacity = NumberAttribute(default=0)
    updated_at = UTCDateTimeAttribute(default=datetime.now())
    created_at = UTCDateTimeAttribute(default=datetime.now())


# Create the table
if not House.exists():
    House.create_table(wait=True)
