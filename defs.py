from enum import IntEnum

class Lookups(IntEnum):
    discogs = 0
    catalog = 1

class Formats(IntEnum):
    flac24 = 0
    flac16 = 1
    opus128 = 2
    opus96 = 3
    opus64 = 4
