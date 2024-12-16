"""
Module docstring
"""
import os

API_BASE_URL = "aviationweather.gov/api/data"
API_KEY = os.environ.get("API_KEY", None)
API_SSL_VERIFY = os.environ.get("API_SSL_VERIFY", True)
LOG_DIR = os.path.dirname(os.path.abspath(__file__))
