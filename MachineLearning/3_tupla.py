"""
est similaire à une liste, mais la différance
entre le deux est que nou ne pouvons pas changer les
éléments d'un tuple
"""

tupla = (0,1,2,3,4,5) #affectation de la variable
print(tupla)

liste = [1,2,3,4] #je peux changer un element
liste[0]=1000
print(liste)
tupla_b = ('un', 'deux', 'trois')
print(tupla_b+tupla) #enchaîner tuples

tupla_c = ('js ')*5 #
print(tupla_c)

repeter = tupla.count(5) #prendre le valeur et le compte
print(repeter)

premier = tupla.index(3)
print(premier) #renvoie l'indice

#modifier tuple
x= ('rouge', 'jeune', 'vert')
print(x)
y = list(x)
y[1]='modifie'
x = tuple(y)
print(x)
