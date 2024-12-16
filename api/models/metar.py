"""
Docstring
"""
from dataclasses import dataclass, field

@dataclass
class Metar:
    """
    Docstring
    """
    metar_id: int
    icao_id: str
    extra_data: dict = field(default_factory=dict)  # Store additional data

    def __init__(self, metar_id: int, icao_id: str, **kwargs):
        self.metar_id = metar_id
        self.icao_id = icao_id
        self.extra_data = kwargs  # Capture unexpected keyword arguments

    # def __str__(self):
    #     return f"{self.metar_id} - {self.icao_id}"



    # def __post_init__(self):
    #     """
    #     Method in @dataclass that is called immediately after __init__.
    #     Use it for any post init processing
    #     :return:
    #     """
    #     if hasattr(self, 'extra') and self.extra:
    #         for key, value in self.extra.items():
    #             if not hasattr(self, key):
    #                 setattr(self, key, value)
    # receipt_time: datetime
    # obs_time: int
    # report_time: datetime
    # wdir: Optional[Union[int, WdirEnum]] = None
    # visib: Optional[Union[float, VisibEnum]] = None
    # qc_field: int
    # max_t24: None
    # min_t24: None
    # pcp3_hr: None
    # pcp6_hr: None
    # pcp24_hr: None
    # snow: None
    # metar_type: MetarType
    # raw_ob: str
    # most_recent: int
    # lat: float
    # lon: float
    # elev: int
    # prior: int
    # name: str
    # clouds: List[Cloud]
    # temp: Optional[float] = None
    # dewp: Optional[float] = None
    # wspd: Optional[int] = None
    # wgst: Optional[int] = None
    # altim: Optional[float] = None
    # slp: Optional[float] = None
    # wx_string: Optional[str] = None
    # pres_tend: Optional[float] = None
    # max_t: Optional[float] = None
    # min_t: Optional[int] = None
    # precip: Optional[float] = None
    # vert_vis: Optional[int] = None
