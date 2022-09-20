"""
Un dictionnaire est une collection nonordonnée d'éléments"""
diccionario = {
    'prenom':'Luis',
    'age':23
}
print(diccionario)
print(diccionario['prenom']) #imprime conforme a la clave

datos_personales = {
    'pays' : 'Mexique',
    'ville' : 'Puebla'
}
print(datos_personales)
datos_personales['ville'] = 'Cholula' #changer le valeur du champ
print(datos_personales)

dict = {
    'luis' : 23,
    'david' : 21,
    'camille' : 19,
    'marie': 24
}

dict.update({'joh': 23}) #ajouter un nouveau champ
print(dict)

del dict['david'] #retirer un champ
print(dict)
hommes={'luis':23,'david':21}
femmes={'camille':19, 'marie':24}
etudiants = list(dict.keys())
etudiants.sort() #trier le valeurs
print(etudiants)

for e in etudiants:
    print(" : ".join((e,str(dict[e])))) #répéter le cicle