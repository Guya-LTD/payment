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
from flask_restplus import Api
from flask import Blueprint

from payment.main.controller.payment_controller import api as payment_api

blueprint = Blueprint('api', '__main__')

api = Api(
    blueprint,
    title = 'PAYMENT SERVICE RESTful API',
    version = '1.0.0',
    description = 'Guya\'s E-commerce Payment API',
    prefix='/api',
    #url_prefix=''
)



# apis
#api.add_namespace(payment_api, path = '/api/v1/auth/payments')
api.add_namespace(payment_api, path = '/v1/payments')