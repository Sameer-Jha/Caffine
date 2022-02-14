#!/usr/bin/env python3
from time import sleep
from sys import exit
import pyautogui
import random

position = pyautogui.position()  # current mouse x and y
size = pyautogui.size()

while True:
    try:
        x = random.randint(1, 500)
        y = random.randint(1, 500)
        num_seconds = random.randint(2, 10)
        if pyautogui.onScreen(x, y): 
            pyautogui.moveTo(x, y, duration=num_seconds)
            sleep(10)
    except KeyboardInterrupt:
        exit()
    except:
        continue