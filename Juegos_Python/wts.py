import random
import time
import pyautogui as pg

h = ("Te quiero","Te amo","Casate conmigo","Tengamos un hijo")
time.sleep(3)

while True:
    a = random.choice(h)
    pg.write(a)
    pg.press("enter")
    