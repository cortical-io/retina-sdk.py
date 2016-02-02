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

class Term(object):
    def __init__(self, fingerprint=None, term=None, df=None, pos_types=None, score=None):
        #The Fingerprint of this term.
        self.fingerprint = Fingerprint(**fingerprint) if isinstance(fingerprint, dict) else fingerprint # Fingerprint
        #The term as a string.
        self.term = term # str
        #The df value of this term.
        self.df = df # float
        #The pos types of the term.
        self.pos_types = pos_types # list[str]
        #The score of this term.
        self.score = score # float

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join(["%s=%s" % (tup[0], repr(tup[1])) for tup in vars(self).items()]))

