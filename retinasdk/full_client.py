"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""

import json

from retinasdk.client.base_client import BaseClient
from retinasdk.client.classify_api import ClassifyApi
from retinasdk.client.compare_api import CompareApi
from retinasdk.client.expressions_api import ExpressionsApi
from retinasdk.client.image_api import ImageApi
from retinasdk.client.retinas_api import RetinasApi
from retinasdk.client.terms_api import TermsApi
from retinasdk.client.text_api import TextApi


class FullClient(object):
    """Client for accessing all REST endpoints on Cortical.io's Retina API"""

    def __init__(self, apiKey, apiServer="http://api.cortical.io/rest", retinaName="en_associative"):
        self._retina = retinaName
        # initialization of helper objects
        self._baseClient = BaseClient(apiKey, apiServer)
        self._retinas = RetinasApi(self._baseClient)
        self._terms = TermsApi(self._baseClient)
        self._text = TextApi(self._baseClient)
        self._expressions = ExpressionsApi(self._baseClient)
        self._compare = CompareApi(self._baseClient)
        self._image = ImageApi(self._baseClient)
        self._classify = ClassifyApi(self._baseClient)

    def getRetinas(self, retinaName=None):
        """Information about retinas
        Args:
            retinaName, str: The retina name (optional)
        Returns:
            list of Retina
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._retinas.getRetinas(retina_name=retinaName)

    def getTerms(self, term=None, getFingerprint=None, startIndex=0, maxResults=10):
        """Get term objects
        Args:
            term, str: A term in the retina (optional)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            startIndex, int: The start-index for pagination (optional)
            maxResults, int: Max results per page (optional)
        Returns: 
            list of Term
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._terms.getTerm(self._retina, term, getFingerprint, startIndex, maxResults)

    def getContextsForTerm(self, term, getFingerprint=None, startIndex=0, maxResults=5):
        """Get the contexts for a given term
        Args:
            term, str: A term in the retina (required)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            startIndex, int: The start-index for pagination (optional)
            maxResults, int: Max results per page (optional)
        Returns:
            list of Context
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._terms.getContextsForTerm(self._retina, term, getFingerprint, startIndex, maxResults)

    def getSimilarTermsForTerm(self, term, contextId=None, posType=None, getFingerprint=None, startIndex=0, maxResults=10):
        """Get the similar terms of a given term
        Args:
            term, str: A term in the retina (required)
            contextId, int: The identifier of a context (optional)
            posType, str: Part of speech (optional)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            startIndex, int: The start-index for pagination (optional)
            maxResults, int: Max results per page (optional)
        Returns:
            list of Term
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._terms.getSimilarTerms(self._retina, term, contextId, posType, getFingerprint, startIndex, maxResults)


    def getFingerprintForText(self, body):
        """Get a retina representation of a text
        Args:
            body, str: The text to be evaluated (required)
        Returns:
            Fingerprint
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._text.getRepresentationForText(self._retina, body)[0]

    def getKeywordsForText(self, body):
        """Get a list of keywords from the text
        Args:
            body, str: The text to be evaluated (required)
        Returns:
            list of str
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._text.getKeywordsForText(self._retina, body)

    def getTokensForText(self, body, POStags=None):
        """Get tokenized input text
        Args:
            body, str: The text to be tokenized (required)
            POStags, str: Specify desired POS types (optional)
        Returns:
            list of str
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._text.getTokensForText(self._retina, body, POStags)


    def getSlicesForText(self, body, getFingerprint=None, startIndex=0, maxResults=10):
        """Get a list of slices of the text
        Args:
            body, str: The text to be evaluated (required)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            startIndex, int: The start-index for pagination (optional)
            maxResults, int: Max results per page (optional)
        Returns:
            list of Text
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._text.getSlicesForText(self._retina, body, getFingerprint, startIndex, maxResults)


    def getFingerprintsForTexts(self, strings, sparsity=1.0):
        """Bulk get Fingerprint for text.
        Args:
            strings, list(str): A list of texts to be evaluated (required)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            list of Fingerprint
        Raises:
            CorticalioException: if the request was not successful
        """
        body = [{"text": s} for s in strings]
        return self._text.getRepresentationsForBulkText(self._retina, json.dumps(body), sparsity)


    def getLanguageForText(self, body):
        """Detect the language of a text
        Args:
            body, str: Your input text (UTF-8) (required)
        Returns:
            LanguageRest
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._text.getLanguage(body)


    def getFingerprintForExpression(self, body, sparsity=1.0):
        """Resolve an expression
        Args:
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            Fingerprint
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._expressions.resolveExpression(self._retina, body, sparsity)


    def getContextsForExpression(self, body, getFingerprint=None, startIndex=0, maxResults=5, sparsity=1.0):
        """Get semantic contexts for the input expression
        Args:
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            startIndex, int: The start-index for pagination (optional)
            maxResults, int: Max results per page (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            list of Context
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._expressions.getContextsForExpression(self._retina, body, getFingerprint, startIndex, maxResults, sparsity)
        

    def getSimilarTermsForExpression(self, body, contextId=None, posType=None, getFingerprint=None, startIndex=0, maxResults=10, sparsity=1.0):
        """Get similar terms for the contexts of an expression
        Args:
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            contextId, int: The identifier of a context (optional)
            posType, str: Part of speech (optional)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            startIndex, int: The start-index for pagination (optional)
            maxResults, int: Max results per page (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            list of Term
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._expressions.getSimilarTermsForExpressionContext(self._retina, body, contextId, posType, getFingerprint, startIndex, maxResults, sparsity)

    def getFingerprintsForExpressions(self, body, sparsity=1.0):
        """Bulk resolution of expressions
        Args:
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            list of Fingerprint
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._expressions.resolveBulkExpression(self._retina, body, sparsity)

    def getContextsForExpressions(self, body, getFingerprint=None, startIndex=0, maxResults=5, sparsity=1.0):
        """Bulk get contexts for input expressions
        Args:
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            startIndex, int: The start-index for pagination (optional)
            maxResults, int: Max results per page (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            list of Context
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._expressions.getContextsForBulkExpression(self._retina, body, getFingerprint, startIndex, maxResults, sparsity)


    def getSimilarTermsForExpressions(self, body, contextId=None, posType=None, getFingerprint=None, startIndex=0, maxResults=10, sparsity=1.0):
        """Bulk get similar terms for input expressions
        Args:
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            contextId, int: The identifier of a context (optional)
            posType, str: Part of speech (optional)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            startIndex, int: The start-index for pagination (optional)
            maxResults, int: Max results per page (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            list of Term
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._expressions.getSimilarTermsForBulkExpressionContext(self._retina, body, contextId, posType, getFingerprint, startIndex, maxResults, sparsity)


    def compare(self, body):
        """Compare elements
        Args:
            body, ExpressionOperation: The JSON encoded comparison array to be evaluated (required)
        Returns:
            Metric
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._compare.compare(self._retina, body)


    def compareBulk(self, body):
        """Bulk compare
        Args:
            body, ExpressionOperation: Bulk comparison of elements 2 by 2 (required)
        Returns:
            list of Metric
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._compare.compareBulk(self._retina, body)

    def getImage(self, body, imageScalar=2, plotShape="circle", imageEncoding="base64/png", sparsity=1.0):
        """Get images for expressions
        Args:
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            imageScalar, int: The scale of the image (optional)
            plotShape, str: The image shape (optional)
            imageEncoding, str: The encoding of the returned image (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            str with the raw byte data of the image
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._image.getImageForExpression(self._retina, body, imageScalar, plotShape, imageEncoding, sparsity)


    def compareImage(self, body, plotShape="circle", imageScalar=2, imageEncoding="base64/png"):
        """Get an overlay image for two expressions
        Args:
            body, ExpressionOperation: The JSON encoded comparison array to be evaluated (required)
            plotShape, str: The image shape (optional)
            imageScalar, int: The scale of the image (optional)
            imageEncoding, str: The encoding of the returned image (optional)
        Returns:
            str with the raw byte data of the image
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._image.getOverlayImage(self._retina, body, plotShape, imageScalar, imageEncoding)


    def getImages(self, body, getFingerprint=None, imageScalar=2, plotShape="circle", sparsity=1.0):
        """Bulk get images for expressions
        Args:
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            getFingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            imageScalar, int: The scale of the image (optional)
            plotShape, str: The image shape (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
        Returns:
            list of Image
        Raises:
            CorticalioException: if the request was not successful
        """
        return self._image.getImageForBulkExpressions(self._retina, body, getFingerprint, imageScalar, plotShape, sparsity)


    def createCategoryFilter(self, filterName, positiveExamples, negativeExamples=[]):
        """Get a classifier filter (fingerprint) for positive and negative text samples
        Args:
            filterName, str: A unique name for the filter. (required)
            positiveExamples, list(str): The list of positive example texts. (required)
            negativeExamples, list(str): The list of negative example texts. (optional)
        Returns:
            CategoryFilter
        Raises:
            CorticalioException: if the request was not successful
        """
        samples = {"positiveExamples": [{"text": s} for s in positiveExamples],
                   "negativeExamples": [{"text": s} for s in negativeExamples]}
        body = json.dumps(samples)
        return self._classify.createCategoryFilter(self._retina, filterName, body)

