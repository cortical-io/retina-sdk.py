"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
from retinasdk.model import context
from retinasdk.model import fingerprint
from retinasdk.model import term


class ExpressionsApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient


    def resolveExpression(self, retina_name, body, sparsity=1.0):
        """Resolve an expression
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON formatted encoded to be evaluated (required)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: Fingerprint
        """

        resourcePath = '/expressions'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['sparsity'] = sparsity
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return fingerprint.Fingerprint(**response.json())

        

    def getContextsForExpression(self, retina_name, body, get_fingerprint=None, start_index=0, max_results=5, sparsity=1.0):
        """Get semantic contexts for the input expression
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            start_index, int: The start-index for pagination (optional) (optional)
            max_results, int: Max results per page (optional) (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: Array[Context]
        """

        resourcePath = '/expressions/contexts'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['start_index'] = start_index
        queryParams['max_results'] = max_results
        queryParams['sparsity'] = sparsity
        queryParams['get_fingerprint'] = get_fingerprint
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [context.Context(**r) for r in response.json()]

        

    def getSimilarTermsForExpressionContext(self, retina_name, body, context_id=None, pos_type=None, get_fingerprint=None, start_index=0, max_results=10, sparsity=1.0):
        """Get similar terms for the contexts of an expression
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            context_id, int: The identifier of a context (optional) (optional)
            pos_type, str: Part of speech (optional) (optional)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            start_index, int: The start-index for pagination (optional) (optional)
            max_results, int: Max results per page (optional) (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: Array[Term]
        """

        resourcePath = '/expressions/similar_terms'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['context_id'] = context_id
        queryParams['start_index'] = start_index
        queryParams['max_results'] = max_results
        queryParams['pos_type'] = pos_type
        queryParams['sparsity'] = sparsity
        queryParams['get_fingerprint'] = get_fingerprint
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [term.Term(**r) for r in response.json()]

        

    def resolveBulkExpression(self, retina_name, body, sparsity=1.0):
        """Bulk resolution of expressions
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: Array[Fingerprint]
        """

        resourcePath = '/expressions/bulk'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['sparsity'] = sparsity
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [fingerprint.Fingerprint(**r) for r in response.json()]

        

    def getContextsForBulkExpression(self, retina_name, body, get_fingerprint=None, start_index=0, max_results=5, sparsity=1.0):
        """Bulk get contexts for input expressions
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            start_index, int: The start-index for pagination (optional) (optional)
            max_results, int: Max results per page (optional) (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: Array[Context]
        """

        resourcePath = '/expressions/contexts/bulk'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['start_index'] = start_index
        queryParams['max_results'] = max_results
        queryParams['sparsity'] = sparsity
        queryParams['get_fingerprint'] = get_fingerprint
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [[context.Context(**c) for c in r] for r in response.json()]

        

    def getSimilarTermsForBulkExpressionContext(self, retina_name, body, context_id=None, pos_type=None, get_fingerprint=None, start_index=0, max_results=10, sparsity=1.0):
        """Bulk get similar terms for input expressions
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            context_id, int: The identifier of a context (optional) (optional)
            pos_type, str: Part of speech (optional) (optional)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            start_index, int: The start-index for pagination (optional) (optional)
            max_results, int: Max results per page (optional) (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: Array[Term]
        """

        resourcePath = '/expressions/similar_terms/bulk'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['context_id'] = context_id
        queryParams['start_index'] = start_index
        queryParams['max_results'] = max_results
        queryParams['pos_type'] = pos_type
        queryParams['sparsity'] = sparsity
        queryParams['get_fingerprint'] = get_fingerprint
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [[term.Term(**t) for t in r] for r in response.json()]


        
