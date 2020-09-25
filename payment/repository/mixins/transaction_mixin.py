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

"""`flask-mongoengine` Based ODM

`flask-mongoengine` built up on pymongo engine.

Version Requirements: 
    * flask-mongoengine v0.7
"""
from datetime import datetime
from pytz import timezone

from ... import db

class TransactionMixin(object):
    """Time Stamped Mixin

    Attributes
    ----------
    transaction_id : String
        Bank transaction id/ TAX id

    transaction_date : String
        Transaction submited date as specfied

    transaction_medium : String
        Bank name


    """

    transaction_id = db.StringField(required=True)

    transaction_date = db.StringField(required=True)

    transaction_medium = db.StringField(required=True)

