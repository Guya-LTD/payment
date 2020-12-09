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

from flask_restplus import Namespace, fields

from payment.blueprint.v1.transaction import namespace

class TransactionDto:
    """Request and Respons Data Transfer Object"""

    request = namespace.model('transaction_request', {
    })


    response = namespace.model('transaction_response', {
    })