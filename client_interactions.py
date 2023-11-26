from __future__ import annotations

import pyautogui
import pyscreenshot as ImageGrab
from data.enums import Location, ImageMode

from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from data.cords import Cords, _Box


def click(cords:Cords, double:bool=False):
    pyautogui.moveTo((cords.x, cords.y))
    if double:
        click(cords)
    pyautogui.mouseDown(cords.x, cords.y)
    pyautogui.mouseUp(cords.x, cords.y)

def get_cord_color(cords:Cords) -> (int, int, int):
    im=ImageGrab.grab(bbox=(cords.x,cords.y,cords.x+1,cords.y+1)).load()
    return im[0, 0]

def get_image(box:_Box, file_name:str, mode:ImageMode=ImageMode.Binary, threshold=200, add_pixel:List[Cords]=None):
    im=ImageGrab.grab(bbox=(box.cord1.x, box.cord1.y, box.cord2.x, box.cord2.y))
    if mode == ImageMode.Binary:
        im=im.convert('L')
        width, height = im.size
        for x in range(width):
            for y in range(height):
                if im.getpixel((x, y)) < threshold:
                    im.putpixel((x, y), 0)
                else:
                    im.putpixel((x, y), 255)
    if add_pixel:
        for cords in add_pixel:
            im.putpixel((cords.x, cords.y), 255)
    im.save(file_name)

def write(text:str):
    pyautogui.write(str(text))

def press_key(key:str):
    pyautogui.press(key)