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
from flask import jsonify, make_response
from flask_restplus import Resource
from werkzeug.exceptions import InternalServerError
from bson import ObjectId

from ..repository.payment import Payment
from ..dtos.payment_dto import PaymentDto
from ..exception import ValueEmpty, InvalidObjectId, DocumentDoesNotExist

api = PaymentDto.api
_request = PaymentDto.request
_response = PaymentDto.response

@api.route('')
@api.response(100, 'Continue')
@api.response(101, 'Switching Protocols')
@api.response(102, 'Processing')
@api.response(103, 'Early Hints (RFC 8297)')
@api.response(200, 'Ok')
@api.response(201, 'Created')
@api.response(202, 'Accepted')
@api.response(203, 'Non-Authoritative Information')
@api.response(204, 'No Content')
@api.response(205, 'Reset Content')
@api.response(206, 'Partial Content')
@api.response(207, 'Multi-Status')
@api.response(208, 'Already Reported')
@api.response(226, 'IM Used')
@api.response(300, 'Multiple Choices')
@api.response(301, 'Moved Permanently')
@api.response(302, 'Found (Previously "Moved temporarily")')
@api.response(303, 'See Other')
@api.response(304, 'Not Modified')
@api.response(305, 'Use Proxy')
@api.response(306, 'Switch Proxy')
@api.response(307, 'Temporary Redirect')
@api.response(308, 'Permanent Redirect')
@api.response(400, 'Bad  Request')
@api.response(401, 'Unauthorized')
@api.response(402, 'Payment Required')
@api.response(403, 'Forbidden')
@api.response(404, 'Not Found')
@api.response(405, 'Method Not Allowed')
@api.response(406, 'Not Acceptable')
@api.response(407, 'Proxy Authentication Required')
@api.response(408, 'Request Timeout')
@api.response(409, 'Conflict')
@api.response(410, 'Gone')
@api.response(411, 'Length Required')
@api.response(412, 'Precondition Failed')
@api.response(413, 'Payload Too Large')
@api.response(414, 'URI Too Long')
@api.response(415, 'Unsupported Media Type')
@api.response(416, 'Range Not Satisfiable')
@api.response(417, 'Expection Failed')
@api.response(418, 'I\'m a teapot')
@api.response(421, 'Misdirected Request')
@api.response(422, 'Unprocessable Entity ')
@api.response(423, 'Locked')
@api.response(424, 'Failed Dependency')
@api.response(425, 'Too Early')
@api.response(426, 'Upgrade Required')
@api.response(428, 'Precondition Required')
@api.response(429, 'Too Many Requests')
@api.response(431, 'Request Header Fields Too Large')
@api.response(451, 'Unavailable For Legal Reasons')
@api.response(500, 'Internal Server Error')
@api.response(501, 'Not Implemented')
@api.response(502, 'Bad Gateway')
@api.response(503, 'Service Unavaliable')
@api.response(504, 'Gateway Timeout')
@api.response(505, 'HTTP Version Not Supported')
@api.response(506, 'Variant Also Negotiates')
@api.response(507, 'Insufficent Storage')
@api.response(508, 'Loop Detected')
@api.response(510, 'Not Extended')
@api.response(511, 'Network Authentication Required')
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
        api.abort(405)

    @api.expect(_request, validate = True)
    def post(self):
        """Save data/datas to database

        ...

        Returns
        -------
            Json Dictionaries

        """
        # start by validating request fields for extra security
        # step 1 validation: strip payloads for empty string
        if not api.payload['invoice_number'].strip() or \
           not api.payload['transaction_id'].strip() or \
           not api.payload['transaction_date'].strip() or \
           not api.payload['transaction_medium'].strip():
           raise ValueEmpty({'payloads': api.payload})
        
        # init new payment object
        payment = Payment(
            invoice_number = api.payload['invoice_number'],
            transaction_id = api.payload['transaction_id'],
            transaction_date = api.payload['transaction_date'],
            transaction_medium = api.payload['transaction_medium']
        )
        
        # persist to db
        payment.save()

        # if persisted in to db return id
        if isinstance(payment.id, ObjectId):
            # Return must always include the global fileds :
            # Field           Datatype        Default         Description             Examples
            # -----           --------        -------         -----------             --------
            # code            int             201             1xx, 2xx, 3xx, 5xx
            # description     string          Created         http code description
            # messages        array           Null            any type of messages
            # errors          array           Null            occured errors
            # warnings        array           Null            can be url format
            # datas           array/json      Null            results                 [ {Row 1}, {Row 2}, {Row 3}]
            res = make_response
            return make_response(jsonify({
                'code': 201,
                'description': 'Created',
                'message': None,
                'errors': [],
                'warnings': [],
                'datas': []
            }), 201)
        else:
            raise InternalServerError({'payloads': api.payload, 'description': 'Server failed to save payload'})


