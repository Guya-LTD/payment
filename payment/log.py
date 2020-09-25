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


"""Logging handler."""

import os
import sys
import logging
import logstash


# const vars
__extra__ = {
    'app_name': 'Payment Service',      
    'environment': os.getenv('ENV'),  
    'container_host': os.getenv('HOST'),
    'port': os.getenv('PORT'),
    'sys': {
        'lang': 'python',
        'version': str(sys.version),
        'version_info': repr(sys.version_info)
    }
}


# Logger with app name i.e xtrack.main
logger = logging.getLogger(__name__)


# logger handler
logger.addHandler(
    logstash.LogstashHandler(
        os.getenv('LOGGING_HOST'),
        os.getenv('LOGGING_PORT'), 
        version=1)
    )