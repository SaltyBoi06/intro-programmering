lista = [59, 53, 52]
print(lista)

lista.extend([51])
print(lista)

lista.insert(0, 56)
print(lista)

lista.pop(1)
lista.insert(1, 22)
print(lista)

lista.pop(len(lista)-2)
lista.insert(len(lista)-1, 99)
print(lista)
print()
b=0
n=0
for x in lista:
    b = b + x
    n = b/len(lista)
print("Medelvärde av lista:", n)

print()
print()
lista2=[9.95, 10.78, 9.99, 10.07, 10.24, 10.47]
print(lista2)
lista3=[]
for x in lista2:
    lista3.append(x+0.01)
print(lista3)