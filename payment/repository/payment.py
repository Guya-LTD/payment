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
from ..model.payment import Payment as PaymentEntity
from .mixins.transaction_mixin import TransactionMixin
from .mixins.timestamp_mixin import TimestampMixin
from .mixins.user_mixin import UserMixin

class Payment(db.Document, PaymentEntity, TransactionMixin, TimestampMixin, UserMixin):
    """Payment ODM
    ...
    
    Attributes
    ----------
    _id : String 
        Auto inherated attribute, 12-byte, 24 char hexadicmal

    user_id : String
        Customer id

    order_tracking_id : String

    """

    PENDING = 'pending'

    COMPLETE = 'complete'

    FAILED = 'failed'

    SENT = 'sent'

    MANUEL = 'manuel'

    AUTOMATIC = 'automatic'

    STATUS_CHOICES = (
        PENDING,
        COMPLETE,
        FAILED
    )

    EMAIL_STATUS_CHOICE = (
        PENDING,
        SENT,
        FAILED
    )

    APPROVAL_METHOD_CHOICE = (
        MANUEL,
        AUTOMATIC
    )


    #user_id = db.StringField(required = False)

    invoice_number = db.StringField(required = True)

    status = db.StringField(required = True, default = PENDING, choices = STATUS_CHOICES )

    email_status =  db.StringField(required = True, default = PENDING, choices = EMAIL_STATUS_CHOICE )

    approval_method = db.StringField(required = False, choices = APPROVAL_METHOD_CHOICE )

    ## Holds faild reason or other flags
    flag = db.StringField()