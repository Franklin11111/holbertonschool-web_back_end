#!/usr/bin/env python3
"""Testing functions in client.py"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_obj = GithubOrgClient(org_name)
        url = f"https://api.github.com/orgs/{org_name}"

        self.assertEqual(test_obj.org, {'key': 'value'})
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one based
        on the mocked payload"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://nowhere.com"}
            test_obj = GithubOrgClient('foo')
            self.assertEqual(test_obj._public_repos_url,
                             "https://nowhere.com")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """public_repos unit test
        - list of repos is what you expect from the chosen payload
        - mocked property and the mocked get_json was called once"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            payload = {'login': 'microsoft',
                       'id': 6154722,
                       'node_id': 'MDEyOk9yZ2FuaXphdGlvbjYxNTQ3MjI=',
                       'url': 'https://api.github.com/orgs/microsoft',
                       'repos_url':
                           'https://api.github.com/orgs/microsoft/repos'}

            test_object = GithubOrgClient('foo')
            mock_get_json.return_value = payload
            org = test_object.org
            mock_public_repos_url.return_value = org.get('repos_url')

            self.assertEqual(test_object._public_repos_url,
                             'https://api.github.com/orgs/microsoft/repos')
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once_with()
