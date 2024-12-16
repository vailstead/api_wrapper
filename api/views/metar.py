"""
Docstring
"""
from typing import List
from api.models.metar import Metar
from api.views.api_view import ApiView


class MetarView(ApiView):
    """
    Class docstring
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_metar_list(self) -> List:
        """
        Docstring
        :return:
        """
        my_params = {'format': "json"}
        metar = self._api.get("metar/", my_params)
        metar_list = []
        for d in metar.data:
            d["_icao_id"] = d.pop('icaoId')
            d["_metar_id"] = d.pop('metar_id')
            metar_list.append(Metar(
                metar_id=d["_metar_id"],
                icao_id=d["_icao_id"],
                **d
            ))
        return metar_list

    def get_single_metar(self) -> Metar:
        """
        Docstring
        :return:
        """
        metar_list = self.get_metar_list()
        return metar_list[0]
