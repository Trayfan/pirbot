from typing import List
from client_interactions import click, get_cord_color
from data.enums import ItemType


class _UsableObject:
    def use(self):
        if self.item:
            match self.item.type_:
                case ItemType.Ticket:
                    pass
                case ItemType.Openable:
                    color = get_cord_color(self.item.check_open)
                    while color != self.item.check_color:
                        click(self.cords, self.double)
                        color = get_cord_color(self.item.check_open)
        else:
            click(self.cords, self.double)

class Cords:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

class _PanelBtn(_UsableObject):
    def __init__(self, cords:Cords):
        self.cords = cords
        self.double = False

        self.item_:Item = None

    def __str__(self) -> str:
        return f"{self.cords}"

class Item:
    def __init__(self, type_:str, check_open:Cords, check_color:(int, int, int)):
        self.type_ = type_
        self.check_use = check_open
        self.check_color = check_color


class _Box:
    def __init__(self, cord1:Cords, cord2:Cords):
        self.cord1 = cord1
        self.cord2 = cord2

class InvSlot(_UsableObject):
    def __init__(self, box:_Box):
        self.box = box
        self.cords = Cords(
            self.box.cord2.x - (self.box.cord2.x - self.box.cord1.x) / 2,
            self.box.cord2.y - (self.box.cord2.y - self.box.cord1.y) / 2
        )
        self.double = True
        self.item:Item = None

    def __str__(self) -> str:
        return f"{self.box.cord1} - {self.box.cord2}"

class _Interface:
    def open(self):
        color = get_cord_color(self.check_open)
        while color != self.check_color:
            click(self.ui_btn)
            color = get_cord_color(self.check_open)

class Interfaces:
    class Panel:
        def __init__(self) -> None:
            self.slots:List[List[_PanelBtn]] = []
            self.__fill_info()
        
        def __fill_info(self):
            offset_x = 34
            offset_y = 34
            
            x = 1054
            y = 1409
            for row in range(2):
                panel_row = []
                for column in range(12):
                    panel_row.append(_PanelBtn(Cords(x + offset_x * column, y - offset_y * row)))
                self.slots.append(panel_row)

    class Inventory(_Interface):
        def __init__(self) -> None:
            self.slots:List[List[InvSlot]] = []
            self.ui_btn = Cords(2355, 1420)
            self.check_open = Cords(662, 122)
            self.check_color = (235, 235, 235)
            self.__fill_info()

        def __fill_info(self):
            offset_x = 38
            offset_y = 38
            x1 = 352
            y1 = 232
            x2 = 389
            y2 = 269
            for row in range(6):
                inv_row = []
                for column in range(8):
                    inv_row.append(InvSlot(_Box(Cords(x1 + offset_x * column, y1 + offset_y * row), Cords(x2 + offset_x * column, y2 + offset_y * row))))
                self.slots.append(inv_row)

class Game:
    def __init__(self) -> None:
        self.inv = Interfaces.Inventory()
        self.panel = Interfaces.Panel()
