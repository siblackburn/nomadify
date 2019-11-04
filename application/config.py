import os


class Config(object):

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '12345'
    
    # sqlite
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

    # postgres
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='postgres',pw='mysecretpassword',url='localhost',db='postgres')

    # mysql
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USERNAME', 'siblackburn')
    db_schema = os.environ.get('DB_SCHEMA', 'nomadify')
    db_password = os.environ.get('DB_PASSWORD')
    # print(db_password)
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_schema}'



class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True