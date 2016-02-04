"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
import requests

import retinasdk
from retinasdk.client.exceptions import CorticalioException


class BaseClient:

    def __init__(self, apiKey=None, apiServer=None):
        if apiKey == None:
            raise CorticalioException('You must pass an apiKey when instantiating the API Client. Please visit http://www.cortical.io/')
        self.apiKey = apiKey
        self.apiServer = apiServer
        self.cookie = None
    

    def _callAPI(self, resourcePath, method, queryParams, postData, headers={}):

        url = self.apiServer + resourcePath
        headers['api-key'] = self.apiKey
        headers['api-client'] = "py_" + retinasdk.__version__
        response = None
        
        if method == 'GET':
            response = requests.get(url, params=queryParams, headers=headers)

        elif method == 'POST':
            response = requests.post(url, params=queryParams, headers=headers, data=postData)

        else:
            raise CorticalioException('Method ' + method + ' is not recognized.')

        if response.status_code != 200:
            raise CorticalioException("Response %s: %s" % (str(response.status_code), str(response.content)))
        return response
        
