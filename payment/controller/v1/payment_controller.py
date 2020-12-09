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
        - Payment namespace
"""

"""REST API Controller

Responses List :
    1xx -> :            Informational response - The request was received, continuing process
        * 100           Continue
        * 101           Switching Protocols
        * 102           Processing
        * 103           Early Hints (RFC 8297)

    2xx -> :            Successful - The request was successfully received, understood, and accepted
        * 200           Ok
        * 201           Created
        * 202           Accepted
        * 203           Non-Authoritative Information
        * 204           No Content
        * 205           Reset Content
        * 206           Partial Content
        * 207           Multi-Status
        * 208           Already Reported
        * 226           IM Used

    3xx -> :            Redirection - Further action needs to be taken in order to complete the request
        * 300           Multiple Choices
        * 301           Moved Permanently
        * 302           Found (Previously "Moved temporarily")
        * 303           See Other
        * 304           Not Modified
        * 305           Use Proxy
        * 306           Switch Proxy
        * 307           Temporary Redirect
        * 308           Permanent Redirect

    4xx -> :            Client Error - The request contains bad syntax or cannot be fulfilled
        * 400           Bad  Request
        * 401           Unauthorized
        * 402           Payment Required
        * 403           Forbidden
        * 404           Not Found
        * 405           Method Not Allowed
        * 406           Not Acceptable
        * 407           Proxy Authentication Required
        * 408           Request Timeout
        * 409           Conflict
        * 410           Gone
        * 411           Length Required
        * 412           Precondition Failed
        * 413           Payload Too Large
        * 414           URI Too Long
        * 415           Unsupported Media Type
        * 416           Range Not Satisfiable
        * 417           Expection Failed
        * 418           I'm a teapot
        * 421           Misdirected Request
        * 422           Unprocessable Entity
        * 423           Locked
        * 424           Failed Dependency
        * 425           Too Early
        * 426           Upgrade Required
        * 428           Precondition Required
        * 429           Too Many Requests
        * 431           Request Header Fields Too Large
        * 451           Unavailable For Legal Reasons

    5xx -> :            Server Error - The server failed to fulfil an apparently valid request
        * 500           Internal Server Error
        * 501           Not Implemented
        * 502           Bad Gateway
        * 503           Service Unavaliable
        * 504           Gateway Timeout
        * 505           HTTP Version Not Supported
        * 506           Variant Also Negotiates
        * 507           Insufficent Storage
        * 508           Loop Detected
        * 510           Not Extended
        * 511           Network Authentication Required


Functions:
    * get - returns list of datas
    * post - returns creation status with the newly created resource link
    * put - return update status with the the newly updated resource link
    * patch - returns the semi updated status with the newly semi updated resource link
    * delete - return delation status

