# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.subsidy import Subsidy  # noqa: E501
from swagger_server.models.subsidy_base import SubsidyBase  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSubsidiesController(BaseTestCase):
    """SubsidiesController integration test stubs"""

    def test_subsidies_id_actions_approve_post(self):
        """Test case for subsidies_id_actions_approve_post

        Approve a subsidy
        """
        body = User()
        response = self.client.open(
            '/v1/subsidies/{id}/actions/approve'.format(id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/nl.kpmg.v1.user+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidies_id_delete(self):
        """Test case for subsidies_id_delete

        Remove a subsidy
        """
        response = self.client.open(
            '/v1/subsidies/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidies_id_get(self):
        """Test case for subsidies_id_get

        Returns a specific subsidy
        """
        response = self.client.open(
            '/v1/subsidies/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidies_id_patch(self):
        """Test case for subsidies_id_patch

        Edit a subsidy's information
        """
        body = Subsidy()
        response = self.client.open(
            '/v1/subsidies/{id}'.format(id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/nl.kpmg.v1.subsidy+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidies_id_put(self):
        """Test case for subsidies_id_put

        Re-upload a subsidy's information
        """
        body = Subsidy()
        response = self.client.open(
            '/v1/subsidies/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/nl.kpmg.v1.subsidy+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_subsidies_post(self):
        """Test case for subsidies_post

        Create a new subsidy
        """
        body = SubsidyBase()
        response = self.client.open(
            '/v1/subsidies',
            method='POST',
            data=json.dumps(body),
            content_type='application/nl.kpmg.v1.subsidy-base+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
