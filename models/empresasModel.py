from config.database import db

def obtenerProductos():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("select * from empresas")
    empresas = cursor.fetchall()  #obtener todo
    #producto = cursor.fetchone() obtener 1 solo registro
    #print(productos[5]['nombre']) imprime poker de la base de datos
    
    cursor.close()
    return empresas

def obtenerCorreo():
    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from empresas")
    #empresas = cursor.fetchall()  #obtener todo
    correo = cursor.fetchone() #obtener 1 solo registro
    #print(productos[5]['nombre']) imprime poker de la base de datos
    
    cursor.close()
    return correo

def obtenerClave():
    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from empresas")
    #empresas = cursor.fetchall()  #obtener todo
    clave = cursor.fetchone() #obtener 1 solo registro
    #print(productos[5]['nombre']) imprime poker de la base de datos
    
    cursor.close()
    return clave

def registrar(nombre, contacto, direccion, correo, clave):
     #insertar datos a la base de datos
    cursor = db.cursor()   
    cursor.execute("insert into empresas(nombre, contacto, direccion, correo, clave) values(%s,%s,%s,%s,%s)", (
        nombre,
        contacto,
        direccion,
        correo,
        clave,
    ))
    cursor.close()
    
def eliminarEmpresa(id):
    cursor=db.cursor()
    cursor.execute("DELETE FROM empresas WHERE id = {0}".format(id))
    db.commit()  
    cursor.close