import numpy as np #numpy ocupa menos memoria para trabajar con matrices y listas
import sys
import time


a= np.array([1,2,3])
print('1D array')
print(a)
print()

b= np.array([(1,2,3),(4,5,6)])
print('2D array')
print(b)
print()


#Creamos matriz donde todos los valores son unos
ones=np.ones((5,5))
print('Ones array')
print(ones)
print()

zeros=np.zeros((3,4)) # ([fila,columna])
print('Zeros array')
print(zeros)
print()

aleatorios = np.random.random([4,3])
print('Random array')
print(aleatorios)
print()

vacia = np.empty((4,3))
print('Empty array')
print(vacia)
print()

unValor = np.full((2,4),7)
print('Un solo valor')
print(unValor)
print()

#matriz con valores espaciados uniformemente
espaciado_1=np.arange(0,30,5)
print('Matriz espaciado de a 5')
print(espaciado_1)
print()

espaciado_2=np.linspace(0,2,5)
print('Matriz espaciado de a 0.5')
print(espaciado_2)
print()

#Crear matriz identidad con funcion eye
identidad_1=np.eye(4,4)
print('Matriz identidad')
print(identidad_1)
print()
#creando matriz identidad usando identity
identidad_2=np.identity(4)
print('Matriz identidad')
print(identidad_2)
print()

#conocer las dimensiones de la matriz
a=np.array([(1,2,3),(4,5,6)])
print('Matriz A')
print(a)
print('Dimension de matriz A')
print(a.ndim)
print()

#Conocer el tipo de datos almacenados en una matriz
tipo=np.array([(1,2,3)])
print('Tipo de dato almacenado:')
print(tipo.dtype)
print()

#Conocer el tamaño y la forma de la matriz
print(a)
print('Tamaño matriz:')
print(a.size)
print('Forma matriz:')
print(a.shape)
print()

#cambiar de forma y tamaño una matriz
r=np.array([(8,9,10),(11,12,13)])
print('Forma original:')
print(r)
print()
print('Cambio de forma')
r=r.reshape(3,2)
print(r)
print()
#Extraer un solo elmento de la matriz en una ubicación
print('Elemento en la posicion (0,2)')
print(r[0,1])
print()

#Extraer los valores de todas la filas ubicadas en la comuna 2
res= np.array([(1,2,3),(4,5,6),(7,8,9)])
print(res)
print('Valores de todas las filas en la columna 2:')
print(res[0:,2]) #desde la fila cero
print()


# OPERACioNES MATEMÁTICAS ENTRE MATRICES
#encontrar valor máximo o mínimo

ab= np.array([(2,4,8)])
print(ab)
print('Valor mínimo:')
print(ab.min())
print('Valor máximo:')
print(ab.max())
print('Suma:')
print(ab.sum())
print()

#Calcular la raíz cuadrada y la desviación estandar

ra=np.array([(1,2,3),(3,4,5)])
print(ra)
print('Raiz cuadrada:')
print(np.sqrt(ra))
print('Desviación estándar:')
print(np.std(ra))
print()

#suma, resta , división y multiplicacion de dos matrices

x=np.array([(1,2,3),(4,5,6)])
y=np.array([(1,2,3),(4,5,6)])
print('Suma')
print(x+y)
print('Resta')
print(x-y)
print('Multiplicación')
print(x*y)
print('División')
print(x/y)





print('-------------------------------------------------------------')
print('Ejemplo de porqué numpy utiliza menos memoria que lista de python')
S = range(1000)
print('Resultado memoria asignada para lista de Python:')
print(sys.getsizeof(5)*len(S))
print()

D= np.arange(1000)
print('Resultado de memoria asignada para Numpy array:')
print(D.size*D.itemsize)

#Esto hace que las matrices creadas con numpy sea la opcion preferida


#Evaluamos la rapidez del tiempo de ejecucion de cada ejemplo 

SIZE = 1000000

L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2= np.arange(SIZE)

start= time.time()
result= [(x,y) for x,y in zip(L1,L2)]
print ('Resultado lista de python:' )
print((time.time()- start)*1000)
print()
start=time.time()
result=A1+A2
print ('Resultado NumPy array: ')
print((time.time()- start)*1000)

#por lo tanto las matrices creadas con Numpy son mucho mas rapidas que la listas creadas con pyton