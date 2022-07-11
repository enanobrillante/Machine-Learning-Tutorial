import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

########## Preparar la data ###########

boston = datasets.load_boston()
print(boston)
print()

# Entender la data

print('Información en el dataset:')
print(boston.keys())
print()

#ver las caracteristicas del dataset

print('Caracteristicas del dataset:')
print(boston.DESCR)

#var la cantidadde datos en el dataset

print('Cantidad de datos en el dataset:')
print(boston.data.shape)
print()

#ver las etiquetas de cada columna
print('Etiquetas de cada columna:')
print(boston.feature_names)

#Seleccionamos solo la columna numero 5, preparamos la data para la regresion lineal
x= boston.data[:,np.newaxis,5] #los datos se encuentran almacenados en numpy

# defino los datos correspondientes a las etiquetas
y = boston.target

#usamos una grafica de dispersion para graficar los datos

plt.scatter(x,y)
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()

# separar los datos de "train" en entrenamiento y prueba para probar los algoritmos
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
#se toman un 20 porciento de los datos para usarlos como prueba

#definimos el algoritmo a utilizar 
lr = linear_model.LinearRegression()

#Entrena el modelo

lr.fit(x_train,y_train)

#realizamos la prediccion utilizando los datos de prueba
y_pred = lr.predict(x_test)

plt.scatter( x_test,y_test)
plt.plot(x_test, y_pred, color='red',linewidth=3)
plt.title('Regresión lineal simple')
plt.ylabel('Valor medio')
plt.xlabel('Número de habitaciones')
plt.show()

#este algotimo no es bueno para este conjunto de datos

# para nver como queda la ecucion del modelo
print()
print('DATOS DEL MODELO REGRESION LINEAL SIMPLE')
print()
print('Valor de la pendiente o coeficiente "a"')
print(lr.coef_)
print()
print('Valor de la intersección o coeficiente "b"')
print(lr.intercept_)
print()
print('La ecuación del modelo es : ')
print('y = ', lr.coef_, 'x = ', lr.intercept_)

#Calculamos la presición del algortimo
print()
print('Presición del algortimo : ')
print(lr.score(x_train,y_train)) # score devuelve el resultado de la estadística R al cuadrado


