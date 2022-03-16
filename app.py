"""
----------------------------------------------------------    
    Interfaz gráfica para controlar al robot Vlasbot V1
    Creado por: Vladimir Guajardo 
    Fecha de creación: Febrero - marzo 2022
----------------------------------------------------------  
"""

from flask import Flask, render_template, Response, request 
from Vlasbot import Robot
from camera import VideoCamera
import threading
import os

pi_camera = VideoCamera(flip=False) # voltear la cámara pi si está al revés.

# Se crea la App
server = Flask("__name__")
# Se crea la ruta por defecto
@server.route('/')
# Método de la ruta anterior
def home():
    return render_template('index.html')

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@server.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@server.route('/led/')
def led():
    print("Encendiendo el LED")
    miRobot.EncenderLed()
    return render_template('index.html')

@server.route("/avanzar/", methods=['POST'])
def avanzar():
    print("Moviendo primera funcion")
    miRobot.Avanzar()
    return render_template('index.html')

@server.route("/retroceder/", methods=['POST'])
def retroceder():
    print("retrocediendo primera funcion")
    miRobot.Retroceder()
    return render_template('index.html')

@server.route("/derecha/", methods=['POST'])
def derecha():
    print("Moviendo Derecha")
    miRobot.Derecha()
    return render_template('index.html')

@server.route("/izquierda/", methods=['POST'])
def izquierda():
    print("Moviendo Izquierda")
    miRobot.Izquierda()
    return render_template('index.html')

@server.route("/stop/", methods=['POST']) # STOP
def stop():
    print("Stop")
    miRobot.Stop()
    return render_template('index.html')

@server.route("/led/", methods=['POST']) # Encender Led
def Encender_Led():
    miRobot.EncenderLed()
    return render_template('index.html')


# Principal 
if __name__=='__main__':
    
    miRobot=Robot()
    server.run(debug=False, host='192.168.1.149')
    #server.run(host='192.168.1.149')
    
    
