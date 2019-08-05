from microbit import *
import radio

radio.on()


def sendMessage():
    while True:
        radio.send("Anyone listening? It's MJ")
        sleep(5000)


def receiveMessage():
    newmessage = radio.receive()
    display.scroll(newmessage)


sendMessage()
receiveMessage()
