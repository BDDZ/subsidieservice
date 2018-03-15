# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.master_account import MasterAccount  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMasterAccountsController(BaseTestCase):
    """MasterAccountsController integration test stubs"""

    def test_master_accounts_get(self):
        """Test case for master_accounts_get

        Returns a list of master-accounts.
        """
        response = self.client.open(
            '/v1/master-accounts',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_master_accounts_id_delete(self):
        """Test case for master_accounts_id_delete

        Remove a master-account
        """
        response = self.client.open(
            '/v1/master-accounts/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_master_accounts_id_get(self):
        """Test case for master_accounts_id_get

        Returns a specific master-account
        """
        response = self.client.open(
            '/v1/master-accounts/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_master_accounts_id_patch(self):
        """Test case for master_accounts_id_patch

        Edit a master-account's information
        """
        body = MasterAccount()
        response = self.client.open(
            '/v1/master-accounts/{id}'.format(id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/nl.kpmg.v1.master-account+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_master_accounts_id_put(self):
        """Test case for master_accounts_id_put

        Re-upload a master-account's information
        """
        body = MasterAccount()
        response = self.client.open(
            '/v1/master-accounts/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/nl.kpmg.v1.master-account+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_master_accounts_post(self):
        """Test case for master_accounts_post

        Create a new master-account
        """
        body = MasterAccount()
        response = self.client.open(
            '/v1/master-accounts',
            method='POST',
            data=json.dumps(body),
            content_type='application/nl.kpmg.v1.master-account+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
