import os

class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY ='moo'


    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
#  email configurations
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #SENDER_EMAIL = os.environ.get('MAIL_uSERNAME')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://omunge:123@localhost/blogs'

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://omunge:123@localhost/blogs'
    DEBUG = True

config_options = {
'development':DevConfig,
#'production':ProdConfig,
'test':TestConfig
}