import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

datos = pd.read_csv(".ipynb_checkpoints/Datos/ingreso.csv")
datos

plt.ylabel("Ingreso ($)")
plt.xlabel("Promedio de horas semanales trabajadas")
plt.scatter(datos["horas"], datos["ingreso"], color="pink")
#plt.show()

regresion = linear_model.LinearRegression()

horas = datos["horas"].values.reshape((-1, 1))

modelo = regresion.fit(horas, datos["ingreso"])

print("Intersección (b)", modelo.intercept_)
print("Pendiente (m)", modelo.coef_)

entrada = [[39.5], [40], [43], [43.5]] #calculo de salario para personas que trabajan n horas
modelo.predict(entrada)

"""
Para cada hora trabajada, el salario aumenta 3965
"""
plt.scatter(entrada, modelo.predict(entrada), color="red")
plt.plot(entrada, modelo.predict(entrada), color="black")

plt.ylabel("Ingreso ($)")
plt.xlabel("Promedio de horas semanales trabajadas")
plt.scatter(datos["horas"], datos["ingreso"], color="pink", alpha=0.55)
plt.show()
