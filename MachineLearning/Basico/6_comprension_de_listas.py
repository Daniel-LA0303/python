
#manera 1
course = []
for letras in 'python':
    course.append(letras) #agrega cada letra como un elemento de de una lista
print(course)

#manera 2
course2 = [letras for letras in 'python']
print(course2)

#crear una lista a partir de otra
lista_a = [1,2,3,4,5,6]
lista_b = []

for i in lista_a:
    to_lista_b = i
    lista_b.append(to_lista_b)

print(lista_b)

lista_c = []
for i in lista_a:
    to_lista_c = i * 2 #multiplo de 2
    lista_c.append(to_lista_c)

print(lista_c)

lista_d = [i * 2 for i in lista_a]
print(lista_d)