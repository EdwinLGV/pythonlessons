sesion = True
opciones = {1:'Valor a',2:'Valor b', 3:'Valor c', 4:'Valor 4', 5:'Valor 5', 6:'Valor 6', 7:'Valor 7'}

while sesion:
    print('Digita el numero de la opción')
    for key, opcion in opciones.items():
        print(f'{key} {opcion}')
    option = input()
    if option == '6':
        result = input('Cuanto es 5 + 7? ')
        if result == '12':
            opcion = input('Digite la opción que desea poner como favorita')
            if int(opcion) >= 1 and int(opcion) <= 5:
                llaves = opciones.keys()
                valores = opciones.values()
                #hacer el cambio como en listas dos veces, por que son dos listas
                #la funcion pop elimina el elemento en el indice dado
                #la funcion insert agrega un elemento en el indice dado
                opciones = dict(zip(llaves, valores))
                print(opciones)
        else:
            sesion = False
    elif option == '7':        
        print('Nos fuimos')
        sesion = False