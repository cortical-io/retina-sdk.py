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
from retinasdk.model.term import Term


class TermsApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient


    def getTerm(self, retina_name, term=None, get_fingerprint=None, start_index=0, max_results=10):
        """Get term objects
        Args:
            retina_name, str: The retina name (required)
            term, str: A term in the retina (optional) (optional)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            start_index, int: The start-index for pagination (optional) (optional)
            max_results, int: Max results per page (optional) (optional)
            Returns: Array[Term]
        """

        resourcePath = '/terms'
        method = 'GET'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['term'] = term
        queryParams['start_index'] = start_index
        queryParams['max_results'] = max_results
        queryParams['get_fingerprint'] = get_fingerprint
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [Term(**r) for r in response.json()]

        

    def getContextsForTerm(self, retina_name, term, get_fingerprint=None, start_index=0, max_results=5):
        """Get the contexts for a given term
        Args:
            retina_name, str: The retina name (required)
            term, str: A term in the retina (required)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            start_index, int: The start-index for pagination (optional) (optional)
            max_results, int: Max results per page (optional) (optional)
            Returns: Array[Context]
        """

        resourcePath = '/terms/contexts'
        method = 'GET'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['term'] = term
        queryParams['start_index'] = start_index
        queryParams['max_results'] = max_results
        queryParams['get_fingerprint'] = get_fingerprint
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [context.Context(**r) for r in response.json()]



    def getSimilarTerms(self, retina_name, term, context_id=None, pos_type=None, get_fingerprint=None, start_index=0, max_results=10):
        """Get the similar terms of a given term
        Args:
            retina_name, str: The retina name (required)
            term, str: A term in the retina (required)
            context_id, int: The identifier of a context (optional) (optional)
            pos_type, str: Part of speech (optional) (optional)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            start_index, int: The start-index for pagination (optional) (optional)
            max_results, int: Max results per page (optional) (optional)
            Returns: Array[Term]
        """

        resourcePath = '/terms/similar_terms'
        method = 'GET'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['term'] = term
        queryParams['context_id'] = context_id
        queryParams['start_index'] = start_index
        queryParams['max_results'] = max_results
        queryParams['pos_type'] = pos_type
        queryParams['get_fingerprint'] = get_fingerprint
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [Term(**r) for r in response.json()]



