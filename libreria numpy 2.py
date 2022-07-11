import numpy as np

#Creacion de matrices 

#Crear una matriz donde todos los valoes sean unos
print('Matriz de unos')
unos = np.ones((3,4)) #matriz de 3 filas , 4 columnas
print(unos)
print()

#Crear una matriz donde todos los valoes sean ceros
print('Matriz de ceros')
ceros = np.zeros((3,3)) #matriz de 3 filas , 3 columnas
print(ceros)
print()

#Crear una matriz con numeros aleatorios
print('Matriz de aleatorios')
aleatorios = np.random.random((3,3)) #matriz de 3 filas , 3 columnas
print(aleatorios)
print()

#Crear una matriz vacia
print('Matriz vacia')
vacia = np.empty((3,2)) #matriz de 3 filas , 2 columnas
print(vacia)
print()

#Crear una matriz de un valor en todas las posiciones
print('Matriz de un solo valor')
full = np.full((3,3),9) #matriz de 3 filas , 3 columnas
print(full)
print()

#Crear una matriz con valores espaciados
print('Matriz espaciada')
espacio1 = np.arange(0,30,5) #comienza en 0 hasta 5 valores 
print(espacio1)
espacio2 = np.linspace(0,2,5) #comienza en 0 y llena con 5 valores hasta llegar a 2
print(espacio2)
print()

#crear un matriz identidad
print('Matriz identidad')
identidad1 = np.eye(4,4) 
print(identidad1)
print()

# inspeccion de las matrices creadas con NumPy

#conocer las dimensiones de una matriz
print('Dimension de matriz')
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print()

#conocer el tipo de dato almacenado en una matriz
print('Tipo de dato de matriz')
a=np.array([(1,2,3)])
print(a.dtype)
print()

#conocer el tamaño y forma de una matriz
print('Tamaño y forma de una matriz')
a=np.array([(1,2,3,4,5,6,7,8,9)])
print(a.size)
print(a.shape)
print()

#Cambiar el tamaño y forma de una matriz
print('Cambiar tamaño y forma de una matriz')
a=np.array([(8,9,10),(11,12,13)])
print(a)
a=a.reshape(3,2)
print(a)
print()

#Seleccionar un solo elemento de la matriz
print('Seleccion de un elemento de matriz')
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0,2])
print()

#Seleccionar los valores de todas las filas ubicadas en la comuna 3 de la matriz
print('Seleccion de elementos columna 3 de matriz')
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print(a[0:,2]) #los dos puntos significan "toda la fila"
print()

#Operaciones matematicas entre matrices

#Encontrar el minimo, maximo y la suma

print('Mínimo, máximo y suma de una matriz')
a=np.array([(1,2,3,4,5,6,7,8,9)])
print(a.min())
print(a.max())
print(a.sum())
print()

# Calcular la raiz cuadrada y la desviación estándar de la matriz
print(' Raiz cuadrada y la desviación estándar de matriz')
a=np.array([(1,2,3,4),(3,4,5,6)])
print(np.sqrt(a))
print(np.std(a))
print()

#Suma , resta, multiplicacion y division de dos matrices

print('Suma, resta, mult, y division de dos matrices')
x=np.array([(1,2,3,4),(3,4,5,6)])
y=np.array([(1,2,3,4),(3,4,5,6)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print()
