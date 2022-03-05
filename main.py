from flask import Flask, render_template
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '',
    port=3306,
    database='productos'    
)
db.autocommit = True

app = Flask(__name__)

@app.get("/")

def inicio():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("select * from productos")
    productos = cursor.fetchall()  #obtener todo
    #producto = cursor.fetchone() obtener 1 solo registro
    #print(productos[5]['nombre']) imprime poker de la base de datos
    
    cursor.close()
    return render_template("index.html", productos=productos)

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<contactoId>")
def editarContacto(contactoId):
    return render_template("editarContacto.html", contactoId = contactoId)

@app.get("/edad/<int:edadId>")
def nacimiento(edadId):
    return render_template("edad.html", edadId = edadId)

app.run(debug=True)
