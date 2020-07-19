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
import unittest
import json
from manager import app as test_app
import requests
class TestPaymentApi(unittest.TestCase):
    def setUp(self):
        # creating a FlaskClient instance to interact with the app
        self.app = test_app.test_client()

    

    #def test_raise(self):
        # this won't raise a Python exception but return a 500
     #   res = self.app.get('/api/v1/payments')
      #  body = json.loads(str(res.data, 'utf8'))
       # self.assertEqual(body['code'], 500)

    

    def test_payment_post_api(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            order_tracking_id = '94820',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        print(res.data)
        # asserting status code
        self.assertEqual(res.status_code, 201)

    