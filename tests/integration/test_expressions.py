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
import os
import unittest

from retinasdk.full_client import FullClient
from tests.integration import configuration as conf


oneTermInputJSON = json.dumps({"term" :"apple" })
simpleExpression = json.dumps({"or": [ {"term": "apple"}, {"term": "fruit" } ] })
bulkInput = os.path.join(os.path.dirname(__file__), 'bulkInput.json')

class TestClientExpreissions(unittest.TestCase):
    

    def setUp(self):
        self.client = FullClient(apiKey=conf.API_KEY, apiServer=conf.BASE_PATH, retinaName=conf.RETINA_NAME)
        self.jsonBulkExpression = None
        # path relative to current working dir
        with open(bulkInput, "r") as f:
            self.jsonBulkExpression = "".join(f.readlines())
    
    def testExpressions(self):
        fp = self.client.getFingerprintForExpression(oneTermInputJSON, sparsity=0.5)
        self.assertGreater(len(fp.positions), 100)

    def testContexts(self):
        contexts = self.client.getContextsForExpression(simpleExpression, getFingerprint=True, startIndex=0, maxResults=3, sparsity=1.0)
        self.assertTrue(contexts != None)
        self.assertEqual(3, len(contexts))
        c0 = contexts[0]
        self.assertGreater(len(c0.fingerprint.positions), 100)
        self.assertTrue(conf.isString(c0.context_label))
        self.assertTrue(c0.context_id == 0)

    def testSimilarTerms(self):
        terms = self.client.getSimilarTermsForExpression(simpleExpression, contextId=None, posType="NOUN", getFingerprint=True, startIndex=0, maxResults=8, sparsity=1.0)
        self.assertTrue(terms != None)
        self.assertEqual(8, len(terms))
        for term in terms:
            self.assertGreater(len(term.fingerprint.positions), 100)
            self.assertTrue(term != None)
            self.assertTrue("NOUN" in term.pos_types)

    def testExpressionBulk(self):
        fps = self.client.getFingerprintsForExpressions(self.jsonBulkExpression)
        self.assertEqual(6, len(fps))
        for fp in fps:
            self.assertGreater(len(fp.positions), 50)

    def testExpressionContextsBulk(self):
        contextsList = self.client.getContextsForExpressions(self.jsonBulkExpression, getFingerprint=True, startIndex=0, maxResults=3)
        
        self.assertEqual(len(contextsList), 6)
        for contextList in contextsList:
            for i, context in enumerate(contextList):
                self.assertGreater(len(context.fingerprint.positions), 50)
                self.assertTrue(conf.isString(context.context_label))
                self.assertTrue(context.context_id == i)

    def testExpressionSimilarTermsBulk(self):
        termsLists = self.client.getSimilarTermsForExpressions(self.jsonBulkExpression, getFingerprint=True, maxResults=7)
        self.assertTrue(len(termsLists) == 6)
        for termList in termsLists:
            self.assertTrue(len(termList) == 7)
            self.assertGreater(len(termList[0].fingerprint.positions), 100)

if __name__ == "__main__":
    unittest.main()

