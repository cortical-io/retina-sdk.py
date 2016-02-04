"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""

from retinasdk.model import category_filter


class ClassifyApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient

    

    def createCategoryFilter(self, retina_name, filter_name, body, ):
        """get filter for classifier
        Args:
            filter_name, str: A unique name for the filter. (required)
            body, FilterTrainingObject: The list of positive and negative (optional) example items. (required)
            retina_name, str: The retina name (required)
            Returns: CategoryFilter
        """

        resourcePath = '/classify/create_category_filter'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['filter_name'] = filter_name
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
            
        return category_filter.CategoryFilter(**response.json())
    


