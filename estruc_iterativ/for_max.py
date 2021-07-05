mayor = None
print ('Antes:', mayor)
for valor in [3, 41, 12, 9, 74, 15]:
    if mayor is None or valor > mayor:
        mayor = valor
    print ('Bucle:', valor, mayor) 
print ('Mayor:', mayor)       