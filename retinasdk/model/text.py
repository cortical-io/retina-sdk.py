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

class Text(object):
    def __init__(self, text=None, fingerprint=None):
        #The text as a string
        self.text = text # str
        #The semantic fingerprint representation of the text.
        self.fingerprint = Fingerprint(**fingerprint) if isinstance(fingerprint, dict) else fingerprint # Fingerprint
        
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join(["%s=%s" % (tup[0], repr(tup[1])) for tup in vars(self).items()]))

