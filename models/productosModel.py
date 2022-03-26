from config.database import db

def obtenerProductos():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("select * from productos")
    productos = cursor.fetchall()  #obtener todo
    #producto = cursor.fetchone() obtener 1 solo registro
    #print(productos[5]['nombre']) imprime poker de la base de datos
    
    cursor.close()
    return productos

def crearProducto(nombre, price):
     #insertar datos a la base de datos
    cursor = db.cursor()
    
    cursor.execute("insert into productos(nombre, price) values(%s,%s)", (
        nombre,
        price,
    ))
    cursor.close()
    
    