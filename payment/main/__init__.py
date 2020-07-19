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
from flask import Flask, jsonify, abort
from flask_mongoengine import MongoEngine
from werkzeug.exceptions import HTTPException, default_exceptions

from .config import config_by_name, os

# mongoengine
db = MongoEngine()

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
    'app_name': 'Payment Sevrice',      
    'environment': ENV,  
    'container_host': HOST,
    'port': PORT,
    'sys': {
        'lang': 'python',
        'version': str(sys.version),
        'version_info': repr(sys.version_info)
    }
}

# Jsonify 1xx, 2xx, 3xx, 4xx, 5xx errors 
def JsonApp(app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {
                'code': error.code, 
                'description': error.description, 
                'type': 'HTTPException',
                'message': str(error)}
        else:
            result = {
                'code': 500, 
                'description': 'Internal Server Error',
                'type': 'Other Exceptions',
                'message': str(error)}

        #logger.exception(str(error), extra=result.update(EXTRA))
        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)

    ## Mongoengine Exception handlers
    def mongoengine_generic_error_handler(error):
        # formatting the exception
        result = {
            'code': 500, 
            'description': 'Internal Server Error', 
            'type': 'mongoengine.errors',
            'message': str(error)}

        # logg exception
        #logger.exception(str(error), extra=result.update(EXTRA))
        resp = jsonify(result)
        resp.status_code = 500
        return resp

    def mongoengine_not_registered_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_invalid_document_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_lookup_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_does_not_exist_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_multiple_objects_returned_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_invalid_query_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_operation_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_not_unique_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_bulk_write_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_file_doesnot_exist_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_validation_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_save_condition_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_deprecated_error_handler(error):
        return mongoengine_generic_error_handler(error)

    # register mongoengine exceptions    
    app.register_error_handler(db.NotRegistered, mongoengine_not_registered_error_handler)
    app.register_error_handler(db.InvalidDocumentError, mongoengine_invalid_document_error_handler)
    app.register_error_handler(db.LookUpError, mongoengine_lookup_error_handler)
    app.register_error_handler(db.DoesNotExist, mongoengine_does_not_exist_error_handler)
    app.register_error_handler(db.MultipleObjectsReturned, mongoengine_multiple_objects_returned_error_handler)
    app.register_error_handler(db.InvalidQueryError, mongoengine_invalid_query_error_handler)
    app.register_error_handler(db.OperationError, mongoengine_operation_error_handler)
    app.register_error_handler(db.NotUniqueError, mongoengine_not_unique_error_handler)
    app.register_error_handler(db.BulkWriteError, mongoengine_bulk_write_error_handler)
    app.register_error_handler(db.FieldDoesNotExist, mongoengine_file_doesnot_exist_error_handler)
    app.register_error_handler(db.ValidationError, mongoengine_validation_error_handler)
    app.register_error_handler(db.SaveConditionError, mongoengine_save_condition_error_handler)
    app.register_error_handler(db.DeprecatedError, mongoengine_deprecated_error_handler)

    return app
  
# app    
def create_app():
    app = JsonApp(Flask(__name__))
    config_name = ENV
    app.config.from_object(config_by_name[config_name])
    app.testing = True
    db.init_app(app)

    return app