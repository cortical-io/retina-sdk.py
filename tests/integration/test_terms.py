"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
import unittest

from retinasdk.client.exceptions import CorticalioException
from retinasdk.full_client import FullClient
from tests.integration import configuration as conf


class TestClientTermsApi(unittest.TestCase):
    
    def setUp(self):
        self.client = FullClient(apiKey=conf.API_KEY, apiServer=conf.BASE_PATH, retinaName=conf.RETINA_NAME)

    def testTerms(self):
        terms = self.client.getTerms(term="apple", getFingerprint=True, startIndex=0, maxResults=5)
        self.assertTrue(len(terms) == 1)
        self.assertTrue(terms[0].term == "apple")
        self.assertTrue("NOUN" in terms[0].pos_types)
        self.assertTrue(terms[0].df > 0.0001)
        self.assertGreater(len(terms[0].fingerprint.positions), 100)

        terms100 = self.client.getTerms("app*", startIndex=0, maxResults=100)
        self.assertEqual(len(terms100), 100)

    def testContexts(self):
        contexts = self.client.getContextsForTerm(term="apple", getFingerprint=True, startIndex=0, maxResults=3)
        self.assertTrue(contexts != None)
        self.assertEqual(3, len(contexts))
        c0 = contexts[0]
        self.assertGreater(len(c0.fingerprint.positions), 100)
        self.assertTrue(conf.isString(c0.context_label))
        self.assertTrue(c0.context_id == 0)

    def testSimilarTerms(self):
        terms = self.client.getSimilarTermsForTerm(term="apple", contextId=0, posType="NOUN", getFingerprint=True, startIndex=0, maxResults=8)
        self.assertTrue(terms != None)
        self.assertEqual(8, len(terms))
        t0 = terms[0]
        self.assertTrue(len(t0.fingerprint.positions) > 0)
        self.assertTrue(t0 != None)
        self.assertTrue("NOUN" in t0.pos_types)

    def testExceptionTerms(self):
        exceptionOccurred = False
        try:
            terms = self.client.getSimilarTermsForTerm(term="apple", posType="wrong")
        except CorticalioException:
            exceptionOccurred = True
        self.assertTrue(exceptionOccurred)
        
if __name__ == "__main__":
    unittest.main()
