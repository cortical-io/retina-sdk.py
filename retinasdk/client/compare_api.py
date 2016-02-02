"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
from retinasdk.model import metric


class CompareApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient


    def compare(self, retina_name, body, ):
        """Compare elements
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded comparison array to be evaluated (required)
            Returns: Metric
        """

        resourcePath = '/compare'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return metric.Metric(**response.json())


    def compareBulk(self, retina_name, body):
        """Bulk compare
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: Bulk comparison of elements 2 by 2 (required)
            Returns: Array[Metric]
        """

        resourcePath = '/compare/bulk'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [metric.Metric(**r) for r in response.json()]

    