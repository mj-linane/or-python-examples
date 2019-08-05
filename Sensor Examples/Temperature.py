from microbit import *

while True:
    tempc = temperature()
    tempf = int(((tempc * 9) / 5 + 32))
    tempfull = str(tempf) + "F"
    display.scroll(tempfull)
    sleep(3000)
