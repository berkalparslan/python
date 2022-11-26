#! python3
import time
import pyautogui, sys

def findPosition():
    print("Press Ctrl-C to quit.")
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(positionStr, end="")
            print("\b" * len(positionStr), end="", flush=True)
    except KeyboardInterrupt:
        print("exited")

def click():
    j = 1
    for i in range(1, 600):
        pyautogui.click(x=1696, y=1172)
        time.sleep(15)
        print("clicked")

findPosition()
# click()