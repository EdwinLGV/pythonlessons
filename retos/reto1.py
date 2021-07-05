from os import system
system('cls')
print('Bienvenido a la zona wifi')
#usuario_guardado = '51743'
#pass_guardado = usuario_guardado[::-1]
user = input('Digite su número de grupo ')
try:
    int(user)
    if len(user) != 5:
        print('Error el dato ingresado debe ser de 5 caracteres')
    else:
        password = input('Digite su contraseña ')
        if user[::-1] == password:
            print('Solucione el capcha')
            print(f'{user[-3::1]} + {user[-2]}')
            capcha = input()
            if int(capcha) == int(user[-3::1]) + int(user[-2]):
                print('Sesión iniciada correctamente!')
            else:
                print('Error en el capcha')
        else:
            print('Error en la contraseña')
except:
    print('Error en el dato ingresado, debe ser númerico')
       