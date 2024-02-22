# se van a concentrar las confguraciones a inplementra 
# acceso a base de datos

import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY='clave nueva'
    SESSION_COOKIE_SECURE =False
    
    
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URL='mysql+pymysql://brenda:root@127.0.0.1/bdidgs801'
    SQLALQUEMY_TRANCK_MODIFICATIONS=False
    


