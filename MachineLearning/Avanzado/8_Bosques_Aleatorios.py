import pandas as pd 
from random import sample
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn import tree



personas = pd.read_csv("Datos/ingresos.csv")


#arboles
"""print(personas.sample(frac=2/3, replace=True))
print(personas.sample(frac=2/3, replace=True))
print(personas.sample(frac=2/3, replace=True))
print(personas.sample(frac=2/3, replace=True))
print(personas.sample(frac=2/3, replace=True))"""



print(personas.columns[:-1], "\n") #-1 ignora la columna ingreso
print(sample(set(personas.columns[:-1]), 3)) #se eligen tres columnas al azar (no se recomienda escoger todas)


#generando bosque
bosque = RandomForestClassifier(n_estimators=100, #numero de arboles
                               criterion="gini", #hay dos criterios (gini y entripia)
                               max_features="sqrt", #
                               bootstrap=True, #necesita estar habilitado
                               max_samples=2/3, #porcentaje para muestrear
                               oob_score=True) #metrica especial para bosques aleatorios

bosque.fit(personas[personas.columns[:-1]].values, personas["ingreso"].values) #pasamoslas columanas y la clase

#Calcular la eficiencia del modelo
print(bosque.predict([[50, 16, 1, 1, 40]])) #pasamos una lista de listas con valores (edad, estudio, genero, tipo_trabajo, horas) que clasificara con ingreso
print(bosque.score(personas[personas.columns[:-1]].values, personas["ingreso"].values)) #evauluacion por medio de los datos que se le dieron
print(bosque.oob_score_) #intanceas que quedaron fuera

#inprimiendo todos los arboles
for arbol in bosque.estimators_:
    tree.plot_tree(arbol, feature_names=personas.columns[:-1])
    plt.show()