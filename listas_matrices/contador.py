""" total = 0
contador = 0
while (True):
    inp = input('Ingresa un número: ')
    if inp == 'fin': break
    valor = float(inp)
    total = total + valor
    contador = contador + 1
    
promedio = total / contador
print('Promedio: ', promedio)    """

numlista = list()
while (True):
    inp = input('Ingrese un número: ')
    if inp == 'fin': break
    
    valor = float(inp)
    numlista.append(valor)

promedio = sum(numlista) / len(numlista)
print ('Promedio :', promedio)    
     