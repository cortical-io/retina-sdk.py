"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
from retinasdk.model import retina


class RetinasApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient


    def getRetinas(self, retina_name=None):
        """Information about retinas
        Args:
            retina_name, str: The retina name (optional) (optional)
            Returns: Array[Retina]
        """

        resourcePath = '/retinas'
        method = 'GET'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [retina.Retina(**r) for r in response.json()]



