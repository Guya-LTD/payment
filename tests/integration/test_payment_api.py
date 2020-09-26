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
import pytest
import json
import requests

from payment import create_app

class TestPaymentApi():
    def setup_class(self):
        # creating a FlaskClient instance to interact with the app
        self.app = create_app().test_client()

    def test_payments_get_api(self):
        # calling apis endpoint
        payments = self.app.get('/api/v1/payments')
        # asserting status code
        assert payments.status_code == 405

    def test_payment_post_api_with_empty_payload(self):
        data = dict(
            user_id = '',
            invoice_number = '',
            transaction_id = '',
            transaction_date = '',
            transaction_medium = '' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_non_json_payload(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '94820',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', data=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_with_space_payload(self):
        data = dict(
            user_id = ' ',
            invoice_number = ' ',
            transaction_id = ' ',
            transaction_date = ' ',
            transaction_medium = ' ' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '94820',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 201

    def test_payment_post_api_with_empty_invoice_number(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_with_none_invoice_number(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = None,
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_without_invoice_number_key(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            #invoice_number = '94820',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_test_invoice_number_datatype(self):
        pass

    def test_payment_post_api_test_invoice_number_redundancia(self):
        pass

    def test_payment_post_api_with_empty_transaction_id(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '95555',
            transaction_id = '',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_with_none_transaction_id(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '22223',
            transaction_id = None,
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_without_transaction_id_key(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '94820',
            #transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_test_transaction_id_datatype(self):
        pass    

    def test_payment_post_api_test_transaction_id_redundancia(self):
        pass

    def test_payment_post_api_with_empty_transaction_date(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '343d3g435435',
            transaction_id = '',
            transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_with_none_transaction_date(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = 'kjkljljk',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = None,
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_without_transaction_date_key(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '94820',
            transaction_id = 'AAAAAAAAAAAAA',
            #transaction_date = '28/4/2012',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_test_transaction_date_datatype(self):
        pass

    def test_payment_post_api_with_empty_transaction_medium(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '8789',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '',
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        res.status_code == 400

    def test_payment_post_api_with_none_transaction_medium(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '99452',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = None,
            transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_without_transaction_medium_key(self):
        data = dict(
            user_id = '834mhdc8v34lnvalj',
            invoice_number = '94820',
            transaction_id = 'AAAAAAAAAAAAA',
            transaction_date = '28/4/2012',
            #transaction_medium = 'MBirr' 
        )
        # calling apis endpoint
        res = self.app.post('/api/v1/payments', json=data)
        # asserting status code
        assert res.status_code == 400

    def test_payment_post_api_test_transaction_date_datatype(self):
        pass

    def test_proper_404_for_payment_api(self):
        # calling a non existing endpoint
        res = self.app.get('/api/v1/payments/dwdwqqwdwqd')
        # yeah it's not there
        assert res.status_code == 404
        # but we still get a nice JSON body
        body = json.loads(str(res.data, 'utf8'))
        assert body['code'] == 404

    #def test_raise(self):
        # this won't raise a Python exception but return a 500
     #   res = self.app.get('/api/v1/payments')
      #  body = json.loads(str(res.data, 'utf8'))
       # self.assertEqual(body['code'], 500)

    def test_payment_get_api_by_id_for_proper_invalid_id_response(self):
        # calling apis endpoint
        payments = self.app.get('/api/v1/payments/88')
        body = json.loads(str(payments.data, 'utf8'))
        # asserting status code
        assert payments.status_code == 400
        #(body['message']['description'], 'Resource ID is not a valid monogdb ObjectId')

    def test_payment_get_api_by_id(self):
        # calling apis endpoint
        payments = self.app.get('/api/v1/payments')

    def test_payment_get_api_by_id_for_no_content_found_response(self):
        # calling apis endpoint
        payments = self.app.get('/api/v1/payments')

        