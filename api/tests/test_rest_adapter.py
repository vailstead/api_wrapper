# pylint: disable=W0212,W0201
"""
Docstring
"""
from unittest import mock

import requests
import pytest

from requests.exceptions import RequestException
from api.config.exceptions import ApiException
from api.models.api_result import APIResult
from api.rest_adapter import RestAdapter


class TestRestAdapter():
    """
    Docstring
    """
    def setup_method(self) -> None:
        """
        Docstring
        :return:
        """
        self.rest_adapter = RestAdapter()
        self.response = requests.Response()

    def teardown_method(self) -> None:
        """
        Docstring
        :return:
        """
        # pylint: disable=W0107
        pass

    def test__do_good_request_returns_result(self):
        """
        Docstring
        :return:
        """
        self.response.status_code = 200
        self.response._content = "{}".encode()
        with mock.patch("requests.request", return_value=self.response):
            result = self.rest_adapter._do('GET', '')
            assert isinstance(result, APIResult)

    def test__do_bad_request_raises_api_exception(self):
        """
        Docstring
        :return:
        """
        with mock.patch("requests.request", side_effect=RequestException):
            with pytest.raises(ApiException):
                self.rest_adapter._do('GET', '')

    def test__do_bad_json_raises_api_exception(self):
        """
        Docstring
        :return:
        """
        bad_json = '{"some bad json": '
        self.response._content = bad_json
        with mock.patch("requests.request", return_value=self.response):
            with pytest.raises(ApiException):
                self.rest_adapter._do('GET', '')

    def test__do_300_or_higher_raises_api_exception(self):
        """
        Docstring
        :return:
        """
        self.response.status_code = 300
        with mock.patch("requests.request", return_value=self.response):
            with pytest.raises(ApiException):
                self.rest_adapter._do('GET', '')

    def test__do_199_or_lower_raises_api_exception(self):
        """
        Docstring
        :return:
        """
        self.response.status_code = 199
        with mock.patch("requests.request", return_value=self.response):
            with pytest.raises(ApiException):
                self.rest_adapter._do('GET', '')
