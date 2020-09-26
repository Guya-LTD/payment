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
from payment.database import db
from ..model.transaction import Transaction as TransactionEntity
from .mixins.user_mixin import UserMixin
from .mixins.timestamp_mixin import TimestampMixin
from .mixins.transaction_mixin import TransactionMixin

class Transaction(db.Document, TransactionEntity, UserMixin, TimestampMixin, TransactionMixin):
    """Transaction ODM
    ...
    
    Attributes
    ----------
    _id : String 
        Auto inherated attribute, 12-byte, 24 char hexadicmal

    amount : Float
        Amount 

    flag : String
        Note or amount is not wright
    """

    amount = db.FloatField(required=True)

    flag = db.StringField()