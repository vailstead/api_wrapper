"""
Module level docstring
"""
from api.views import (
    MetarView
)

metars = MetarView()
print(metars.get_single_metar())
