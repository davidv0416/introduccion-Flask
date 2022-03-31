from flask import Flask, flash, render_template, request, redirect, url_for
from models import empresasModel
import hashlib
from smtplib import SMTP
from email.message import EmailMessage
import re


app = Flask(__name__)
app.secret_key = '*@SERVER0KEY_'

@app.get("/")
def index():
    empresas = empresasModel.obtenerProductos()
    return render_template("index.html", empresas=empresas)

@app.get("/login")
def login():
    return render_template("login.html")

@app.route("/initSesion")
def initSesion():
    if request.method == 'GET':
        return render_template("login.html")
    correo = request.form.get('correo')
    clave = request.form.get('clave')
    clave = hashlib.sha1(clave.encode()).hexdigest()
    
    email = empresasModel.obtenerCorreo(correo)
    passw = empresasModel.obtenerClave(clave)
    
    if correo == email and clave == passw:
        return render_template("home.html")
    else:
        flash("Correo o clave incorrecta")

@app.route("/eliminar/<string:id>")
def eliminarEmpresa(id):
    empresasModel.eliminarEmpresa(id)
    return redirect(url_for("index"))
         
@app.get("/registro")
def registro():
    return render_template("registro.html")

@app.post("/registrar")
def registrar():
    #recuperar datos del formulario
    if request.method == 'GET':
        return render_template("registro.html")
    else:
        #recuperar datos del formulario
        nombre = request.form.get('nombre')
        contacto = request.form.get('contacto')
        direccion = request.form.get('direccion')
        correo = request.form.get('correo')
        clave = request.form.get('clave')
        
        
        
        is_valid = True
        if nombre == "":
            flash("El nombre es requerido")
            is_valid = False 
            
        if contacto == "":
            flash("El contacto es requerido")
            is_valid = False
            
        if not contacto.isdigit():
            flash("El contacto debe de ser un número")
            is_valid = False
        
        if direccion == "":
            flash("La direccion es requerida")
            is_valid = False
        
        if correo == "":
            flash("El correo es requerido")
            is_valid = False
        
        if clave == "":
            flash("La clave es requerida")
            is_valid = False
        
        if len(clave) < 8:
            flash("La clave debe tener mínimo 8 caracteres")
            is_valid = False
        
        if not re.search('[a-z]', clave):
            flash("La clave debe tener mínimo 1 letra minuscula")
            is_valid = False    
        
        if not re.search('[A-Z]', clave):
            flash("La clave debe tener mínimo 1 letra mayuscula")
            is_valid = False
        
        if not re.search('[0-9]', clave):
            flash("La clave debe tener mínimo 1 número")
            is_valid = False
        
        if not re.search('[.@_#$&]', clave):
            flash("La clave debe tener mínimo 1 caracter especial (.@_#$&)")
            is_valid = False    
            
        if is_valid == False:
            return render_template("registro.html",
                    nombre=nombre,
                    contacto=contacto,
                    direccion=direccion,
                    correo=correo,
                    clave=clave,
            )
        
        clave = hashlib.sha1(clave.encode()).hexdigest()
            
        msg = EmailMessage()
        msg.set_content('Su empresa ha sido registrada satisfactoriamente.')

        msg['Subject'] = 'Confirmación de registro'
        msg['From'] = "davidvivas2020@itp.edu.co"
        msg['To'] = correo

        username = 'davidvivas2020@itp.edu.co'
        password = '1085340013'

        server = SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.send_message(msg)

        server.quit()
        
        
        empresasModel.registrar(nombre=nombre, contacto=contacto, direccion=direccion, correo=correo, clave=clave)
        
        
        return redirect(url_for('index'))


"""
@app.route("/edit_producto/<id>")
def get_Producto(id):
  cursor=db.cursor()
  cursor.execute("SELECT * FROM productos WHERE id=%s", (id))
  datos=cursor.fetchall()
  print(datos[0])
  return render_template("editProducto.html", producto = datos[0])


@app.route("/actualizar_producto/<string:id>", methods=['POST'])
def actualizarProducto(id):
  if request.method=='POST':
    nombre=request.form['nombre']
    price=request.form['price']
    cursor=db.cursor()
    cursor.execute(nombre, price, id)
    db.connection.commit()
    return redirect(url_for('inicio'))


"""

app.run(debug=True)
