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
from flask_basic import app as tested_app

_404 = ('The requested URL was not found on the server. '
        'If you entered the URL manually please check your '
        'spelling and try again.')

class TestPaymentApi(unittest.TestCase):
    def setup(self):
       # creating a FlaskClient instance to interact with the app
       app = tested_app.test_client()

    def test_proper_404(self):
        # calling a non existing endpoint
        res = self.app.get('/api/v1/payments/dwdwqqwdwqd')

        # yeah it's not there
        self.assertEqual(res.status_code, 404)

        # but we still get a nice JSON body
        body = json.loads(str(res.data, 'utf8'))
        self.assertEqual(body['code'], 404)
        self.assertEqual(body['message'], '404: Not Found')
        self.assertEqual(body['description'], _404)

    def test_raise(self):
        # this won't raise a Python exception but return a 500
        res = self.app.get('/api/v1/payments')
        body = json.loads(str(res.data, 'utf8'))
        self.assertEqual(body['code'], 500)

    def test_payment_get_api(self):
        # calling apis endpoint
        payments = app.get('/api/v1/payments')

        # asserting the body
        body = json.loads(str(hello, 'utf8'))

