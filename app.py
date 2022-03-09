from flask import Flask, render_template, Response, request 
from Vlasbot import Robot
from camera import VideoCamera
import threading
import os

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.
 

# Se crea el objeto
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
 

@server.route("/avanzar/", methods=['POST'])
def avanzar():
    #Moving forward code
    #forward_message = "Moving Forward..."
    print("Moviendo primera funcion")
    miRobot.Avanzar()
    return render_template('index.html')#, forward_message=forward_message);

@server.route("/stop/", methods=['POST']) # STOP
def Retroceder():
    #Moving forward code
    #forward_message = "Moving Forward..."
    print("Stop")
    miRobot.Stop()
    return render_template('index.html')#, forward_message=forward_message);

@server.route("/led/", methods=['POST']) # Encender Led
def Encender_Led():
    miRobot.EncenderLed()
    return render_template('index.html')
    
# Principal 
if __name__=='__main__':
    
    miRobot=Robot()
    server.run(debug=False, host='0.0.0.0')
    #server.run(host='192.168.1.149')
    
    
