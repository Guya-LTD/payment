"""Header

Copyright
---------
    Copyright (C) Guya , PLC - All Rights Reserved (As Of Pending...)
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential

LICENSE
-------
    This file is subject to the terms and conditions defined in
    file 'LICENSE.txt', which is part of this source code package.

Authors
-------
    * [Simon Belete](https://github.com/Simonbelete)
 
Project
-------
    * Name: 
        - Guya E-commerce & Guya Express
    * Sub Project Name:
        - Payment Service
    * Description
        - Payment api
"""
""" Config class. """
import os 
 
class Config:
    """Base config vars.""" 
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_5x'
    
    DEBUG = os.environ.get('DEBUG') or True
    
    TESTING = os.environ.get('TESTING') or True

    MONGODB_DB = os.environ.get('DB_NAME') or 'payment_db'
    
    MONGODB_HOST = os.environ.get('DB_HOST') or 'mongo'

    MONGODB_PORT =  int(os.environ.get('DB_PORT') or 27017)


class Prodconfig(Config):
    pass



class DevConfig(Config):
    pass


   
class TestConfig(Config):
    pass


config_by_name = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=Prodconfig
)