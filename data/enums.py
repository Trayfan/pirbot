from enum import Enum


class ItemType(Enum):
    Ticket = 1
    AnotherCell = 2
    Disapear = 3

class Location(Enum):
    IcespireHaven = "Icespire Haven"
    BelmontPlains = "Belmont Plains"
    ThundoriaCastle = "Thundoria Castle"
    SacredForest = "Sacred Forest"
    ThundoriaHarbor = "Thundoria Harbor"
    SacredSnowMountain = "Sacred Snow Mountain"
    OasisHaven = "Oasis Haven"
    SouthernDesert = "Southern Desert"
    AndesForestHaven = "Andes Forest Haven"


class ImageMode(Enum):
    Binary = 1
    Default = 2

class RecognitionMode(Enum):
    Number = 1
    All = 2