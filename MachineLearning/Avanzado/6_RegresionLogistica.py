import numpy as np
import matplotlib.pyplot as plt
import math

# Creamos una función logística vectorial (ufuncs)
logistica = np.frompyfunc(lambda b0, b1, x:
                         1 / (1 + math.exp(-(b0 + b1*x))), #ecuacion
                         3, 1) #numero de parametros de labmda, un parametro de salida

# Graficamos la función logística
plt.figure(figsize=(8, 4))

# Diferentes pendientes (grafica de dispersion)
plt.scatter(np.arange(-5, 5, 0.1),
           logistica(0, 1, np.arange(-5, 5, 0.1)),
           color="green")

plt.scatter(np.arange(-5, 5, 0.1),
           logistica(0, 2, np.arange(-5, 5, 0.1)), #inclinacion
           color="gold")

plt.scatter(np.arange(-5, 5, 0.1),
           logistica(0, 3, np.arange(-5, 5, 0.1)),
           color="red")

plt.title("Función Logística Estándar - Diferentes 'Pendientes'", fontsize=14.0)
plt.ylabel("Probabilidad", fontsize=13.0)
plt.xlabel("Valores", fontsize=13.0)
#plt.show()


##Taquicardia porobablidad y clase
personas_normal = [65, 70, 80, 80, 80,
                   90, 95, 100, 105, 110]

personas_taquicardia = [105, 110, 110, 120, 120,
                        130, 140, 180, 185, 190]

# Graficamos una función logística
plt.figure(figsize=(6, 4))

# y = b0 + b1x
#
# y = -46.68057196 + 0.42460226x

plt.scatter(np.arange(60, 200, 0.1),
            logistica(-46.68057196, 0.42460226,
                      np.arange(60, 200, 0.1)))

# Graficamos la frecuencia cardíaca de las personas
plt.scatter(personas_normal, [0]*10,
            marker="o", c="green", s=250, label="Normal")
plt.scatter(personas_taquicardia, [1]*10,
            marker="o", c="red", s=250, label="Taquicardia")

# Graficamos las probabilidades para tres (3) individuos
individuos = [80, 110, 180]

probalidades = logistica(-46.68057196, 0.42460226, individuos)

plt.scatter(individuos, probalidades,
            marker="*", c="darkorange", s=500)

plt.text(individuos[0]+7, 0.05, "%0.2f" % probalidades[0],
         size=12, color="black")
plt.text(individuos[1]+7, 0.48, "%0.2f" % probalidades[1],
         size=12, color="black")
plt.text(individuos[2]+7, 0.90, "%0.2f" % probalidades[2],
         size=12, color="black")
plt.text(0, 1, "TAQUICARDIA", size=12, color="red")
plt.text(0, 0, "NORMAL", size=12, color="red")
plt.ylabel("Probabilidad de Taquicardia", fontsize=13.0)
plt.xlabel("Frecuencia cardíaca (latidos por minuto)", fontsize=13.0)
plt.legend(bbox_to_anchor=(1, 0.2))
plt.show()
