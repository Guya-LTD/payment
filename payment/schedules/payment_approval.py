# -*- coding: utf-8 -*-

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


This module contains the factory function 'create_app' that is
responsible for initializing the application according
to a previous configuration.
"""
import requests

from payment.endpoint import Endpoint
from payment.repository.payment import Payment
from payment.repository.transaction import Transaction

#from .database import db

def checkAndApprove():
    print("Payment approval starting...")
    ## Endpoint
    endpoint = Endpoint()
    ## Find matching payment transaction
    payments = Payment.objects(status = Payment.PENDING)
    ## Loop through payments
    for payment in payments:
        try:
            transaction =  Transaction.objects.get(
                transaction_id = payment.transaction_id,
                transaction_date = payment.transaction_date,
                transaction_medium = payment.transaction_medium
            )
            ## Check if transaction is correct
            if transaction.id:
                ## Transaction and payment matched
                ## TODO: Retrive invoice using `payment.invoice_id` from Order Service
                ##       and send receipt email
                invoice_request = requests.get(
                    #endpoint.order('invoices/' + str(payment.invoice_id))
                    endpoint.mocking_server('invoices/1')
                )
                ## Send receipt
                chipmunk_request = requests.post(
                    endpoint.chipmunk('emails/send/receipt'),
                    json = invoice_request.json()['data']
                )
                Payment.objects(id = payment.id).update(
                    status = Payment.COMPLETE,
                    email_status = Payment.SENT,
                    approval_method = Payment.AUTOMATIC
                )
        except Exception as ex:
            print(ex)
