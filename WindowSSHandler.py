import Checks
import win32gui
import win32con
import pyautogui
import time
import string
import random


def ScreenShotWindow(process):
    if Checks.CheckForWindow(process) is False:
        print("Minecraft java isn't open")
        exit()

    hwnd = win32gui.FindWindow(None, process)

    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)

    time.sleep(.25)
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(10))
    pyautogui.screenshot().save(result_str + ".png")
    return result_str + ".png"
