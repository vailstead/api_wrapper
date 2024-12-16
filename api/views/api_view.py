"""
Docstring
"""
from api.rest_adapter import RestAdapter
import api.config.settings

class ApiView:
    """
    class docstring
    """

    def __init__(
            self,
            hostname: str = api.config.settings.API_BASE_URL,
            api_key: str = api.config.settings.API_KEY,
            ssl_verify: bool = api.config.settings.API_SSL_VERIFY):
        self._api = RestAdapter(hostname, api_key, ssl_verify)
