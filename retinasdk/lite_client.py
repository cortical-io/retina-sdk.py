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

from retinasdk.client.exceptions import CorticalioException
from retinasdk.full_client import FullClient


class LiteClient(object):
    """Minimalistic client for accessing core features of Cortical.io's Retina API in a simple way."""
    
    def __init__(self, apiKey):
        self._fullClient = FullClient(apiKey, apiServer="http://api.cortical.io/rest", retinaName="en_associative")

    def _createDictionary(self, textOrFingerprint):
        if type(textOrFingerprint) == str:
            return {"text": textOrFingerprint}
        elif type(textOrFingerprint) == list:
            return {"positions": textOrFingerprint}
        else:
            raise CorticalioException("Invalid argument, cannot create input from: '%s'" % (str(textOrFingerprint)))

    def getSimilarTerms(self, textOrFingerprint):
        """Get the similar terms for a given text or fingerprint
        Args:
            textOrFingerprint, str OR list of integers
        Returns:
            list of str: the 20 most similar terms
        Raises:
            CorticalioException: if the request was not successful
        """
        expression = self._createDictionary(textOrFingerprint)
        terms = self._fullClient.getSimilarTermsForExpression(json.dumps(expression), maxResults=20)
        return [t.term for t in terms]

    def getKeywords(self, text):
        """Get a list of keywords from the text
        Args:
            text, str: The input document
        Returns:
            list of str
        Raises:
            CorticalioException: if the request was not successful
        """
        terms = self._fullClient.getKeywordsForText(text)
        return terms

    def getFingerprint(self, text):
        """Get the semantic fingerprint of the input text.
        Args:
            text, str: The text to be evaluated
        Returns:
            list of str: the positions of the semantic fingerprint
        Raises:
            CorticalioException: if the request was not successful
        """
        fp = self._fullClient.getFingerprintForText(text)
        return fp.positions

    def compare(self, textOrFingerprint1, textOrFingerprint2):
        """Returns the semantic similarity of texts or fingerprints. Each argument can be eiter a text or a fingerprint.
        Args:
            textOrFingerprint1, str OR list of integers
            textOrFingerprint2, str OR list of integers
        Returns:
            float: the semantic similarity in the range [0;1]
        Raises:
            CorticalioException: if the request was not successful
        """
        compareList = [self._createDictionary(textOrFingerprint1), self._createDictionary(textOrFingerprint2)]
        metric = self._fullClient.compare(json.dumps(compareList))
        return metric.cosineSimilarity

    def createCategoryFilter(self, positiveExamples):
        """Creates a filter fingerprint.
        Args:
            positiveExamples, list(str): The list of positive example texts.
        Returns:
            list of int: the positions representing the filter representing the texts
        Raises:
            CorticalioException: if the request was not successful
        """
        categoryFilter = self._fullClient.createCategoryFilter("CategoryFilter", positiveExamples)
        return categoryFilter.positions
