from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def inicio():
    return render_template("index.html")

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
