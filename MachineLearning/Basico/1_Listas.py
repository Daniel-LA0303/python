lista1 = [1,2,3,4,5,6] #lista de num
lista1_1 = [7,8,9,10,11,12]
print(lista1)

lista2 = ["a","java","js","python"] #lista de strings
print(lista2)

lista3 = [1,2,3,"python","js",2.5,["a","b"]] #lista de diferentes tipos de datos
print(lista3)

suma = lista1+lista1_1 #concatena listas
print(suma)

num = [1,2,3,4,5]
num[2]=9 #cambia el elemento de la lista
print(num)

print(len(num)) #tamaño de la lista

print(num[1:3])#toma en cuenta solo los elementos con determinadas pocisiones

num.insert(2,"nuevo") #2=posicion del nuevo elemento
print(num)

num.append("nuevo2") #agrega el elemento al ultimo
print(num)

#print(num.extend()) #concatena las dos listas

letras=["def","abc","xyz"]
letras.sort()
print(letras) #ordena la lista
print(letras.index("abc"))#devuelve la posicion del elemento

print(letras.pop()) #elimina el primer elemento