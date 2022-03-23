from browser import document
from Vlasbot import Robot

print("Dentro del script de python")

def avanzar(evento):
    print("avanzando...")
    Ejemplo.Hola()
    miRobot.Avanzar()

def stop(evento):
    print("Stop..")
    miRobot.Stop()

document["btn-avanzar"].bind("click", avanzar)
document["btn-stop"].bind('click',stop) 