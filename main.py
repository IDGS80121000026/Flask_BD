from flask import Flask,render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig

#variables globales 

from flask import g

import forms


app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
#proceso de configuracion
csrf=CSRFProtect()
#por que queremos trabajar con ese

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos",methods=['GET','POST'])
def alumnos():
    print("alumno : {}".format(g.nombre))
    nom=""
    apa=''
    ama=''
    email=''
    edad=''
    
    
    alumno_clase= forms.UserForm(request.form)
    if request.method=='POST' and alumno_clase.validate():
        nom=alumno_clase.nombre.data
        apa=alumno_clase.apaterno.data
        ama=alumno_clase.amaterno.data
        email=alumno_clase.email.data
        edad=alumno_clase.edad.data
        
        
        print('Nombre: {}'.format(nom))
        print('Apaterno: {}'.format(apa))
        print('Amaterno: {}'.format(ama))
        
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos.html",form=alumno_clase,nom=nom,apa=apa,ama=ama)
    '''titulo="UTL!!!"
    nombres=["mario","pedro","juan","darios"]
    return render_template("alumnos.html",titulo=titulo,nombres=nombres)'''


if __name__=="__main__":
    csrf.init_app(app)
    
    app.run() 