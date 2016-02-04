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
import unittest

from retinasdk.client.exceptions import CorticalioException
from retinasdk.full_client import FullClient
from tests.integration import configuration as conf


inputJSONarray =  json.dumps([{ "term": "apple" }, { "text": "banana is a kind of fruit" }])
bulkJSONarray = json.dumps([ [{"term": "jaguar" }, {"term": "car" }], [{ "term": "jaguar" }, {"term" : "cat"}] ])
oneTermInputJSONarray = json.dumps([{"term": "apple"}])
syntaxErrorJSONarray = json.dumps([{"invalid_key": "apple" }, {"term": "banana"}])

class TestClientCompareApi(unittest.TestCase):


    def setUp(self):
        self.client = FullClient(apiKey=conf.API_KEY, apiServer=conf.BASE_PATH, retinaName=conf.RETINA_NAME)

    def testCompare(self):
        resultMetric = self.client.compare(inputJSONarray)
        self.assertGreater(resultMetric.cosineSimilarity, 0.1)
        self.assertGreater(resultMetric.euclideanDistance, 0.1)
        self.assertGreater(resultMetric.jaccardDistance, 0.1)
        self.assertGreater(resultMetric.weightedScoring, 0.1)
        self.assertGreater(resultMetric.sizeRight, 10)
        self.assertGreater(resultMetric.sizeLeft, 10)
        self.assertGreater(resultMetric.overlappingLeftRight, 0.1)
        self.assertGreater(resultMetric.overlappingAll, 10)
        self.assertGreater(resultMetric.overlappingRightLeft, 0.1)

    def testCompareBulk(self):
        resultMetricList = self.client.compareBulk(bulkJSONarray)
        self.assertEqual(len(resultMetricList), 2)
        for resultMetric in resultMetricList:
            self.assertGreater(resultMetric.cosineSimilarity, 0.1)
            self.assertGreater(resultMetric.euclideanDistance, 0.1)
            self.assertGreater(resultMetric.jaccardDistance, 0.1)
            self.assertGreater(resultMetric.weightedScoring, 0.1)
            self.assertGreater(resultMetric.sizeRight, 10)
            self.assertGreater(resultMetric.sizeLeft, 10)
            self.assertGreater(resultMetric.overlappingLeftRight, 0.1)
            self.assertGreater(resultMetric.overlappingAll, 10)
            self.assertGreater(resultMetric.overlappingRightLeft, 0.1)
        

    def testException(self):
        # testing using only one input element in the array
        expectedException = False
        try:
            self.client.compare(oneTermInputJSONarray)
        except CorticalioException:
            expectedException = True
        self.assertTrue(expectedException)
        
        # testing JSON parse exception in the input
        expectedException = False
        try:
            self.client.compare(syntaxErrorJSONarray)
        except CorticalioException:
            expectedException = True
        self.assertTrue(expectedException)


if __name__ == "__main__":
    unittest.main()


