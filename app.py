from flask import Flask, render_template
from Vlasbot import Robot
# Se crea el objeto
server=Flask("__name__")
# Se crea la ruta por defecto
@server.route('/')
# Método de la ruta anterior
def home():
    return render_template('index.html')

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
    server.run(debug=True, host='0.0.0.0')
    #server.run(host='192.168.1.149')
    
    
