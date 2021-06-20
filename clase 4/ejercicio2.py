edad = int(input('Digita la edad: '))

if edad > 20:
    print('Categoría profesional')
elif edad >= 18:
    print('Categoría sub_20')
elif edad >= 15:
    print('Categoría juvenil')
elif edad >= 10:
    print('Categoría infantil')
else:
    print('Edad inválida')
        
    