""" numeros = [3.1, 2.8, 4.2, 4, 3.9, 2.78, 3.2, 3.68, 4.01, 2.99]

print(list(map(lambda numero: numero, numeros))) """

#multiplicar *2
""" numeros = [3.1, 2.8, 4.2, 4, 3.9, 2.78, 3.2, 3.68, 4.01, 2.99]

print(list(map(lambda numero: numero*2, numeros))) """


#booleano
numeros = [3.1, 2.8, 4.2, 4, 3.9, 2.78, 3.2, 3.68, 4.01, 2.99]

print(list(map(lambda numero: numero>3, numeros)))

#sumar uno a un número mayor a 3
numeros = [3.1, 2.8, 4.2, 4, 3.9, 2.78, 3.2, 3.68, 4.01, 2.99]

print(list(map(lambda numero: numero+1 if numero<3 else numero, numeros)))



#verificar si un número es par and sumar uno si es impar
lista = [5, 4, 6, 8, 9, 1, 7, 3, 6, 8, 5]

print(list(map(lambda numero: 'Par' if numero % 2 ==0 else 'Impar', lista)))
print(list(map(lambda numero: numero if numero % 2 ==0 else numero+1, lista)))

