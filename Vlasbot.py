import RPi.GPIO as gpio
from time import sleep
import pinesGPIO as pin

class Robot():

    velocidad=50

    def __init__(self):
        print("Robot Creado!!!")    
        
    def Avanzar(self):
        print("Avanzando con el robot desde la clase")
        pin.pwm_b.start(self.velocidad) 
        pin.pwm_a.start(self.velocidad)
        gpio.output(pin.motor_a_pin2,gpio.HIGH)
        #gpio.output(pin.motor_a_pin1,gpio.LOW)  
        gpio.output(pin.motor_b_pin2,gpio.HIGH)
        #gpio.output(motor_b_pin1,gpio.LOW
        
    def Stop(self):
        print("Stop")
        gpio.output(pin.motor_a_pin2,gpio.LOW)
        gpio.output(pin.motor_b_pin2,gpio.LOW)
        gpio.output(pin.motor_a_pin1,gpio.LOW)
        gpio.output(pin.motor_b_pin1,gpio.LOW)
    
    def Retroceder(self):
        print("Retroceder")
        pin.pwm_b.start(self.velocidad)
        pin.pwm_a.start(self.velocidad)
        gpio.output(pin.motor_a_pin1,gpio.HIGH)
        #gpio.output(motor_a_pin1,gpio.LOW)  
        gpio.output(pin.motor_b_pin1,gpio.HIGH)
        #gpio.output(motor_b_pin1,gpio.LOW)
    def Derecha(self):
        print("Girar Derecha")
        pin.pwm_a.start(self.velocidad)
        pin.pwm_b.start(self.velocidad)
        gpio.output(pin.motor_a_pin1,gpio.HIGH)
        gpio.output(pin.motor_b_pin2,gpio.HIGH)

    def Izquierda(self):
        print("Girar izquierda")
        pin.pwm_b.start(self.velocidad) 
        pin.pwm_a.start(self.velocidad)
        gpio.output(pin.motor_b_pin1,gpio.HIGH)
        gpio.output(pin.motor_a_pin2,gpio.HIGH)
        
    def EncenderLed(self):
        gpio.output(5,gpio.HIGH)
        gpio.output(6,gpio.HIGH)
        gpio.output(13,gpio.HIGH)
        sleep(3)
        gpio.output(5,gpio.LOW)
        gpio.output(6,gpio.LOW)
        gpio.output(13,gpio.LOW)

