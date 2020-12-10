import threading
import time
from pynput.keyboard import Listener, Key, Controller

__version__ = 1.0

keyboard = Controller()


def press1():
    while True:
        keyboard.press("1")
        keyboard.release("1")
        time.sleep(0.05)
        keyboard.press("1")
        keyboard.release("1")
        time.sleep(3)


def press2():
    while True:
        keyboard.press("2")
        keyboard.release("2")
        time.sleep(0.05)
        keyboard.press("2")
        keyboard.release("2")
        time.sleep(3.01)


def press3():
    while True:
        keyboard.press("\"")
        keyboard.release("\"")
        time.sleep(0.05)
        keyboard.press("\"")
        keyboard.release("\"")
        time.sleep(1)


def press4():
    while True:
        keyboard.press("f1")
        keyboard.release("f1")
        time.sleep(1)
        keyboard.press("f1")
        keyboard.release("f1")
        time.sleep(61)


def press5():
    while True:
        keyboard.press("f2")
        keyboard.release("f2")
        time.sleep(2)
        keyboard.press("f2")
        keyboard.release("f2")
        time.sleep(111)


t = threading.Thread(target=press1)
k = threading.Thread(target=press2)
l = threading.Thread(target=press3)
m = threading.Thread(target=press4)
n = threading.Thread(target=press5)

time.sleep(5)

t.start()
k.start()


# l.start()
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