"""
from flask import request, jsonify, make_response
from flask_restplus import Resource
from werkzeug.exceptions import InternalServerError
from bson import ObjectId

from payment.repository.payment import Payment
from payment.dto.payment_dto import PaymentDto
from payment.blueprint.v1.payment import namespace
from payment.exception import ValueEmpty, InvalidObjectId, DocumentDoesNotExist
from payment.middleware.jwt_auth_middleware import JWTAuthMiddleWare

@namespace.route('')
class PaymentList(Resource):
    """Payment Related Operation

    ...

    `asc'  +
    `desc` -


    Attributes
    ----------
    LIMIT : Integer
        Max allowed rows

    Methods
    -------
    get() :
        Get All/Semi datas from database

    post() :
        Save data/datas to database

    """
    _LIMIT = 10

    @namespace.header('Authorization', 'Jwt Token')
    def get(self):
        """Get All/Semi datas from database

        ...

        Query Examples:
            * Filtering :
                - name.en=eq:abc&name.am=neq:abc

        Returns
        -------
            Json Dictionaries

        """
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', self._LIMIT))
        filters = {}
        order_by = request.args.get('order_by')

        for key in request.args:
            if key not in ['page', 'limit', 'sort_by', 'order_by']:
                splited = request.args.get(key).split(':')
                value = splited[1]
                try: 
                    value = ast.literal_eval(value)
                except ValueError:
                    pass 

                filters[key] = {'$%s' % splited[0] :  value}

        payments = Payment.objects(__raw__ = filters).order_by(order_by).paginate( page = page, per_page = limit).items

        return make_response(jsonify({
            'status_code': 200,
            'status': 'Ok',
            'message': 'All Payments',
            'data': payments,
            'pagination': {
                'count': Payment.objects.count(),
                'limit': limit,
                'page': page
            }
        }), 200)

    @namespace.expect(PaymentDto.request, validate = True)
    def post(self):
        """Save data/datas to database

        ...

        Returns
        -------
            Json Dictionaries

        """
        ## Payments entered by not a client

        jwtAuthMiddleWare = JWTAuthMiddleWare(request)
        auth = jwtAuthMiddleWare.authorize()
        # If auth is false break and return response to client
        # Else jwtAuthMiddleWare holds decoded users data
        if not auth:
            return jwtAuthMiddleWare.response

        # start by validating request fields for extra security
        # step 1 validation: strip payloads for empty string
        if not namespace.payload['invoice_number'].strip() or \
           not namespace.payload['transaction_id'].strip() or \
           not namespace.payload['transaction_date'].strip() or \
           not namespace.payload['transaction_medium'].strip():
           raise ValueEmpty({'payloads': namespace.payload})
        
        # init new payment object
        payment = Payment(
            invoice_number = namespace.payload['invoice_number'],
            transaction_id = namespace.payload['transaction_id'],
            transaction_date = namespace.payload['transaction_date'],
            transaction_medium = namespace.payload['transaction_medium'],
            created_by = str(jwtAuthMiddleWare.user["data"]["id"])
        )
        
        # persist to db
        payment.save()

        # if persisted in to db return id
        if isinstance(payment.id, ObjectId):
            return make_response(jsonify({
                'status_code': 201,
                'status': 'Created'
            }), 201)
        else:
            raise InternalServerError({'payloads': namespace.payload, 'description': 'Server failed to save payload'})


@namespace.route('/<string:id>')
class PaymentResource(Resource):
    """"Single Payment Related Operation

    ...

    Methods
    -------
    get(id:String) :
        Get a data from database

    put(id:String) :
        Update a data from database

    delete(id:String) :
        Delete a data from database

    """

    def get(self, id):
        """Get All/Semi datas from database

        ...

        Parameters
        ----------
        id : integer
            Object Id, i.e 12-byte, 24 char hexadicmal

        Returns
        -------
            Json Dictionaries

        """
        # start by validating request fields for extra security
        # step 1 validation: valid if id is 12-hex
        if not ObjectId.is_valid(id):
            raise InvalidObjectId({'payloads': [{'id': id}]})

        # retrieve a result that should be unique in the collection, use get(). 
        # this will raise DoesNotExist if no document matches the query, 
        # and MultipleObjectsReturned if more than one document matched the query
        payment = Payment.objects.get(id = id)

        return make_response(jsonify({
            'status_code': 200,
            'status': 'OK',
            'datas': [payment]
        }), 200)



    @namespace.expect(PaymentDto.request, validate = True)
    def put(self, id):
        """Update a data from database

        ...

        Parameters
        ----------
        id : String
            Object Id, i.e 12-byte, 24 char hexadicmal

        Returns
        -------
            Json Dictionaries

        """
        jwtAuthMiddleWare = JWTAuthMiddleWare(request)
        auth = jwtAuthMiddleWare.authorize()
        # If auth is false break and return response to client
        # Else jwtAuthMiddleWare holds decoded users data
        if not auth:
            return jwtAuthMiddleWare.response

        # start by validating request fields for extra security
        # step 1 validation: valid if id is 12-hex
        if not ObjectId.is_valid(id):
            raise InvalidObjectId({'payloads': [{'id': id}]})

        # step 2 validation: check if document exists in collection
        if not Payment.objects(id = id):
            raise DocumentDoesNotExist({'payloads': [{'id': id}]})

        # step 3 validation: strip payloads for empty string
        if not namespace.payload['invoice_number'].strip() or \
           not namespace.payload['transaction_id'].strip() or \
           not namespace.payload['transaction_date'].strip() or \
           not namespace.payload['transaction_medium'].strip():
           raise ValueEmpty({'payloads': namespace.payload})

        # update sets
        payment = Payment.objects(id = id).update(
            invoice_number = namespace.payload['invoice_number'],
            transaction_id = namespace.payload['transaction_id'],
            transaction_date = namespace.payload['transaction_date'],
            transaction_medium = namespace.payload['transaction_medium'],
            updated_by = str(jwtAuthMiddleWare.user["data"]["id"])
        )

        # save to db
        #payment.reload()

        #if isinstance(payment.id, ObjectId):
        if payment:
            return make_response(jsonify({
                'status_code': 200,
                'status': 'OK',
            }), 200)
        else:
            raise InternalServerError({'payloads': namespace.payload, 'description': 'Server failed to update document'})


    def delete(self, id):
        # start by validating request fields for extra security
        # step 1 validation: strip payloads for empty string
        if not id.strip():
           raise ValueEmpty({'payloads': {'id': id}})

        # the query may be filtered by calling the QuerySet object 
        # with field lookup keyword arguments. The keys in the keyword 
        # arguments correspond to fields on the Document you are querying
        payments = Payment.objects(id = id).delete()

        return make_response(jsonify({
            "status_code": 200,
            "status": "OK",
            "message": "Payment deleted"
        }), 200)