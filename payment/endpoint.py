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
        - Branch Service
    * Description
        - Branch location and details service
"""


"""This module contains class whose instances will be used to
load the settings according to the running environment. """

import os
 
class Endpoint:
    def gatekeeper(self, name):
        return 'http://' + os.environ.get('GATEKEEPER_URL') + "/api/v1/" + name

    def order(self, name):
        return 'http://' + os.environ.get('ORDER_URL') + '/api/v1/' + name

    def chipmunk(self, name):
        return 'http://' + os.environ.get('CHIPMUNK_URL') + '/api/v1/' + name

    def mocking_server(self, name):
        return 'http://' + os.environ.get('MOCKING_SERVER_URL') + '/api/v1/' + name