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

from retinasdk.lite_client import LiteClient
from tests.integration import configuration as conf


inputText = """
Martin Luther King, Jr. (January 15, 1929 - April 4, 1968) was an American Baptist minister, activist, humanitarian, 
and leader in the African-American Civil Rights Movement. He is best known for his role in the advancement of civil 
rights using nonviolent civil disobedience based on his Christian beliefs.

King became a civil rights activist early in his career. He led the 1955 Montgomery Bus Boycott and helped found the 
Southern Christian Leadership Conference (SCLC) in 1957, serving as its first president. With the SCLC, King led an 
unsuccessful 1962 struggle against segregation in Albany, Georgia (the Albany Movement), and helped organize the 1963 
nonviolent protests in Birmingham, Alabama. King also helped to organize the 1963 March on Washington, where he 
delivered his famous 'I Have a Dream' speech. There, he established his reputation as one of the greatest orators in 
American history."""
from retinasdk.client.exceptions import CorticalioException

class Test(unittest.TestCase):


    def setUp(self):
        self.client = LiteClient(conf.API_KEY)

    def testGetSimilarTerms(self):
        terms = self.client.getSimilarTerms(inputText)
        self.assertEqual(20, len(terms))
        for term in terms:
            self.assertGreater(len(term), 0)
            self.assertTrue(conf.isString(term))

        terms = self.client.getSimilarTerms(list(range(500)))
        self.assertEqual(20, len(terms))
        for term in terms:
            self.assertGreater(len(term), 0)
            self.assertTrue(conf.isString(term))

        try:
            self.client.getSimilarTerms(45)
            self.fail("An exception should have been thrown")
        except CorticalioException:
            pass

        try:
            self.client.getSimilarTerms([])
            self.fail("An exception should have been thrown")
        except CorticalioException:
            pass

    def testGetKeywords(self):
        terms = self.client.getKeywords(inputText)
        self.assertGreater(len(terms), 2)
        for term in terms:
            self.assertGreater(len(term), 0)
            self.assertTrue(conf.isString(term))

    def testGetFingerprint(self):
        self.assertGreater(len(self.client.getFingerprint("apple")), 100)
        self.assertGreater(len(self.client.getFingerprint("which was the son of")), 100)

        try:
            self.client.getFingerprint("")
            self.fail("An exception should have been thrown")
        except CorticalioException:
            pass
    
    def testCompare(self):
        appleString = "apple"
        bananaString = "banana is a kind of fruit"
        appleFingerprint = self.client.getFingerprint(appleString)
        bananaFingerprint = self.client.getFingerprint(bananaString)
        fingerprint = list(range(500))
        
        self.assertGreater(self.client.compare(appleString, bananaString), 0.1)
        self.assertGreater(self.client.compare(appleString, bananaFingerprint), 0.1)
        self.assertGreater(self.client.compare(appleFingerprint, bananaString), 0.1)
        self.assertGreater(self.client.compare(appleFingerprint, bananaFingerprint), 0.1)

        self.assertGreater(self.client.compare(fingerprint, "language"), 0.1)
        self.assertGreater(self.client.compare(fingerprint, list(range(100))), 0.1)
        self.assertGreater(self.client.compare("language", fingerprint), 0.1)
        self.assertGreater(self.client.compare(fingerprint, "Linguistics is the scientific study of language"), 0.1)
        
        try:
            self.client.compare("", 2)
            self.fail("An exception should have been thrown")
        except CorticalioException:
            pass

    def testCategoryF2ilter(self):
        fingerprint = self.client.createCategoryFilter(["once upon a time", "lived a noble prince"])
        self.assertEqual(type(fingerprint), list)
        self.assertGreater(len(fingerprint), 50)
        self.assertEqual(type(fingerprint[0]), int)
        
        try:
            self.client.createCategoryFilter([])
            self.fail("An exception should have been thrown")
        except CorticalioException:
            pass

if __name__ == "__main__":
    unittest.main()
