tripulantes = ['Sergio', 'David', 'Eider', 'Lina']

tripulantes_dic = { trupulante : '5' for trupulante in tripulantes}
#otra forma de convertir de lista a diccionario
tripulantes_dic  = dict.fromkeys(tripulantes, 5)
#tripulantes_dic = dict(zip(tripulantes, range(0, len(tripulantes)))


print(tripulantes_dic)

