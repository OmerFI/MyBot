import pyautogui
import threading
import time
from pynput.keyboard import Listener, Key, Controller

__version__ = 1.0


def press1():
    while True:
        pyautogui.press("1")
        time.sleep(0.05)
        pyautogui.press("1")
        time.sleep(3)


def press2():
    while True:
        pyautogui.press("2")
        time.sleep(0.05)
        pyautogui.press("2")
        time.sleep(3.01)


def press3():
    while True:
        pyautogui.press("\"")
        time.sleep(0.05)
        pyautogui.press("\"")
        time.sleep(1)


def press4():
    while True:
        pyautogui.press("f1")
        time.sleep(1)
        pyautogui.press("f1")
        time.sleep(61)


def press5():
    while True:
        pyautogui.press("f2")
        time.sleep(2)
        pyautogui.press("f2")
        time.sleep(111)


t = threading.Thread(target=press1)
k = threading.Thread(target=press2)
l = threading.Thread(target=press3)
m = threading.Thread(target=press4)
n = threading.Thread(target=press5)

time.sleep(10)

t.start()
k.start()
l.start()


# m.start()
# n.start()

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
