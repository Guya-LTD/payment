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
from pymongo import errors as pymongoErrors

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

    # register http code errors
    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)

    ## pymongo exception handlers
    def pymongo_generic_error_handler(error):
        # formatting the exception
        result = {
            'code': 500, 
            'description': 'Internal Server Error', 
            'type': 'pymongo.errors',
            'message': str(error)}

        # logg exception
        #logger.exception(str(error), extra=result.update(EXTRA))
        resp = jsonify(result)
        resp.status_code = 500
        return resp

    def pymongo_auto_reconnect_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_bulkwrite_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_collection_invalid_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_configuration_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_connection_failure_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_cursor_not_found_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_document_too_large_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_duplicate_key_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_encryption_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_exceede_max_waiters_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_execution_timeout_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_invalid_name_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_invalid_operation_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_invalid_uri_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_network_timeout_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_not_master_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_operation_failure_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_protocol_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_pymongo_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_server_selection_timeout_error_handler(error): 
        return pymongo_generic_error_handler(error)

    def pymongo_wtimeout_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_write_concern_error_handler(error):
        return pymongo_generic_error_handler(error)

    def pymongo_write_error_handler(error):
        return pymongo_generic_error_handler(error)

    # register errors
    app.register_error_handler(pymongoErrors.AutoReconnect, pymongo_auto_reconnect_error_handler)
    app.register_error_handler(pymongoErrors.BulkWriteError, pymongo_bulkwrite_error_handler)
    app.register_error_handler(pymongoErrors.CollectionInvalid, pymongo_collection_invalid_error_handler)
    app.register_error_handler(pymongoErrors.ConfigurationError, pymongo_configuration_error_handler)
    app.register_error_handler(pymongoErrors.ConnectionFailure, pymongo_connection_failure_error_handler)
    app.register_error_handler(pymongoErrors.CursorNotFound, pymongo_cursor_not_found_error_handler)
    app.register_error_handler(pymongoErrors.DocumentTooLarge, pymongo_document_too_large_error_handler)
    app.register_error_handler(pymongoErrors.DuplicateKeyError, pymongo_duplicate_key_error_handler)
    app.register_error_handler(pymongoErrors.EncryptionError, pymongo_encryption_error_handler)
    app.register_error_handler(pymongoErrors.ExceededMaxWaiters, pymongo_exceede_max_waiters_error_handler)
    app.register_error_handler(pymongoErrors.ExecutionTimeout, pymongo_execution_timeout_error_handler)
    app.register_error_handler(pymongoErrors.InvalidName, pymongo_invalid_name_error_handler)
    app.register_error_handler(pymongoErrors.InvalidOperation, pymongo_invalid_operation_error_handler)
    app.register_error_handler(pymongoErrors.InvalidURI, pymongo_invalid_uri_error_handler)
    app.register_error_handler(pymongoErrors.NetworkTimeout, pymongo_network_timeout_error_handler)
    app.register_error_handler(pymongoErrors.NotMasterError, pymongo_not_master_error_handler)
    app.register_error_handler(pymongoErrors.OperationFailure, pymongo_operation_failure_error_handler)
    app.register_error_handler(pymongoErrors.ProtocolError, pymongo_protocol_error_handler)
    app.register_error_handler(pymongoErrors.PyMongoError, pymongo_pymongo_error_handler)
    app.register_error_handler(pymongoErrors.ServerSelectionTimeoutError, pymongo_server_selection_timeout_error_handler)
    app.register_error_handler(pymongoErrors.WTimeoutError, pymongo_wtimeout_error_handler)
    app.register_error_handler(pymongoErrors.WriteConcernError, pymongo_write_concern_error_handler)
    app.register_error_handler(pymongoErrors.WriteError, pymongo_write_error_handler)

    ## Mongoengine Exception handlers
    def mongoengine_generic_error_handler(error, code = 500):
        # formatting the exception
        result = {
            'code': 500, 
            'description': 'Internal Server Error', 
            'type': 'mongoengine.errors',
            'message': str(error)}

        # logg exception
        #logger.exception(str(error), extra=result.update(EXTRA))
        resp = jsonify(result)
        resp.status_code = code
        return resp

    def mongoengine_not_registered_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_invalid_document_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_lookup_error_handler(error):
        return mongoengine_generic_error_handler(error)

    def mongoengine_does_not_exist_error_handler(error):
        return mongoengine_generic_error_handler(error = error, code = 204)

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