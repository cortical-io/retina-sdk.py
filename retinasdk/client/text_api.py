"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
from retinasdk.model import fingerprint
from retinasdk.model import language_rest
from retinasdk.model import text


class TextApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient


    def getRepresentationForText(self, retina_name, body, ):
        """Get a retina representation of a text
        Args:
            retina_name, str: The retina name (required)
            body, str: The text to be evaluated (required)
            Returns: Array[Fingerprint]
        """

        resourcePath = '/text'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [fingerprint.Fingerprint(**r) for r in response.json()]

        

    def getKeywordsForText(self, retina_name, body, ):
        """Get a list of keywords from the text
        Args:
            retina_name, str: The retina name (required)
            body, str: The text to be evaluated (required)
            Returns: Array[str]
        """

        resourcePath = '/text/keywords'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return response.json()

        

    def getTokensForText(self, retina_name, body, POStags=None):
        """Get tokenized input text
        Args:
            retina_name, str: The retina name (required)
            body, str: The text to be tokenized (required)
            POStags, str: Specify desired POS types (optional)
            Returns: Array[str]
        """

        resourcePath = '/text/tokenize'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['POStags'] = POStags
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return response.json()

        

    def getSlicesForText(self, retina_name, body, get_fingerprint=None, start_index=0, max_results=10):
        """Get a list of slices of the text
        Args:
            retina_name, str: The retina name (required)
            body, str: The text to be evaluated (required)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            start_index, int: The start-index for pagination (optional) (optional)
            max_results, int: Max results per page (optional) (optional)
            Returns: Array[Text]
        """

        resourcePath = '/text/slices'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['start_index'] = start_index
        queryParams['max_results'] = max_results
        queryParams['get_fingerprint'] = get_fingerprint
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [text.Text(**r) for r in response.json()]

        

    def getRepresentationsForBulkText(self, retina_name, body, sparsity=1.0):
        """Bulk get Fingerprint for text.
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: Array[Fingerprint]
        """

        resourcePath = '/text/bulk'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['sparsity'] = sparsity
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [fingerprint.Fingerprint(**r) for r in response.json()]


    def getLanguage(self, body, ):
        """Detect the language of a text
        Args:
            body, str: Your input text (UTF-8) (required)
            Returns: LanguageRest
        """

        resourcePath = '/text/detect_language'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return language_rest.LanguageRest(**response.json())

