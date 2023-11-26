import difflib
from typing import List
from client_interactions import click, get_cord_color, get_image, write
from data.enums import ItemType, Location, RecognitionMode, ImageMode
from data.recognition import get_text
from time import sleep


class _UsableObject:
    def use(self):
        if not self.item:
            print("К ячейке не привязан предмет!", self.item)
            exit()
        if self.get_color() != self.item.color:
            print("Предмет для использования не найден!", self.item)
            exit()
        open_count = 0
        match self.item.type_:
            case ItemType.Ticket:
                current_location = Interfaces.Minimap.location()
                while current_location not in self.item.check_object.value:
                    click(self.cords, self.double)
                    sleep(1)
                    current_location = Interfaces.Minimap.location()
                print(f"Находимся в локации: {current_location.value}")
            case ItemType.Disapear:
                color = self.item.check_object.get_color()
                while color == self.item.check_object.item.color and open_count < 30:
                    click(self.cords, self.double)
                    # кликаем по безопасному месту в инвентаре
                    click(Cords(622, 473))
                    color = self.item.check_object.get_color()
                    open_count += 1
                print(f"Использован предмет: {self.item.name}")
            case ItemType.AnotherCell:
                color = self.item.check_object.get_color()
                while color != self.item.check_object.item.color and open_count < 30:
                    click(self.cords, self.double)
                    # кликаем по безопасному месту в инвентаре
                    click(Cords(622, 473))
                    color = self.item.check_object.get_color()
                    open_count += 1
                print(f"Использован предмет: {self.item.name}")
            case ItemType.Buff:
                color = get_cord_color(self.item.check_object[0])
                while color != self.item.check_object[1]:
                    click(self.cords, self.double)
                    sleep(1)
                    color = get_cord_color(self.item.check_object[0])
            case _:
                click(self.cords, self.double)
        if open_count >= 30:
            print("Не удалось использовать предмет!", self.item)
            exit()

    def get_color(self):
        return get_cord_color(self.cords)

class Cords:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
    
    def __eq__(self, __value: object) -> bool:
        return ((self.x, self.y) == (__value.x, __value.y))

class _PanelBtn(_UsableObject):
    def __init__(self, cords:Cords):
        self.cords = cords
        self.double = False

        self.item:Item = None

    def __str__(self) -> str:
        return f"{self.cords}"

class Item:
    def __init__(self, name:str, type_:str, check_object, color:(int, int, int)=None):
        self.name = name
        self.type_ = type_
        self.color = color
        self.check_object = check_object

    def __str__(self) -> str:
        return self.name

class _Box:
    def __init__(self, cord1:Cords, cord2:Cords):
        self.cord1 = cord1
        self.cord2 = cord2

class InvSlot(_UsableObject):
    def __init__(self, box:_Box):
        self.box = box
        self.cords = Cords(
            int(self.box.cord2.x - (self.box.cord2.x - self.box.cord1.x) / 2),
            int(self.box.cord2.y - (self.box.cord2.y - self.box.cord1.y) / 2)
        )
        self.double = True
        self.item:Item = None

    def get_treasure_cords(self):
        file_name = "images/treasure_cords.png"
        click(self.cords)
        get_image(_Box(Cords(530, 290), Cords(530+56, 290+11)), file_name)
        raw_text = get_text(file_name)
        x = int(raw_text.split(",")[0])
        y = int(raw_text.split(",")[1])
        if x == 697:
            x = 897
        elif x == 642:
            x = 842
        elif x == 647:
            x = 847
        print(f"Получены координаты: {Cords(x, y)}")
        return Cords(x, y)


    def __str__(self) -> str:
        return f"{self.box.cord1} - {self.box.cord2}"

class _Interface:
    def open(self):
        color = get_cord_color(self.check_open)
        while color != self.check_color:
            click(self.ui_btn)
            color = get_cord_color(self.check_open)
        print(f"{self.__class__.__name__} открыт")

class Button:
    def __init__(self, cords:Cords, check_cords:Cords=None, check_color:(int, int, int)=None, reverse:bool=False):
        self.cords = cords
        self.check_cords = check_cords
        self.check_color = check_color
        self.reverse=reverse

    def click_btn(self):
        if self.reverse:
            color = get_cord_color(self.check_cords)
            while color == self.check_color:
                click(self.cords)
                sleep(0.1)
                color = get_cord_color(self.check_cords)
        else:
            color = get_cord_color(self.check_cords)
            while color != self.check_color:
                click(self.cords)
                sleep(0.1)
                color = get_cord_color(self.check_cords)

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

    class Minimap:
        def location() -> Location:
            file_name = "images/location.png"
            get_image(box=_Box(Cords(2408, 12), Cords(2408 + 130, 12 + 15)), file_name=file_name, threshold=180)
            raw_text = get_text(file_name, RecognitionMode.All)
            loc_win = None
            loc_win_ratio = 0
            for loc in Location:
                ratio = difflib.SequenceMatcher(None, raw_text, loc.value).ratio()
                if loc_win_ratio < ratio:
                    loc_win = loc
                    loc_win_ratio = ratio
            return loc_win
        
        def get_char_cord():
            file_name = "images/char_cords.png"
            add_pixel = [Cords(31, 11), Cords(32, 9), Cords(31, 9)] # [Cords(32, 12), Cords(32, 9), Cords(31, 9)]
            get_image(box=_Box(Cords(2440, 189), Cords(2440 + 70, 189 + 12)), file_name=file_name, threshold=150, add_pixel=add_pixel)
            raw_text = get_text(file_name)
            return raw_text
            # print(raw_text)
            # try:
            #     x = raw_text.replace(".", ",").split(",")[0]
            #     y = raw_text.replace(".", ",").split(",")[1]
            #     return Cords(int(x), int(y))
            # except:
            #     return Cords(0, 0)


        def wait_running():
            print("Бежим к точке")
            while 1:
                cords1 = Interfaces.Minimap.get_char_cord()
                sleep(1)
                cords2 = Interfaces.Minimap.get_char_cord()
                # print(cords1, cords2)
                # if cords1 == cords2 == Cords(0, 0):
                #     continue
                if cords1 == cords2:
                    return True
        
    class Radar(_Interface):
        def __init__(self) -> None:
            self.ui_btn = Cords(1182, 1339)
            self.check_open = Cords(526, 222)
            self.check_color = (235, 235, 235)
            self.confirm = Button(cords=Cords(480, 300), check_cords=Cords(526, 222), check_color=(235, 235, 235), reverse=True)

        def write_cords(self, cords:Cords):
            click(Cords(420, 275))
            write(cords.x)
            sleep(0.1)
            click(Cords(500, 275), True)
            write(cords.y)
            sleep(0.1)

        def go_to(self, cords:Cords):
            print(f"Двигаемся к точке: {cords}")
            self.open()
            self.write_cords(cords)
            self.confirm.click_btn()

class Game:
    def __init__(self) -> None:
        self.inv = Interfaces.Inventory()
        self.panel = Interfaces.Panel()
        self.minimap = Interfaces.Minimap
        self.radar = Interfaces.Radar()
        print("Бот инициализирован")