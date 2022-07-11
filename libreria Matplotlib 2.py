import matplotlib.pyplot as plt

#diagrama de linea
#definir los datos
x1= [3,4,5,6] 
y1= [5,6,3,4]
x2= [2,5,8]
y2= [3,4,3]

#configurar caracteristicas del grafico

plt.plot(x1,y1,label = 'Linea 1', linewidth = 4, color = 'blue')
plt.plot(x2,y2,label = 'Linea 2', linewidth = 4, color = 'green')

#definir título y nombres de ejes
plt.title('Diagrama de líneas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#mostrar leyenda, cuadrícula y figura
plt.legend()
plt.grid()
plt.show()

#Gráficos de barra

#definir los datos
x1= [0.25,1.25,2.25,3.25,4.25] 
y1= [10,55,80,32,40]
x2= [0.75,1.75,2.75,3.75,4.75]
y2= [42,26,10,29,66]

#configurar caracteristicas del grafico

plt.bar(x1,y1,label = 'Datos 1', width = 0.5, color = 'Lightblue')
plt.bar(x2,y2,label = 'Datos 2', width = 0.5, color = 'orange')

#definir título y nombres de ejes
plt.title('Gráficos de barra')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#mostrar leyenda,  y figura
plt.legend()

plt.show()

#Histograma _ útiles para matrices o una lista muy larga

#Definir los datos
a = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
#Configurar las características del gráfico
plt.hist(a, bins, histtype = 'bar', rwidth = 0.8, color = 'lightgreen')
#Definir título y nombres de ejes
plt.title('Histograma')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar figura
plt.show()

#Gráficos de dispersión: se utilizan para comparar varaibles

#Definir los datos
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10, 55, 80, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]
#Configurar las características del gráfico
plt.scatter(x1, y1, label = 'Datos 1',color = 'red')
plt.scatter(x2, y2,label = 'Datos 2', color = 'purple')
#Definir título y nombres de ejes
plt.title('Gráfico de dispersión')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
#Mostrar leyenda y figura
plt.legend()
plt.show()

#Gráfico circular:

#Definir los datos
dormir =[7,8,6,11,7]
comer = [2,3,4,3,2]
trabajar =[7,8,7,2,2]
recreación = [8,5,7,8,13]
divisiones = [7,2,2,13]
actividades = ['Dormir','Comer','Trabajar','Recreación']
colores = ['red','purple','blue','orange']
#Configurar las características del gráfico
plt.pie(divisiones, labels=actividades, colors=colores, startangle=90, shadow=True, explode=(0.1,0,0,0), autopct='%1.1f%%')
#Definir título
plt.title('Gráfico circular')
#Mostrar figura
plt.show()

