import os


class Config(object):
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class ProductionConfig(Config):
    DEBUG = False
    DYNAMO_REGION = 'us-west-2'


class DevelopmentConfig(Config):
    DEBUG = True
    DYNAMO_DEBUG = True
    DYNAMO_ENABLE_LOCAL = True
    DYNAMO_LOCAL_HOST = 'localhost'
    DYNAMO_LOCAL_PORT = 8000


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DYNAMO_DEBUG = True
    DYNAMO_ENABLE_LOCAL = True
    DYNAMO_LOCAL_HOST = 'localhost'
    DYNAMO_LOCAL_PORT = 8000

