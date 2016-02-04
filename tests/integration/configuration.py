"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
API_KEY = "your_api_key"
BASE_PATH="http://api.cortical.io/rest"
RETINA_NAME = "en_associative"

def isString(st):
    # for python 2 and 3
    try:
        return isinstance(st, basestring)
    except NameError:
        return isinstance(st, str)
