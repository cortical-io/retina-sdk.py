"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
from retinasdk.model.fingerprint import Fingerprint

class Image(object):
    def __init__(self, fingerprint=None, image_data=None):
        #The semantic fingerprint representation.
        self.fingerprint = Fingerprint(**fingerprint) if isinstance(fingerprint, dict) else fingerprint # Fingerprint
        #Image data in base64 encoding.
        self.image_data = image_data # list[byte]
        
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join(["%s=%s" % (tup[0], repr(tup[1])) for tup in vars(self).items()]))

