# libreria para presentar los datos
#utilizada para graficos 2d

import matplotlib.pyplot as plt

a=[1,2,3,4]
b=[11,22,33,44]

plt.plot(a,b,color='blue', linewidth=3, label='Línea')
plt.legend()
plt.show()

#la figura es la ventana o pagina gral en la que se dibuja todo
#la figura puede contener multiples ejes

# matplotlib es todo el paquete de visualizacion de datos de python
# pyplot es un modilo del paquete mtplotlib
#para graficar con matplotlib deben estar los datos estructurados en numpy
