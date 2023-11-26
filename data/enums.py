from enum import Enum


class ItemType(Enum):
    Ticket = 1
    AnotherCell = 2
    Disapear = 3
    Buff = 4

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
    MagicalOcean = "Magical Ocean"
    Ascaron = "Ascaron"
    ArgentCity = "Argent City"

class Ticket(Enum):
    IcespireHaven = [Location.IcespireHaven]
    AbandonMine1 = [Location.BelmontPlains]
    ThundoriaCastle = [Location.ThundoriaCastle]
    LoneTower = [Location.SacredForest]
    ThundoriaHarbor = [Location.ThundoriaHarbor, Location.Ascaron]
    SacredSnowMountain = [Location.SacredSnowMountain]
    OasisHaven = [Location.OasisHaven, Location.MagicalOcean]
    BarrenCavern = [Location.SouthernDesert]
    AndesForestHaven = [Location.AndesForestHaven]
    ArgentCity = [Location.ArgentCity]



class ImageMode(Enum):
    Binary = 1
    Default = 2

class RecognitionMode(Enum):
    Number = 1
    All = 2