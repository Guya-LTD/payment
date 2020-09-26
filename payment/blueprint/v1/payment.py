"""Copyright Header Details

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
        - Payment Microservices service
"""


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style


Blueprint to organize and group, views related
to the '/payments' endpoint of HTTP REST API.
"""

from flask_restplus import Namespace

from . import api

namespace = Namespace('Payment', description = 'Payment api')

api.add_namespace(namespace, path = '/api/v1/payments')