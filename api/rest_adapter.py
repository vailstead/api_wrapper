"""
Module docstring
"""
from json import JSONDecodeError
from urllib.parse import urlencode
from typing import Dict

import requests
import requests.packages

import api.config.settings
from api.config.exceptions import ApiException
from api.models.api_result import APIResult
from api.config.logger import Logger


class RestAdapter:
    """
    Docstring
    """

    def __init__(
            self,
            hostname: str = api.config.settings.API_BASE_URL,
            api_key: str = '',
            ssl_verify: bool = True):
        self._logger = Logger.get_logger(__name__, log_file=__name__ + ".log")
        self.url = f"https://{hostname}/"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # pylint: disable=E1101
            requests.packages.urllib3.disable_warnings()

    def _do(
            self,
            http_method: str,
            endpoint: str,
            ep_params: Dict = None,
            data: Dict = None) -> APIResult:
        full_url = self.url + endpoint
        headers = {'x-api-key': self._api_key}
        if ep_params:
            ep_params = urlencode(ep_params)
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ', '.join(
            (log_line_pre, "success={}, status_code={}, message={}"))
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method,
                                        url=full_url,
                                        verify=self._ssl_verify,
                                        headers=headers,
                                        params=ep_params,
                                        json=data,
                                        timeout=5)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=str(e))
            raise ApiException("Request failed") from e

        # handle non 200 responses (bad requests)
        is_success = 299 >= response.status_code >= 200
        log_line = log_line_post.format(is_success,
                                        response.status_code,
                                        response.reason)
        if not is_success:
            self._logger.debug(msg=log_line)
            raise ApiException(
                f"Request Error - Status Code {response.status_code}")
        try:
            data_out = response.json()
        except (ValueError, TypeError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise ApiException("Bad JSON in response") from e

        if is_success:
            self._logger.debug(msg=log_line)
            return APIResult(response.status_code,
                             message=response.reason,
                             data=data_out)
        # pylint: disable=W0719
        raise Exception(data_out["message"])

    def get(self,
            endpoint: str,
            ep_params: Dict = None) -> APIResult:
        """
        Docstring
        :param endpoint:
        :param ep_params:
        :return:
        """
        return self._do(http_method="GET", endpoint=endpoint, ep_params=ep_params)

    def post(self,
             endpoint: str,
             ep_params: Dict = None,
             data: Dict = None) -> APIResult:
        """
        Docstring
        :param endpoint:
        :param ep_params:
        :param data:
        :return:
        """
        return self._do(http_method="GET",
                        endpoint=endpoint,
                        ep_params=ep_params,
                        data=data)

    def delete(self,
               endpoint: str,
               ep_params: Dict = None,
               data: Dict = None) -> APIResult:
        """
        Docstring
        :param endpoint:
        :param ep_params:
        :param data:
        :return:
        """
        return self._do(http_method='DELETE',
                        endpoint=endpoint,
                        ep_params=ep_params,
                        data=data)
