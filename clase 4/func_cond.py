def verificar_mayor(edad1, edad2, edad3, edad4):
    #if edad1 > edad2 and edad1 > edad3 and edad1 > edad4:
    if edad1 > edad2 > edad3 > edad4:    
        print(edad1)
    elif edad2 > edad3 > edad4:
        print(edad2)
    elif edad3 > edad4:
        print(edad3)
    else:
        print(edad4)


verificar_mayor(15, 48, 45, 25)
verificar_mayor(15, 28, 25, 35)
verificar_mayor(15, 58, 45, 65)
