"""
est une collection non ordennée d'éléments où chaque
élément de l'ensemble est unique
"""

set = {1,2,3,4,5} #définir ensemble
print(set)

set2 = {1.2,3.2,4,6,'js',('W','k')}
print(set2)

set.add(6) #ajouter élément
print(set)

#set.clear() #nettoyer ensemble
#print(set)

set.discard(2) #jeter élément
print(set)

set.remove(4) #retirer élément
print(set)

#union d'ensambles
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A | B)

#intersection d'ensambles
print(A & B)

#différence d'ensambles
print(A - B)

#différence symétrique d'ensambles
print(A ^ B)
