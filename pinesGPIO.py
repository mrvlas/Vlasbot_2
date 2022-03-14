import RPi.GPIO as gpio

############### Configuración pines GPIO  #################

gpio.setwarnings(False)
#Configuración Modo pines GPIO 
gpio.setmode(gpio.BCM)
# Motor A
motor_a_en=4
motor_a_pin1=26
motor_a_pin2=21
# Motor B
motor_b_en=17
motor_b_pin1=27
motor_b_pin2=18
# Configuración como salida motor A
gpio.setup(motor_a_en, gpio.OUT)
gpio.setup(motor_a_pin1, gpio.OUT)
gpio.setup(motor_a_pin2, gpio.OUT)
# Configuración como salida motor B
gpio.setup(motor_b_en, gpio.OUT)
gpio.setup(motor_b_pin1, gpio.OUT)
gpio.setup(motor_b_pin2, gpio.OUT)
# Configuración de la velocidad
pwm_a=gpio.PWM(motor_a_en, 1000)
pwm_b=gpio.PWM(motor_b_en, 1000)
# Configuracion pin LED
gpio.setup(5,gpio.OUT)
gpio.setup(6,gpio.OUT)
gpio.setup(13,gpio.OUT)
# Configuración Ultrasonico

