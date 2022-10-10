import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pais 1
#x = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
#y = [45, 46, 47, 48, 50, 51, 52]

#grafica 1 sencilla
#plt.plot(x,y)
#plt.show()

#grafica 1 personalizada 1
#plt.plot(x, y, marker='o')
#plt.show()

#grafica 1 personalizada 2
#plt.plot(x, y, marker='o', linestyle='--')
#plt.show()

#grafica 1 personalizada 3
#plt.plot(x, y, marker='o', linestyle='--', color='r')
#plt.show()

#grafica 1 personalizada 4
#plt.figure(figsize=(10, 6)) #cambia el tamaño de la fig
#plt.plot(x, y, marker='o', linestyle='--')
#plt.xlabel('Años') #agrega label eje x
#plt.ylabel('Poblacion') #agrega label eje y
#plt.title('Población reflejada en años') #agrega titulo
#plt.yticks([45, 48, 51]) #solo muestra estos valores en el eje y
#plt.show()

#pais 2
#x2 = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
#y2 = [40, 41, 42, 50, 44, 45, 45]

#grafica 2 perzonalizada 1
#agrega una nueva linea
#plt.plot(x, y, marker='o', linestyle='--', color='g', label='Mexico')
#plt.plot(x2, y2, marker='o', linestyle='--', color='r', label='Francia')
#plt.xlabel('Años') #agrega label eje x
#plt.ylabel('Poblacion') #agrega label eje y
#plt.title('Población reflejada en años') #agrega titulo
#plt.yticks([45, 48, 51]) #solo muestra estos valores en el eje y
#plt.legend(loc='lower right') #muestra el nombre de cada linea y tambien especifica su posicion
#plt.savefig('Grafica.png') #para guardar el documento
#plt.show()

#barra 1
#x = ['Argentina', 'Alemania', 'Mexico', 'USA', 'Francia']
#y = [49, 68, 129, 240, 50]

#plt.bar(x, y)
#plt.show()

#picharts 1
#x = ['Argentina', 'Alemania', 'Mexico', 'USA', 'Francia']
# = [49, 68, 129, 240, 50]
#plt.pie(y, labels=x)
#plt.show()

#hitogramas 1
#data = np.random.RandomState(0).randn(400) #llenado
#(counts, bins, patches) = plt.hist(data)
#labels
#plt.xlabel("Datos")
#plt.ylabel("Eventos")
#plt.show()

#boxplots 1
#plt.boxplot(data)
#plt.show()

#Scatterplot 1
#relacion entre dos variables
#a = [1,3,5,2,6,4,6,3,7,9]
#b = [8,4,2,5,7,2,8,9,2,6]

#plt.scatter(a, b)
#plt.show()

#Subplots 1
x = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
y = [45, 46, 47, 48, 50, 51, 52]

x2 = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
y2 = [40, 41, 42, 50, 44, 45, 45]
fig, ax = plt.subplots(1, 2, sharey=True) #figura
ax[0].plot(x, y, color='r', label='Mexico')#valores primer subplot
ax[0].legend()
ax[1].plot(x2, y2, color='g', label='Francia')#valores segundo subplot
ax[1].legend()

plt.show()