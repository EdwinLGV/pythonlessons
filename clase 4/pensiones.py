edad = 58
genero = 'F'
semanas = 250

if genero == 'F':
    if edad >= 58:
        if semanas >= 250:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 250 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 58 - edad ) +' años')
elif genero == 'M':
    if edad >= 60:
        if semanas >= 255:
            print('Se puede pensionar')
        else:
            print('Le faltan '+str( 255 - semanas ) +' semanas')
    else:    
        print('Le faltan '+str( 60 - edad ) +' años')
else:
    print('Genero no valido')