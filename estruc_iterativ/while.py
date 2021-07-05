""" n = 5
while n > 0:
    print(n)
    n = n - 1
print('¡Despegue!') """



""" while True:
    nombre = input('Indique su nombre: ')
    if nombre:
        break """
        
while True:
    linea = input('>')
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado!')    
            

       