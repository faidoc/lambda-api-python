"""All Flask blueprints for the entire application.

All blueprints for all endpoints. They shall be imported by the controllers themselves and by cleanclick.py. Blueprint
URL paths are defined here as well.
"""

from flask import Blueprint

API_VERSION = 'v1'


def _factory(partial_module_string, url_prefix):
    """Generates blueprint objects for view modules.

    Positional arguments:
    partial_module_string -- string representing the blueprint name.
    url_prefix -- URL prefix passed to the blueprint.

    Returns:
    Blueprint instance.
    """
    name = partial_module_string
    import_name = 'api.{}.{}.resources'.format(API_VERSION, partial_module_string)
    blueprint = Blueprint(name, import_name, url_prefix=url_prefix)
    return blueprint


house_endpoint = _factory('houses', '/{}/houses'.format(API_VERSION))
car_endpoint = _factory('cars', '/{}/cars'.format(API_VERSION))


all_blueprints = (house_endpoint, car_endpoint)
