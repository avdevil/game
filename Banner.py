import platform
import os
import time
import random
import urllib.request

def banner():

 print(r"***************************************** ")
 print(r"*******#### coded by avhacker ####******* ")
 print(r"***************************************** ") 
 
banner()


import time
import random

def move_mouse(how_long_in_seconds):
    start_time = time.time()
    time_elapsed = time.time() - start_time
    xsize, ysize = pyautogui.size()
    
    while time_elapsed < how_long_in_seconds:
        x, y = random.randrange(xsize), random.randrange(ysize)
        pyautogui.moveTo(x, y, duration=0.2)
        time_elapsed = time.time() - start_time

if __name__ == "__main__":
    pyautogui.alert("Your Java update is now complete")
    move_mouse(120)
