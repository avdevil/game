import platform
import os
import time
import random
import urllib.request

def banner():

 print(r"************************************** ")
 print(r"*******#### coded by avhacker #******* ")
 print(r"************************************** ") 
 
banner()

April Fools’ Day Python Prank
 March 31, 2017  Grayson Stanton  Uncategorized
“With great power comes great responsibility.
 Except on April Fools’ Day.”
              - Uncle Ben

Do you know someone who Karma’s been slacking on lately? Looking for a harmless April Fools’ Day prank that allows you to flex your Pythonic muscles? Well look no further. Here’s a simple little prank you can quickly code up in Python, customize for maximum effect, and maybe even learn about a couple useful Python packages along the way.

You will want Python installed to code the prank, but the victim probably won’t need to have Python on their machine. This prank makes use of the wonderfully easy-to-use pyautogui package, which allows you to automate mouse and keyboard actions, as well as make message boxes and take screenshots.

So here’s the idea: the victim gets on their computer (after you’ve had a minute or two with it) and sees a seemingly harmless message that they close, which triggers their cursor to start freaking out (after which, we hope, the victim starts freaking out…at least a little bit).

If you haven’t used pyautogui before, install it by entering the following command in Windows Command Prompt (or the Mac OS X or Linux equivalent):

pip install pyautogui
Looking over some pyautogui examples, you should start to get some ideas of what’s possible. Keep in mind that a fail-safe mechanism is built into pyautogui where if you move the cursor to the top-left corner of the screen (which you can usually do if you are quick with the mouse, even if the cursor’s moving quite fast on its own), an exception will be raised and the program will abort. This can be disabled, but exercise caution if you choose to do so.

Now let’s get to coding. Here’s that starter script I mentioned:

import time
import random
import pyautogui

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
