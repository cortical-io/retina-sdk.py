"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
class Metric(object):
    def __init__(self, cosineSimilarity=None, jaccardDistance=None, overlappingAll=None, overlappingLeftRight=None, overlappingRightLeft=None, sizeLeft=None, sizeRight=None, weightedScoring=None, euclideanDistance=None):
        #Get Cosine-Similarity.
        self.cosineSimilarity = cosineSimilarity # float
        #Get Jaccard-Distance.
        self.jaccardDistance = jaccardDistance # float
        #Get Overlapping-All.
        self.overlappingAll = overlappingAll # int
        #Get Overlapping-Left-Right.
        self.overlappingLeftRight = overlappingLeftRight # float
        #Get Overlapping-Right-Left.
        self.overlappingRightLeft = overlappingRightLeft # float
        #Get Size-left.
        self.sizeLeft = sizeLeft # int
        #Get Size-Right.
        self.sizeRight = sizeRight # int
        #Get the Weighted-Scoring.
        self.weightedScoring = weightedScoring # float
        #Get Euclidean-Distance.
        self.euclideanDistance = euclideanDistance # float
        
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join(["%s=%s" % (tup[0], repr(tup[1])) for tup in vars(self).items()]))

