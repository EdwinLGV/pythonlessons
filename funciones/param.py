def mi_funcion(nombre, apellido):
    nombre_completo = nombre, apellido
    print(nombre_completo)

mi_funcion('Edwin', 'Guzmán')

def saludar(nombre, mensaje = 'Hola'):
    print(mensaje, nombre)
    
# saludar('Pepe Grillo')

saludar(mensaje = 'Buen día', nombre = 'Juancho')

