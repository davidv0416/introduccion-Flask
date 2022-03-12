from flask import Flask, flash, render_template, request, redirect, url_for
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
app.secret_key = '*@SERVER0KEY_'

@app.get("/")

def inicio():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("select * from productos")
    productos = cursor.fetchall()  #obtener todo
    #producto = cursor.fetchone() obtener 1 solo registro
    #print(productos[5]['nombre']) imprime poker de la base de datos
    
    cursor.close()
    return render_template("index.html", productos=productos)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProducto.html")

@app.post("/form_crear")
def crearProducto():
    #recuperar datos del formulario
    nombre = request.form.get('nombre')
    price = request.form.get('price')
    
    is_valid = True
    
    if nombre == "":
        flash("El nombre es requerido")
        is_valid = False 
        
    if price == "":
        flash("El precio es requerido")
        is_valid = False
        
    if not price.isdigit():
        flash("El precio debe de ser un número")
        is_valid = False
    
    if is_valid == False:
        return render_template("crearProducto.html",
                nombre=nombre,
                price=price,
        )
    #insertar datos a la base de datos
    cursor = db.cursor()
    
    cursor.execute("insert into productos(nombre, price) values(%s,%s)", (
        nombre,
        price,
    ))
    cursor.close()
    
    return redirect(url_for('inicio'))

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

@app.route("/eliminar_producto/<string:id>")
def eliminarProducto(id):
  cursor=db.cursor()
  cursor.execute("DELETE FROM productos WHERE id = {0}".format(id))
  db.commit()
  return redirect(url_for("inicio"))

"""@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<contactoId>")
def editarContacto(contactoId):
    return render_template("editarContacto.html", contactoId = contactoId)

@app.get("/edad/<int:edadId>")
def nacimiento(edadId):
    return render_template("edad.html", edadId = edadId)"""

app.run(debug=True)
