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
	
def updateProducts(update_field, update_value, update_check):
	conn = sqlite3.connect('db_inventario.db')
	cursor = conn.cursor()
	query = f'''UPDATE productos SET "{update_field}" = "{update_value}" WHERE id = "{update_check}"'''
	cursor.execute(query)
	conn.commit()
	conn.close()
	
def deleteProducts(delete_id):
	conn = sqlite3.connect('db_inventario.db')
	cursor = conn.cursor()
	query = f'''DELETE FROM productos WHERE id = "{delete_id}"'''
	cursor.execute(query)
	conn.commit()
	conn.close()
	
def searchProducts(search_field, search_value):
	conn = sqlite3.connect('db_inventario.db')
	cursor = conn.cursor()
	query = f'''SELECT * FROM productos WHERE '{search_field}' = "{search_value}"'''
	cursor.execute(query)
	results = cursor.fetchall()
	conn.close()
	return(results)
	
def checkNumerical(value):
	flagError = True
	while flagError == True:
		try:
			value = int(value)
			flagError = False
			return(value)
		except ValueError:
			print('La opción ingresada no es válida, intente nuevamente: ')
			value = displayMenu()
#%--------------------------------------
#Inicio
print('%'*5, '-'*5,
'Te damos la bienvenida al sistema de gestión de inventario'.title(),
'-' * 5, '%' * 5 + '\n')
initializeTable()

option = checkNumerical(displayMenu())
#verificar opción válida
#%--------------------------------------
while option != 7 & (0 < option < 7) == True:
	#%----------------
	if option == 1:
		listProducts = readProducts()
		if len(listProducts) == 0:
			print('La lista de productos se encuentra vacía.')
			option = checkNumerical(displayMenu())
		else:
			print(listProducts)
			option = checkNumerical(displayMenu())
	#%----------------
	elif option == 2:
		marca = input('Marca comercial del producto: ')
		nombreGenerico = input('Nombre genérico del producto: ')
		descripcion = input('Decripción y especificaciones del producto: ')
		rubro = input('Rubro: ')
		estante = input('Nº de estante de reposición (dejar vacío de ser necesario): ')
		cantidad = input('Cantidad en stock: ')
		precio = input('Precio por unidad (dejar vacío de ser necesario): ')
		proveedor = input('Proveedor/es (dejar vacío de ser necesario): ')
		createProducts(marca, nombreGenerico, descripcion, rubro, estante, cantidad, precio, proveedor)
		print('El producto se añadió correctamente')
	#%----------------
	elif option == 3:
		update_check = input('ID del producto a modificar: ')
		update_field = input('Campo a modificar: ')
		update_value = input('Nuevo valor: ')
		updateProducts(update_field, update_value, update_check)
	#%----------------
	elif option == 4:
		delete_id = input('ID del producto a eliminar: ')
		deleteProducts(delete_id)
	#%----------------
	elif option == 5:
		search_field = input('Campo de entrada: ')
		search_value = input('Valor de busqueda: ')
		searchProducts(search_field, search_value)
	#%----------------
	elif option == 6:
		print('\n' + '-' * 80,
		'\n-> Las opciones de eliminar y actualizar productos requieren conocer de antemano la ID del producto en inventario',
		'\n-> El nombre genérico de producto refiere a la especie, por ejemplo: taladro, leche en polvo, mesa, etc.',
		'\n-> El precio se debe expresar en pesos argentinos (ARS)',
		'\n-> Para recibir asistencia personalizada consulte con su administrador o complete un reporte en:',
		'https://github.com/gnuido/Proyecto-Integrador/issues')
	#%----------------
	else:
		indiceError = 0		
		#contador de intentos inválidos
		if indiceError < 3:
			print('Opción inválida, por favor, intente nuevamente')
			indiceError += 1
		else:
			print('El valor que ingresado no es válido.',
			'Por favor, ingrese únicamente el dìgito correspondiente a la opción')
			indiceError = 0
#%----------------
else:
		print('Finalizando...',
		'\n%' + '-' * 82)
#%--------------------------------------
#fin
