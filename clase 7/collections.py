palabra = 'Una palabra'
print(palabra)
lista = list(palabra)
print(lista)
diccionario = {'nombre': 'Lina', 'Apellido': 'Silva'}
lista = list(diccionario)
lista = list(diccionario.keys())
lista = list(diccionario.values())
#lista = list(diccionario.items())
print(lista)
tupla = tuple(lista)
print(tupla)

lista = list(palabra)
palabra = ''.join(lista)
print(palabra)
