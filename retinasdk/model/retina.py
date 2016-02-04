"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
class Retina(object):
    def __init__(self, retinaName=None, numberOfTermsInRetina=None, numberOfRows=None, numberOfColumns=None, description=None):
        #The identifier of a specific retina
        self.retinaName = retinaName # str
        #The number of terms contained in a specific retina
        self.numberOfTermsInRetina = numberOfTermsInRetina # long
        #Number of rows of the fingerprints
        self.numberOfRows = numberOfRows # int
        #Number of columns of the fingerprints
        self.numberOfColumns = numberOfColumns # int
        #The description of a specific retina
        self.description = description # str
        
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join(["%s=%s" % (tup[0], repr(tup[1])) for tup in vars(self).items()]))