@api.route('/<int:id>')
@api.response(100, 'Continue')
@api.response(101, 'Switching Protocols')
@api.response(102, 'Processing')
@api.response(103, 'Early Hints (RFC 8297)')
@api.response(200, 'Ok')
@api.response(201, 'Created')
@api.response(202, 'Accepted')
@api.response(203, 'Non-Authoritative Information')
@api.response(204, 'No Content')
@api.response(205, 'Reset Content')
@api.response(206, 'Partial Content')
@api.response(207, 'Multi-Status')
@api.response(208, 'Already Reported')
@api.response(226, 'IM Used')
@api.response(300, 'Multiple Choices')
@api.response(301, 'Moved Permanently')
@api.response(302, 'Found (Previously "Moved temporarily")')
@api.response(303, 'See Other')
@api.response(304, 'Not Modified')
@api.response(305, 'Use Proxy')
@api.response(306, 'Switch Proxy')
@api.response(307, 'Temporary Redirect')
@api.response(308, 'Permanent Redirect')
@api.response(400, 'Bad  Request')
@api.response(401, 'Unauthorized')
@api.response(402, 'Payment Required')
@api.response(403, 'Forbidden')
@api.response(404, 'Not Found')
@api.response(405, 'Method Not Allowed')
@api.response(406, 'Not Acceptable')
@api.response(407, 'Proxy Authentication Required')
@api.response(408, 'Request Timeout')
@api.response(409, 'Conflict')
@api.response(410, 'Gone')
@api.response(411, 'Length Required')
@api.response(412, 'Precondition Failed')
@api.response(413, 'Payload Too Large')
@api.response(414, 'URI Too Long')
@api.response(415, 'Unsupported Media Type')
@api.response(416, 'Range Not Satisfiable')
@api.response(417, 'Expection Failed')
@api.response(418, 'I\'m a teapot')
@api.response(421, 'Misdirected Request')
@api.response(422, 'Unprocessable Entity ')
@api.response(423, 'Locked')
@api.response(424, 'Failed Dependency')
@api.response(425, 'Too Early')
@api.response(426, 'Upgrade Required')
@api.response(428, 'Precondition Required')
@api.response(429, 'Too Many Requests')
@api.response(431, 'Request Header Fields Too Large')
@api.response(451, 'Unavailable For Legal Reasons')
@api.response(500, 'Internal Server Error')
@api.response(501, 'Not Implemented')
@api.response(502, 'Bad Gateway')
@api.response(503, 'Service Unavaliable')
@api.response(504, 'Gateway Timeout')
@api.response(505, 'HTTP Version Not Supported')
@api.response(506, 'Variant Also Negotiates')
@api.response(507, 'Insufficent Storage')
@api.response(508, 'Loop Detected')
@api.response(510, 'Not Extended')
@api.response(511, 'Network Authentication Required')
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

        # Return must always include the global fileds :
        # Field           Datatype        Default         Description             Examples
        # -----           --------        -------         -----------             --------
        # code            int             201             1xx, 2xx, 3xx, 5xx
        # description     string          Created         http code description
        # messages        array           Null            any type of messages
        # errors          array           Null            occured errors
        # warnings        array           Null            can be url format
        # datas           array/json      Null            results                 [ {Row 1}, {Row 2}, {Row 3}]
        res = make_response
        return make_response(jsonify({
            'code': 200,
            'description': 'OK',
            'message': None,
            'errors': [],
            'warnings': [],
            'datas': [payment]
        }), 200)



    @api.expect(_request, validate = True)
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
        # start by validating request fields for extra security
        # step 1 validation: valid if id is 12-hex
        if not ObjectId.is_valid(id):
            raise InvalidObjectId({'payloads': [{'id': id}]})

        # step 2 validation: check if document exists in collection
        if not Payment.objects(id = id):
            raise DocumentDoesNotExist({'payloads': [{'id': id}]})

        # step 3 validation: strip payloads for empty string
        if not api.payload['invoice_number'].strip() or \
           not api.payload['transaction_id'].strip() or \
           not api.payload['transaction_date'].strip() or \
           not api.payload['transaction_medium'].strip():
           raise ValueEmpty({'payloads': api.payload})

        # update sets
        payment = Payment.objects(id = id).update(
            invoice_number = api.payload['invoice_number'],
            transaction_id = api.payload['transaction_id'],
            transaction_date = api.payload['transaction_date'],
            transaction_medium = api.payload['transaction_medium']
        )

        # save to db
        payment.reload()

        if isinstance(payment.id, ObjectId):
            # Return must always include the global fileds :
            # Field           Datatype        Default         Description             Examples
            # -----           --------        -------         -----------             --------
            # code            int             201             1xx, 2xx, 3xx, 5xx
            # description     string          Created         http code description
            # messages        array           Null            any type of messages
            # errors          array           Null            occured errors
            # warnings        array           Null            can be url format
            # datas           array/json      Null            results                 [ {Row 1}, {Row 2}, {Row 3}]
            res = make_response
            return make_response(jsonify({
                'code': 200,
                'description': 'OK',
                'message': None,
                'errors': [],
                'warnings': [],
                'datas': []
            }), 200)
        else:
            raise InternalServerError({'payloads': api.payload, 'description': 'Server failed to update document'})

    def delete(self, id):
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
        # method not allowed
        api.abort(405)