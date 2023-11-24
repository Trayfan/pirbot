from __future__ import annotations

import pyautogui
import pyscreenshot as ImageGrab

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data.cords import Cords


def click(cords:Cords, double:bool=False):
    pyautogui.moveTo((cords.x, cords.y))
    if double:
        click(cords)
    pyautogui.mouseDown(cords.x, cords.y)
    pyautogui.mouseUp(cords.x, cords.y)

def get_cord_color(cords:Cords) -> (int, int, int):
    im=ImageGrab.grab(bbox=(cords.x,cords.y,cords.x+1,cords.y+1)).load()
    return im[0, 0]
