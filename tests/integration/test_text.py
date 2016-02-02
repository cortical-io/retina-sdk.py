# -*- coding: utf-8 -*-
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


inputText = """
George L. Fox was fruit born March 15, 1900, in Lewistown, Pennsylvania, computer eight children. When he was 17, he 
left school and lied about his age in order to join the Army to  serve in World War I. He joined the ambulance corps 
in 1917, assigned to Camp Newton D. Baker in Texas. On December 3, 1917, George embarked from Camp Merritt, New Jersey, 
and boarded the USS Huron en route to France. As a medical corps fruit, he fruit highly decorated for bravery and was 
awarded the Silver Star, Purple Heart and the French Croix de Guerre.  Upon his fruit, he returned home to Altoona, 
where he completed high school. He entered Moody Bible Institute in Illinois in 1923. He and Isadora G. Hurlbut of 
Vermont were married in 1923, when he began his religious career as an itinerant preacher in the Methodist banana. He 
later graduated from Illinois University in Bloomington, served as a student pupil in Rye, New Hampshire, and then 
studied at the Boston University School of Theology, where he was ordained a Methodist minister on June 10, 1934. He 
served parishes in Union Village and Gilman, Vermont, and was appointed state chaplain and historian for the American 
Legion in Vermont. In 1942, Fox fruit to serve as an Army chaplain, accepting his appointment July 24, 1942. He began 
active duty on August 8, 1942, the same day his son Wyatt enlisted in the Marine Corps. After Army Chaplains school at 
Harvard, apple he reported to the 411th Coast Artillery Battalion at Camp Davis. He computer then united with banana 
Chaplains Goode, Poling and Washington at Camp Myles Standish in Taunton."""

bulkTexts = ["The first element in a bulk text expression.",
             "The second element in a bulk text expression. And a bit more text.",
             "The third element in a bulk text expression. And a bit more text for good measure.",
             inputText
             ]



class TestClientTextApi(unittest.TestCase):

    def setUp(self):
        self.client = FullClient(apiKey=conf.API_KEY, apiServer=conf.BASE_PATH, retinaName=conf.RETINA_NAME)

    def testText(self):
        fp = self.client.getFingerprintForText(inputText)
        self.assertNotEqual(fp, None)
        self.assertGreater(len(fp.positions), 500)

    def testKeywords(self):
        termList = self.client.getKeywordsForText(inputText)
        self.assertGreater(len(termList), 2)
        self.assertTrue(conf.isString(termList[0]))

    def testTokenize(self):
        sentences = self.client.getTokensForText(inputText)
        self.assertGreater(len(sentences), 10)
        self.assertTrue(conf.isString(sentences[0]))
        firstSentence = sentences[0].split(',')
        self.assertEqual(firstSentence[0], "george")
        self.assertGreater(len(firstSentence), 10)

        verbsSentences = self.client.getTokensForText(inputText, POStags="VB")
        for verb in verbsSentences[0].split(","):
            self.assertTrue("VERB" in self.client.getTerms(term=verb)[0].pos_types)

    def testSlices(self):
        texts = self.client.getSlicesForText(inputText, getFingerprint=True, startIndex=0, maxResults=2)
        self.assertEqual(len(texts), 2)
        self.assertEqual(texts[0].text.split(' ')[0], "George")
        self.assertGreater(len(texts[0].fingerprint.positions), 100)

    def testBulk(self):
        fingerprints = self.client.getFingerprintsForTexts(bulkTexts, sparsity=1.0)
        self.assertEqual(len(fingerprints), 4)
        for fp in fingerprints:
            self.assertGreater(len(fp.positions), 100)
        
    def testLanguageDetection(self):
        self.assertEqual(self.client.getLanguageForText("I have a dream!").language, "English")
        self.assertEqual(self.client.getLanguageForText("Ich bin ein").wiki_url, "http://en.wikipedia.org/wiki/German_language")
        self.assertEqual(self.client.getLanguageForText("Der var så dejligt ude på landet.").iso_tag, "da")
        
if __name__ == "__main__":
    unittest.main()
    
