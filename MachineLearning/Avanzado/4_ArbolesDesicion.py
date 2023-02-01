import pandas as pd
import matplotlib.pyplot as plt
#entropia
from scipy.stats import entropy
from math import log
#entropia

#entrenamineto
from sklearn.model_selection import train_test_split
#arbol
from sklearn import tree

pacientes = pd.read_csv("Datos/pacientes.csv")

#separacion
saludables = pacientes[pacientes["problema_cardiaco"]==0]
cardiacos = pacientes[pacientes["problema_cardiaco"]==1]

plt.figure(figsize=(6, 6))
plt.xlabel('Edad', fontsize = 20.0)
plt.ylabel('Colesterol', fontsize = 20.0)
plt.scatter(saludables["edad"], saludables["colesterol"],
            label="Saludable (Clase: 0)", marker="*", c="skyblue", s=200)
plt.scatter(cardiacos["edad"], cardiacos["colesterol"],
            label="Cardíaco (Clase: 1)", marker="*", c="lightcoral", s=200)
plt.legend(bbox_to_anchor=(1, 0.15))
#plt.show()

"""
edades = pd.Series([40, 30, 20, 50])
colesterol = pd.Series([100, 110, 100, 110])
print(edades.value_counts()/edades.size)
print(colesterol.value_counts()/colesterol.size)
print(entropy(edades.value_counts()/edades.size, base=2))
print(entropy(colesterol.value_counts()/colesterol.size, base=2))
"""


#creando arbol de desicion
#Entrenamiento
datos_entrena, datos_prueba, clase_entrena, clase_prueba = train_test_split(
    pacientes[["edad", "colesterol"]],
    pacientes["problema_cardiaco"],
    test_size=0.30) #30%

arbol_decision = tree.DecisionTreeClassifier(criterion="entropy",
                                             max_depth=2
                                             )

arbol = arbol_decision.fit(datos_entrena, clase_entrena) ##aprendizaje de maquina

accuracy = arbol_decision.score(datos_prueba, clase_prueba) #que tan bueno fue 

print(accuracy)

print(tree.export_text(arbol,
                      feature_names=["Edad", "Colesterol"]))
plt.figure(figsize=(12, 6))
tree.plot_tree(arbol,
              feature_names=["Edad", "Colesterol"])
plt.show()

print("Nuevo paciente", arbol_decision.predict([[70, 150]]))#70 años, 150 colesterol