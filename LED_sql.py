from importlib.abc import TraversableResources
from os import getppid
from pydoc import ispackage
import gpiozero
import sqlite3

class LED():
    def __init__(self, gpioPin : int, ledOn : bool) -> None:
        self.gpioPin = gpioPin
        self.ledOn = ledOn

    def SetLED(self):
        self.gpioPin = LED(14)
        if self.Taster1.returnStatus():
            self.gpioPin.on()
        else:
            self.gpioPin.off()

    def holdTime(self):
        pass

class Taster():
    def __init__(self, pin : int, isPressed : bool) -> None:
        self.pin = pin
        self.isPressed = isPressed
        self.con = sqlite3.connect("LED.db")
        self.cur = self.con.cursor()

    def buttonPress(self):
        self.cur.execute("tables")
        #if self.pin.when_pressed:
         #   self.isPressed = True
          #  self.cur.execute("SHOW TABLES")
        #self.pin.when_released = self.isPressed = False


    def returnStatus(self):
        return self.isPressed

    


Taster1 = Taster(4, False)
LED1 = LED(14, False)
Taster1.buttonPress()