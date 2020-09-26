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

class PaymentDto:
    """Request and Respons Data Transfer Object"""

    api = Namespace('Payment', description = 'Footstep related operations')


    request = api.model('payment_request', {
        #'user_id' : fields.String(required = True, description = ''),
        'invoice_number' : fields.String(required = True, description = ''),
        'transaction_id' : fields.String(required = True, description = ''),
        'transaction_date' : fields.String(required = True, description = ''),
        'transaction_medium' : fields.String(required = True, description = ''),
    })


    response = api.model('payment_response', {
    })