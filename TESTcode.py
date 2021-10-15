import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio
mouse=Mouse(usb_hid.devices)


while True:

    time.sleep(7)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=830,x=270) #Camera opener
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=290,x=410) # Multi Snap clicker
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=297,x=410)  #Multisnap opener
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=740,x=270) #Click Photo
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=500,x=270) # OK 8 snap limit
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=830,x=410) # Click Send
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=175,x=170) # Ghost Click
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(1)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=225,x=390) # Select All Click
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(1)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    mouse.move(y=830,x=410) # Finish Click
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.5)
    mouse.move(y=-1000,x=-1000)
    time.sleep(0.5)
    
    
    for x in range(2):
        time.sleep(7)
        mouse.move(y=-1000,x=-1000)
        time.sleep(0.5)
        mouse.move(y=830,x=270) #Camera opener
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.move(y=-1000,x=-1000)
        time.sleep(0.5)
        mouse.move(y=740,x=270) #Click Photo
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(1)
        mouse.move(y=-1000,x=-1000)
        time.sleep(0.5)
        mouse.move(y=500,x=270) # OK 8 snap limit
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.move(y=-1000,x=-1000)
        time.sleep(0.5)
        mouse.move(y=830,x=410) # Click Send
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.move(y=-1000,x=-1000)
        time.sleep(0.5)
        mouse.move(y=175,x=170) # Ghost Click
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(1)
        mouse.move(y=-1000,x=-1000)
        time.sleep(0.5)
        mouse.move(y=225,x=390) # Select All Click
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(1)
        mouse.move(y=-1000,x=-1000)
        time.sleep(0.5)
        mouse.move(y=830,x=410) # Finish Click
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.5)
        mouse.move(y=-1000,x=-1000)
        time.sleep(0.5)

    


    
