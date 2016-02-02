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

from retinasdk.full_client import FullClient
from tests.integration import configuration as conf


inputJSON = '{ "term" : "apple" }'
inputJSONarray = '[ { "term" : "apple" }, { "term" : "banana" } ]'
inputJSONarray3 = '[ { "term" : "apple" }, { "term" : "banana" }, { "term" : "fruit" } ]'

class TestClientImageApi(unittest.TestCase):
    """INFO:
    'base64/png' image data can be written to disk like this (python2.7):

    with open("imageToSave.png", "wb") as f:
        f.write(imageData.decode('base64'))
    """

    def setUp(self):
        self.client = FullClient(apiKey=conf.API_KEY, apiServer=conf.BASE_PATH, retinaName=conf.RETINA_NAME)

    def testImage(self):
        imageData = self.client.getImage(inputJSON)
        self.assertNotEqual(imageData, None)
        self.assertGreater(len(imageData), 1000)

    def testCompare(self):
        imageData = self.client.compareImage(inputJSONarray)
        self.assertNotEqual(imageData, None)
        self.assertGreater(len(imageData), 1000)

    def testBulk(self):
        images = self.client.getImages(inputJSONarray3, getFingerprint=True)
        self.assertEqual(len(images), 3)
        for image in images:
            self.assertNotEqual(image, None)
            self.assertNotEqual(image.image_data, None)
            self.assertGreater(len(image.image_data), 1000)
            self.assertGreater(len(image.fingerprint.positions), 50)

if __name__ == "__main__":
    unittest.main()
