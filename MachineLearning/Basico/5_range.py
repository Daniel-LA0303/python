"""
la fonction range génére des entiers entre l'initiale et
la finale
"""

print(list(range(0,7)))

for i in range(0,7):
    print(i, end= ' ')
print("")
for i in range(2, 10, 2): #le dernier 2 sont des étapes
    print(i, end = ' ')

for num in range(10):
    for i in range(num):
        print(num, end=' ')
    print("")

for i in reversed(range(0, 10)):
    print(i, end=' ')
print("")
liste= list(range(1,8))
print("La liste est: ", liste)