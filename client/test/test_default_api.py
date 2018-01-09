# coding: utf-8

"""
    SmartAPI API

    This is the API provided from [SmartAPI](http://smart-api.info) application.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: cwu@scripps.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_get(self):
        """Test case for query_get

        Query metadata for matching APIs.  # noqa: E501
        """
        pass

    def test_suggestion_get(self):
        """Test case for suggestion_get

        Return suggested values for a give field.  # noqa: E501
        """
        pass

    def test_validate_get(self):
        """Test case for validate_get

        Validate input SmartAPI metadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()