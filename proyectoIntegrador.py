#main.py

#importar módulos a utilizar
import sqlite3

#%--------------------------------------
#verificar existencia de tablas
def initializeTable():
	conn = sqlite3.connect('db_personas.db')	#establecer conexión con la base de datos asignada
	cursor = conn.cursor()	#generar cursor para manipular la base de datos enlazada
	query = '''CREATE TABLE IF NOT EXISTS 'productos' (
			'id' INTEGER NOT NULL UNIQUE,
			'marca' TEXT NOT NULL,
			'nombre' TEXT NOT NULL,
			'descripción' TEXT NOT NULL,
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

def readTable():
	#leer lista completa de productos
	
#%--------------------------------------
#Inicio
print('%'*5, '-'*5,
'Te damos la bienvenida al sistema de gestión de inventario'.title(),
'-'*5, '%'*5 + '\n')
initializeTable()

option = displayMenu()

	
