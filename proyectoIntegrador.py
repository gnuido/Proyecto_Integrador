#Importar módulos
import sqlite3

#%--------------------------------------

#Definir funciones
#Iniciar base de datos y tabla
def initializeInventory():
	conn = sqlite3.connect('inventario.db')
	cursor = conn.cursor()
	#definir query para ejecución
	query = '''CREATE TABLE IF NOT EXISTS "productos" (
		"id"	INTEGER NOT NULL UNIQUE,
		"nombre_fantasia"	TEXT NOT NULL,
		"marca"	TEXT NOT NULL,
		"rubro" TEXT,
		"estante" INTEGER,
		"cantidad"	INTEGER NOT NULL,
		"precio_lista"	REAL NOT NULL,
		"proveedor" TEXT,
		PRIMARY KEY("id" AUTOINCREMENT)
		);'''
	cursor.execute(query)
	conn.commit()
	conn.close()

#Mostrar lista completa
def displayProducts():
	conn = sqlite3.connect('inventario.db')
	cursor = conn.cursor()
	query = '''SELECT * FROM Productos'''
	cursor.execute(query)
	listProduct = cursor.fetchall()
	conn.close()

#Añadir registros
def addProducts(product):
	conn = sqlite3.connect('inventario.db')
	cursor = conn.cursor()
	query = '''INSERT INTO (id,
	nombre_fantasia,
	marca,
	rubro,
	estante,
	cantidad,
	precio_lista,
	proveedor) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
	cursor.execute(query,
	(product[0],
	product[1],
	product[2],
	product[3],
	product[4],
	product[5],
	product[6],
	product[7]))
	conn.commit()
	conn.close()

#Actualizar registros	
def updateProduct():
	conn = sqlite3.connect('inventario.db')
	cursor = conn.cursor()
	query = '''UPDATE Productos SET WHERE '''
	cursor.execute(query)
	conn.commit()
	conn.close()
	
#Eliminar Registros
def deleteProduct():
	conn = sqlite3.connect('inventario.db')
	cursor = conn.cursor()
	query = '''DELETE FROM'''
	cursor.execute(query)
	conn.commit()
	conn.close()
	
#Buscar registros
def searchProduct():
	conn = sqlite3.connect('inventario.db')
	cursor = conn.close()
	query = '''SELECT FROM '''
	cursor.execute(query)
	cursor.fetchall()
	conn.close()

#Configuración de notificaciones por bajo stock	
def notifyProduct(lowStockTreshold):
	conn = sqlite3.connect('inventario.db')
	cursor = conn.cursor()
	query '''SELECT cantidad FROM Productos WHERE '''

#Menú de opciones
def displayMenu():
	print('Por favor, seleccione una de las siguientes opciones: ',
	'\n1> Ver lista completa de producto',
	'\n2> Añadir producto a la lista',
	'\n3> Editar detalles de una producto',
	'\n4> Eliminar producto de la lista',
	'\n5> Buscar producto en la lista',
	'\n6> Ayuda/FAQ',
	'\n7> Finalizar')
	

#%--------------------------------------

#Invocar menú
print(f'%'*5, '-'*5, 'Te damos la bienvenida al sistema de gestión de inventario'.title(), '-'*5, '%'*5 + '\n')
displayMenu()
option = input()
while option == '':
	#Verificación de entrada vacía
	displayMenu()
	option = input()
