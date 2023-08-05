from enum import Enum


class BatteryType(Enum):
    UNKNOWN = 'Unknown'
    LI_ION = 'Li-Ion'
    NI_MH = 'NiMH'
    NICD = 'NiCd'
