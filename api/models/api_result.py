"""
Docstring
"""
from typing import List, Dict


class APIResult:
    """
    Docstring
    """
    def __init__(self,
                 status_code: int,
                 message: str = '',
                 data: List[Dict] = None):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []
