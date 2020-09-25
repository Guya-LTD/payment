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

class TimestampMixin(object):
    """Time Stamped Mixin

    Attributes
    ----------
    created_at : DateTime

    updated_at : DateTime


    """

    created_at = db.Datetime(default = datetime.now(timezone('Africa/Addis_Ababa')))

    updated_at = db.Datetime(default = datetime.now(timezone('Africa/Addis_Ababa')))

