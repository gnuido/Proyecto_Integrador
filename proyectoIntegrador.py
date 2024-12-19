#main.py

#importar módulos a utilizar
import sqlite3

#%--------------------------------------
def initializeTable():
	#verificar la existencia de tablas y generar base de datos / tabla en su defecto
	conn = sqlite3.connect('db_inventario.db')	#establecer conexión con la base de datos asignada
	cursor = conn.cursor()	#generar cursor para manipular la base de datos enlazada
	query = '''CREATE TABLE IF NOT EXISTS 'productos' (
			'id' INTEGER NOT NULL UNIQUE,
			'marca' TEXT NOT NULL,
			'nombre_generico' TEXT NOT NULL,
			'descripcion' TEXT NOT NULL,
			'rubro' TEXT NOT NULL,
			'estante' INTEGER,
			'cantidad' INTEGER NOT NULL,
			'precio' REAL,
			'proveedor' TEXT,
			PRIMARY KEY('id' AUTOINCREMENT)
			);'''
	cursor.execute(query)	#verificar existencia o generar tabla con los campos indicados en la base de datos
	conn.commit()
	conn.close()

#%--------------------------------------
#definir funciones a implementar
def displayMenu():
	#mostrar menú de opciones
	print('Por favor, seleccione una de las siguientes opciones: ',
	'\n1> Mostar lista completa de productos.',
	'\n2> Agregar nuevo producto a la lista.',
	'\n3> Actualizar producto existente en la lista.',
	'\n4> Eliminar producto de la lista.',
	'\n5> Buscar producto en la lista.',
	'\n6> Ayuda/FAQ.',
	'\n7> Salir.')
	option = input()
	return(option)

def readProducts():
	#leer lista completa de productos
	conn = sqlite3.connect('db_inventario.db')
	cursor = conn.cursor()
	query = '''SELECT * FROM productos'''
	cursor.execute(query)	
	products = cursor.fetchall()
	conn.close()
	return(products)
	
def createProducts(marca, nombre_generico, descripcion, rubro, estante, cantidad, precio, proveedor):
	#crear nuevo registro
	conn = sqlite3.connect('db_inventario.db')
	cursor = conn.cursor()
	query = '''INSERT INTO productos (marca, nombre_generico, descripcion, rubro, estante, cantidad, precio, proveedor)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
	cursor.execute(query, (marca, nombre_generico, descripcion, rubro, estante, cantidad, precio, proveedor))
	conn.commit()
	conn.close()
	
def updateProducts():
	conn = sqlite3.connect('db_inventario.db')
	cursor = conn.cursor()
	query = ''''''
	cursor.execute()
	conn.commit()
	conn.close()
	
def deleteProducts(del_ID):
	conn = sqlite3.connect('db_inventario.db')
	cursor = conn.cursor()
	query = f'''DELETE FROM personas WHERE id = {del_ID}'''
	cursor.execute(query)
	conn.commit()
	conn.close()
	
def searchProducts(search_field, search_value):
	conn = sqlite3.connect('db_inventario.db')
	cursor = conn.cursor()
	query = f'''SELECT {search_field} FROM productos VALUE {search_value}'''
	cursor.execute(query)
	results = cursor.fetchall()
	conn.close()
	return(results)
#%--------------------------------------
#Inicio
print('%'*5, '-'*5,
'Te damos la bienvenida al sistema de gestión de inventario'.title(),
'-' * 5, '%' * 5 + '\n')
initializeTable()

option = displayMenu()

'''marca = 'Rucci'
nombre_generico = 'Llave Stilson'
descripcion = 'Llave Stilson tipo sueca, acero forjado'
rubro = 'Ferretería'
estante = 28
cantidad = 18
precio = 120500
proveedor = 'Rucci S.R.L.'
createProducts(marca, nombre_generico, descripcion, rubro, estante, cantidad, precio, proveedor)
'''
search_field = 'marca'
search_value = 'Rucci'
result = searchProducts(search_field, search_value)
print(result)
