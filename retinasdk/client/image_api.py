"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
from retinasdk.model import image


class ImageApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient

    

    def getImageForExpression(self, retina_name, body, image_scalar=2, plot_shape="circle", image_encoding="base64/png", sparsity=1.0):
        """Get images for expressions
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            image_scalar, int: The scale of the image (optional) (optional)
            plot_shape, str: The image shape (optional) (optional)
            image_encoding, str: The encoding of the returned image (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: java.io.ByteArrayInputStream
        """

        resourcePath = '/image'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'image/png', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['image_scalar'] = image_scalar
        queryParams['plot_shape'] = plot_shape
        queryParams['image_encoding'] = image_encoding
        queryParams['sparsity'] = sparsity
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return response.content

        

    def getOverlayImage(self, retina_name, body, plot_shape="circle", image_scalar=2, image_encoding="base64/png"):
        """Get an overlay image for two expressions
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded comparison array to be evaluated (required)
            plot_shape, str: The image shape (optional) (optional)
            image_scalar, int: The scale of the image (optional) (optional)
            image_encoding, str: The encoding of the returned image (optional)
            Returns: java.io.ByteArrayInputStream
        """

        resourcePath = '/image/compare'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'image/png', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['plot_shape'] = plot_shape
        queryParams['image_scalar'] = image_scalar
        queryParams['image_encoding'] = image_encoding
        postData = body
        
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return response.content

        

    def getImageForBulkExpressions(self, retina_name, body, get_fingerprint=None, image_scalar=2, plot_shape="circle", sparsity=1.0):
        """Bulk get images for expressions
        Args:
            retina_name, str: The retina name (required)
            body, ExpressionOperation: The JSON encoded expression to be evaluated (required)
            get_fingerprint, bool: Configure if the fingerprint should be returned as part of the results (optional)
            image_scalar, int: The scale of the image (optional) (optional)
            plot_shape, str: The image shape (optional) (optional)
            sparsity, float: Sparsify the resulting expression to this percentage (optional)
            Returns: Array[Image]
        """

        resourcePath = '/image/bulk'
        method = 'POST'

        queryParams = {}
        headerParams = {'Accept': 'Application/json', 'Content-Type': 'application/json'}
        postData = None

        queryParams['retina_name'] = retina_name
        queryParams['image_scalar'] = image_scalar
        queryParams['plot_shape'] = plot_shape
        queryParams['sparsity'] = sparsity
        queryParams['get_fingerprint'] = get_fingerprint
        postData = body
        response = self.apiClient._callAPI(resourcePath, method, queryParams, postData, headerParams)
        return [image.Image(**r) for r in response.json()]



