import json
from nose.tools import *

from tests import test_app


def check_content_type(headers):
    eq_(headers['Content-Type'], 'application/json')


def test_houses_routes():
    rv = test_app.get('/v1/houses')
    check_content_type(rv.headers)
    resp = json.loads(rv.data)
    # make sure we get a response
    eq_(rv.status_code, 200)
    # make sure there are no items
    eq_(len(resp), 0)


def test_houses_create():
    # create a user
    house = dict(name="House Test", capacity=1)
    rv = test_app.post('/v1/houses', data=house)
    check_content_type(rv.headers)
    eq_(rv.status_code, 201)
    