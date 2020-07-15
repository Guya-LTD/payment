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

from payment.main.repository.payment import Payment as PaymentRepository, db

class TestPaymentRepository(unittest.TestCase):
    def test_payment_creation(self):
        payment = PaymentRepository(
           user_id = '555AAAAA',
           order_tracking_id = '8899',
           transaction_id = 'AAAAAAAAAAAAA',
           transaction_date = '28/4/2012',
           transaction_medium = 'MBirr' 
        )

        payment.save()
        print(payment.id)
        self.assertNotEqual(payment.id, None)

    def test_payment_creation_using_user_id(self):
        with self.assertRaises(db.ValidationError): PaymentRepository(user_id = 55).save()




