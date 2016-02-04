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


class TestClientRetinasApi(unittest.TestCase):

    def setUp(self):
        self.client = FullClient(apiKey=conf.API_KEY, apiServer=conf.BASE_PATH, retinaName=conf.RETINA_NAME)

    def testRetinas(self):
        retinas = self.client.getRetinas()
        self.assertNotEqual(retinas, None)
        self.assertNotEqual(retinas[0], None)
        self.assertNotEqual(retinas[1], None)
        self.assertTrue("en_synonymous" == retinas[0].retinaName or "en_associative" == retinas[0].retinaName)
        self.assertTrue("en_synonymous" == retinas[1].retinaName or "en_associative" == retinas[1].retinaName)
        self.assertGreater(retinas[0].numberOfTermsInRetina, 50000)

    def testException(self):
        exceptionOccurred = False
        try:
            self.client.getRetinas("nonexisting_retina")
        except CorticalioException:
            exceptionOccurred = True
        self.assertTrue(exceptionOccurred)

if __name__ == "__main__":
    unittest.main()
