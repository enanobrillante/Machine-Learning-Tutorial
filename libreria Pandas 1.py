import pandas as pd
import numpy as np

#crear un data frame es lo primero en un proyecto de machine learning en python

data = np.array([['','Col1','Col2'],['Fila1',11,22],['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))
print()
 
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]])) #crea una matriz de 3 x 3 con sus indices
print('Dataframe: ')
print(df)
print()


#el primer indice de la serie es 0
series = pd.Series({"Argentina":"Buenos Aires","Chile":"Santiago de Chile","Colombia":"Bogotá","España":"MAdrid"})
print('Series:')
print(series)


#Forma del DataFrame

print('Forma del DataFrame:')
print(df.shape)

#Altura del DataFrame

print('Altura del DataFrame:')
print(len(df.index))

#Estadisticas del DataFrame para columnas numericas
print('Estadisticas del DataFrame:')
print(df.describe())

#Media de las columnas DataFrame
print('Media de las columnas DataFrame:')
print(df.mean())

#Correlacion entre columnas
print('Correlacion entre columnas:')
print(df.corr())

#Cuenta los datos del data frame
#numeros de valores no nulos por columna

print('numeros de valores no nulos:')
print(df.count())

#Valor mas alto en cada columna
print('Valor mas alto en cada columna:')
print(df.max())
#print(df.min()) para saber el minimo

#mediana de cada coluna
print('Mediana de cada columna:')
print(df.median())

#Desviación estándar de cada columna
print('Desviación estándar de cada columna:')
print(df.std())

#Seleccionar la primera columna del DataFrame
print('Valores de la Primer fila del data frame:')
print(df.loc[0])

#Seleccionar los valores de la primer fila del DataFrame
print('Primer columna del data frame:')
print(df[0])

#Seleccionar varias columnas del DataFrame
print('Columna 1 y 3 del data frame:')
print(df[[0,2]])

#Seleccionar un valor usando los indices fila y columna del DataFrame
print('Seleccion de un valor, posicion [0,2]:')
print(df.iloc[0][2])

# Importando datos :se puede hacer desde un archivo local
#o desde una base de datos de un sitio web a traves de una URL

#df = pd.read_csv('train.csv')

#limpiar nuestros datos
#Verificar si hay dato snulos en el DataFrame

print('Datos nulos:')
print(df.isnull())

#suma de valores nulos
print('Suma de datos nulos:')
print(df.isnull().sum())

#luego de obtener una lista de valores nulos nos podremos deshacer de ellos
#o rellenar los valores

#pd.dropna() elimina las filas con datos perdidos
#df.dropna(axis=1) elimina las columnas con datos perdidos

#Se pueden rellenar los valores perdidos con otros valores
print('Reemplazar los valores perdidos por la media con X:')
print(df.fillna(df.mean())) #en este caso se reemplazan con la media de los datos







