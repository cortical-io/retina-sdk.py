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


positiveExamples = ["Shoe with a lining to help keep your feet dry and comfortable on wet terrain." ,
                    "running shoes providing protective cushioning."]
negativeExamples = ["The most comfortable socks for your feet.",
                    "6 feet USB cable basic white"]


class TestClassifyApi(unittest.TestCase):


    def setUp(self):
        self.client = FullClient(apiKey=conf.API_KEY, apiServer=conf.BASE_PATH, retinaName=conf.RETINA_NAME)

    def testCreateCategoryFilter(self):
        filterName = "filter1"
        filter1 = self.client.createCategoryFilter(filterName, positiveExamples, negativeExamples)
        self.assertGreater(len(filter1.positions), 50)
        self.assertEqual(filter1.categoryName, filterName)
        
    def testErrors(self):
        expectedException = False
        try:
            self.client.createCategoryFilter(None, positiveExamples, negativeExamples)
        except CorticalioException:
            expectedException = True
        self.assertTrue(expectedException)
        
        expectedException = False
        try:
            self.client.createCategoryFilter("filterName", [], negativeExamples)
        except CorticalioException:
            expectedException = True
        self.assertTrue(expectedException)


if __name__ == "__main__":
    unittest.main()
