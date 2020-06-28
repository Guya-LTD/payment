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
import sys
import logging
import logstash
from flask import Flask

from .config import config_by_name, os

# app
HOST = os.environ.get('HOST') or '0.0.0.0'
PORT = os.environ.get('PORT') or 5000

#env
ENV = os.getenv('ENV') or 'dev'

# logger 
LOGGER_HOST = os.getenv('LOGGER_HOST') or 'logstash'
LOGGER_PORT = os.getenv('LOGGER_PORT') or 5600

# Logger with app name i.e xtrack.main
logger = logging.getLogger(__name__)         

# logger handler
logger.addHandler(logstash.LogstashHandler(LOGGER_HOST, LOGGER_PORT, version=1))
# logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

# extra logging formats
EXTRA = {
    'app_name': 'Xtrack Sevrice',      
    'environment': ENV,  
    'container_host': HOST,
    'port': PORT,
    'sys': {
        'lang': 'python',
        'version': str(sys.version),
        'version_info': repr(sys.version_info)
    }
} 
  
# app    
def create_app():
    app = Flask(__name__)
    config_name = ENV
    app.config.from_object(config_by_name[config_name])
    
    return app