import pandas as pd
from sklearn.model_selection import train_test_split #separacion de datos y prueba

pacientes = pd.read_csv("Datos/problemas_del_corazon.csv")
print(pacientes)

#%60%Entrenamiento, 20% Validacion, 20% Prueba
resto, prueba, resto_clase, prueba_clase = train_test_split(
    pacientes[["edad", "genero", "presion", "colesterol", "diabetico"]], #columnas para entrenar
    pacientes["cardiaco"], #clase
    test_size=0.20) #validacion
print(resto)

entrena, valida, entrena_clase, valida_clase = train_test_split(
    resto[["edad", "genero", "presion", "colesterol", "diabetico"]],
    resto_clase,
    test_size=0.25)

pacientes[pacientes["cardiaco"]==1]

print(pacientes)