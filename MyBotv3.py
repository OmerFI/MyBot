import pyautogui
import threading
import time
from pynput.keyboard import Listener, Key, Controller

__version__ = 1.0

keyboard = Controller()


def press1():
    while True:
        pyautogui.click(586, 778, 2, 1.5, "right")
        time.sleep(70)


def press2():
    while True:
        pyautogui.click(618, 778, 2, 2, "right")
        time.sleep(110)


def press3():
    while True:
        pyautogui.click(446, 778, 2, 0.1, "right")
        time.sleep(3)


def press4():
    while True:
        pyautogui.click(478, 778, 2, 0.1, "right")
        time.sleep(4)


"""
1 - 446,778
2 - 478,778
f1 - 586,778
f2 - 618,778
"""

k = threading.Thread(target=press1)
l = threading.Thread(target=press2)
m = threading.Thread(target=press3)
n = threading.Thread(target=press4)

time.sleep(5)

k.start()
l.start()
m.start()
n.start()


def start():
    with Listener(on_press=callback_function) as listener:
        listener.join()


def callback_function(key):
    if key == Key.delete:
        print("okay")
        exit()


p = threading.Thread(target=start)
p.start()

#
