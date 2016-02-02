"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""

class LanguageRest(object):

    def __init__(self, language=None, iso_tag=None, wiki_url=None):
        #Language
        self.language = language # str
        #ISO tag
        self.iso_tag = iso_tag # str
        #Get Wiki URL
        self.wiki_url = wiki_url # str
        
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, ", ".join(["%s=%s" % (tup[0], repr(tup[1])) for tup in vars(self).items()]))

