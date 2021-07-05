import math
import pandas as pd
from os import system
system('cls')

#definicion de variables y funciones globales:
#Se envía la bienvenida 
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Se definen las variables
usuariop = int(51743)
contrasenap = int(34715)
#Variables para validar el capcha y se convierten a entero para poder efectuar operaciones aritméticas
sumando1 = str(usuariop)[-3:]
sumando2 = str(usuariop)[-2]
captchap = int(sumando1) + int(sumando2)

#Variables para las 3 operaciones solicitadas en el captcha, se convierten a entero cada dígito para poder operarlas
operando1 = int(str(usuariop)[0])#5
operando2 = int(str(usuariop)[1])#1
operando3 = int(str(usuariop)[-3])#7
operando4 = int(str(usuariop)[-1])#3
operando5 = int(str(usuariop)[3])#4

operaciona = operando3 - operando4
operacionb = (((operando3 + operando2) * operando4) % operando1 )
operacionc = round(((operando3 * operando1) - operando4 ) / (operando2 + operando3))

#Definir matriz para Coordenadas:
coordenadas=[["EMPTY" for i in range (2)] for j in range (3)]

#validar coordenada:
max_latitud = [2.548,2.766]
max_longitud = [-76.879,-76.493]

def imprimir_coordenadas(coord):
    i = 0
    while i < len(coord):
        j = 0
        print(f"coordenada [latitud, longitud] " + str(i+1) + "  :  ['" + str(coord[i][j]) + "', '"+ str(coord[i][j+1]) + "']" )
        i += 1

def esCoordenadaValida(latitud:float, longitud:float, limlatitudinf:float, limlatitudsup:float, limlongitudinf:float, limlongitudsup:float) -> bool:
    validarLatitud = latitud >= limlatitudinf and latitud <= limlatitudsup
    validarLongitud = longitud >= limlongitudinf and longitud <= limlongitudsup
    if validarLatitud and validarLongitud:
        return True
    else:
        return False

def esCoordenadaenRango(coord):
    k = 0
    x = False
    while k < len(coord):
        if esCoordenadaValida(coord[k][0],coord[k][1],max_latitud[0],max_latitud[1],max_longitud[0],max_longitud[1] ) == x:
            x = False
        else:
            x = True
        k += 1
    return x

def sitiosVacios(coord):
    coorVacia=[["EMPTY" for i in range (2)] for j in range (3)]
    if coord == coorVacia:
        return True
    else:
        return False

# esCoordenadaVacia
def tieneCoordVacia(coord):
    x = False
    for fila in coord:
        if fila[0] == "EMPTY" and fila[1] == "EMPTY":
            x = True
    return x

def ingresarCoordenadas():
    i = 0
    x = True
    while i < len(coordenadas):
        j = 0
        while j < len(coordenadas[i])  :
            coordenadas[i][j] = float(input(f"Por favor ingrese la matriz de coordenadas de sus sitios de acuerdo a lo siguiente latitud, longitud " + str(i+1) + ", "+ str(j+1)  + " : "))   
            if esCoordenadaValida(coordenadas[i][j],coordenadas[i][j],max_latitud[0],max_latitud[1],max_longitud[0],max_longitud[1]) == x and coordenadas[i][j] != 0:
                x = True
            else:
                x = False
                #print("Error")
                #break
            j += 1
        i += 1
    return x       

# Funcion que calcula la coordenada ubicada mas al norte
def coordenadaNorte(coord):
    latitudes = []
    latitudNor = 0
    for sitio in coord:
        latitudes.append(sitio[0])
    latitudNor = latitudes.index(max(latitudes))+1
    print("La coordenada " + str(latitudNor) + " es la que está más al norte")

# Funcion que calcula la coordenada promedio
def coordenada_promedio(matrix):
    i = 0
    sum_latitud = 0
    sum_longitud = 0
    coord_prom = []
    while i < len(matrix):
        sum_latitud = sum_latitud + float(matrix[i][0])
        sum_longitud = sum_longitud + float(matrix[i][1])
        i += 1
    coord_prom = [round(sum_latitud / 3, 3), round(sum_longitud / 3, 3)]
    print("La coordenada promedio es: " + str(coord_prom))

#menu principal
def show_menu():
    #Definir lista opciones de menú
    opcionesmenu = ['1. Cambiar contraseña', '2. Ingresar coordenadas actuales', '3. Ubicar zona wifi más cercana', '4. Guardar archivo con ubicación cercana', '5. Actualizar registros de zonas wifi desde archivo', '6. Elegir opción de menú favorita', '7. Cerrar sesión']
    contador = 0
    useropc = 0
    contrasenap = int(34715)
# TODO: Revisar código    

    def imprimir_menu():
        for opc in opcionesmenu:
            print(opc)
        print("\n")

    imprimir_menu()    
    useropc = int(input("Elija una opción "))

    while contador <= 3: # Se controla la cantidad de veces que se puede equivocar el usuario si >3 genera error
        print("Usted ha elegido la opción " + str(useropc))
        if useropc == 1:
            contrasena_act = int(input("Por favor confirme su contraseña actual: "))
            if contrasena_act == contrasenap:
                contrasena_nuv = int(input("Por favor ingrese la nueva contraseña: "))
                contrasenap = contrasena_nuv
                imprimir_menu()
                #useropc = int(input("Elija una opción "))
                #continue
            else:
                print("Error")
                exit(0)

        if useropc == 2:
            if sitiosVacios(coordenadas) != True: # Para la segunda o + veces
                imprimir_coordenadas(coordenadas)
                coordenadaNorte(coordenadas)
                coordenada_promedio(coordenadas)
                modifica_coor = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. \nPresione 0 para regresar al menú "))
                if modifica_coor >= 0 and modifica_coor <= 3:
                    if modifica_coor >= 1 and modifica_coor <= 3:
                        #modifica coordenada
                        lat = float(input("Ingrese la latitud: "))
                        long = float(input("Ingrese la longitud: "))
                        coordenadas[modifica_coor-1][0] = lat
                        coordenadas[modifica_coor-1][1] = long
                        if esCoordenadaenRango(coordenadas) == True:
                            imprimir_menu()
                            useropc = int(input("Elija una opción "))
                            #continue
                        else:
                            print("Error coordenada")
                            exit(0)
                    elif modifica_coor == 0:
                        imprimir_menu()
                        useropc = int(input("Elija una opción "))
                        #continue
                else:
                    print("Error actualización")
                    exit(0)
            elif sitiosVacios(coordenadas) == True: #Para la primera vez
                #ingreso datos
                ingresarCoordenadas()
                #imprimir_coordenadas(coordenadas) #comentar lfsz
                if tieneCoordVacia(coordenadas) == False:
                    if esCoordenadaenRango(coordenadas) == True:
                        imprimir_menu()
                        useropc = int(input("Elija una opción "))
                        continue                        
                    else:
                        print("Error coordenada")
                        exit(0)
                else:
                    print("Error")
                    exit(0)
            else:
                print("Error")
                exit(0) 
        # if useropc == 3:
        # if useropc == 4:
        # if useropc == 5:

        if useropc == 6:
            fav = input("Seleccione opción favorita ")
            if int(fav) >=1 and int(fav) <= 5:
                adivinanzaa = int(input("Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "))
                if adivinanzaa == operando5:
                    adivinanzab = int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es: "))
                    if adivinanzab == operando4:
                        contador = 4
                        laopc = opcionesmenu.pop(int(fav)-1)
                        opcionesmenu.insert(0,laopc)
                        print("Usted ha elegido la opción " + str(fav))
                        print("\n")
                    else:
                        print("Error")
                        system('cls')
                        contador += 1
                else:
                    print("Error")
                    system('cls')
                    contador += 1
                imprimir_menu()
                useropc = int(input("Elija una opción"))
                print("Usted ha elegido la opción " + str(useropc))
            else:
                contador = 4
                print("Error")

        if useropc == 7:
            print("Hasta pronto")
            exit(0)
        
        else:
            print("Error")    
        contador += 1
        exit()

#Inicio Programa
def initial_validation():
    usuario = int(input("Por favor ingrese su usuario: "))
    if usuario == usuariop:
        contrasena = int(input("Por favor ingrese su contraseña: "))
        if contrasena == contrasenap:
         import math
import numpy as np
from numpy.core.fromnumeric import reshape, resize

from os import system
system('cls')

#definicion de variables y funciones globales:
#Se envía la bienvenida 
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Se definen las variables
usuariop = int(51743)
contrasenap = int(34715)
#Variables para validar el capcha y se convierten a entero para poder efectuar operaciones aritméticas
sumando1 = str(usuariop)[-3:]
sumando2 = str(usuariop)[-2]
captchap = int(sumando1) + int(sumando2)

#Variables para las 3 operaciones solicitadas en el captcha, se convierten a entero cada dígito para poder operarlas
operando1 = int(str(usuariop)[0])#5
operando2 = int(str(usuariop)[1])#1
operando3 = int(str(usuariop)[-3])#7
operando4 = int(str(usuariop)[-1])#3
operando5 = int(str(usuariop)[3])#4

operaciona = operando3 - operando4
operacionb = (((operando3 + operando2) * operando4) % operando1 )
operacionc = round(((operando3 * operando1) - operando4 ) / (operando2 + operando3))


#Definir matriz para Coordenadas:
coordenadas=[["EMPTY" for i in range (2)] for j in range (3)]

#validar coordenada:
max_latitud = [2.548,2.766]
max_longitud = [-76.879,-76.493]

def imprimir_coordenadas(coord):
    i = 0
    while i < len(coord):
        j = 0
        print(f"coordenada [latitud, longitud] " + str(i+1) + "  :  ['" + str(coord[i][j]) + "', '"+ str(coord[i][j+1]) + "']" )
        i += 1

def esCoordenadaValida(latitud:float, longitud:float, limlatitudinf:float, limlatitudsup:float, limlongitudinf:float, limlongitudsup:float) -> bool:
    validarLatitud = latitud >= limlatitudinf and latitud <= limlatitudsup
    validarLongitud = longitud >= limlongitudinf and longitud <= limlongitudsup
    if validarLatitud and validarLongitud:
        return True
    else:
        return False

def esCoordenadaenRango(coord):
    k = 0
    x = False
    while k < len(coord):
        if esCoordenadaValida(coord[k][0],coord[k][1],max_latitud[0],max_latitud[1],max_longitud[0],max_longitud[1] ) == x:
            x = False
        else:
            x = True
        k += 1
    return x

def sitiosVacios(coord):
    coorVacia=[["EMPTY" for i in range (2)] for j in range (3)]
    if coord == coorVacia:
        return True
    else:
        return False

# esCoordenadaVacia
def tieneCoordVacia(coord):
    x = False
    for fila in coord:
        if fila[0] == "EMPTY" and fila[1] == "EMPTY":
            x = True
    return x

def ingresarCoordenadas():
    i = 0
    x = True
    while i < len(coordenadas):
        j = 0
        while j < len(coordenadas[i])  :
            coordenadas[i][j] = float(input(f"Por favor ingrese la matriz de coordenadas de sus sitios de acuerdo a lo siguiente latitud, longitud " + str(i+1) + ", "+ str(j+1)  + " : "))   
            if esCoordenadaValida(coordenadas[i][j],coordenadas[i][j],max_latitud[0],max_latitud[1],max_longitud[0],max_longitud[1]) == x and coordenadas[i][j] != 0:
                x = True
            else:
                x = False
                #print("Error")
                #break
            j += 1
        i += 1
    return x       

# Funcion que calcula la coordenada ubicada mas al norte
def coordenadaNorte(coord):
    latitudes = []
    latitudNor = 0
    for sitio in coord:
        latitudes.append(sitio[0])
    latitudNor = latitudes.index(max(latitudes))+1
    print("La coordenada " + str(latitudNor) + " es la que está más al norte")

# Funcion que calcula la coordenada promedio
def coordenada_promedio(matrix):
    i = 0
    sum_latitud = 0
    sum_longitud = 0
    coord_prom = []
    while i < len(matrix):
        sum_latitud = sum_latitud + float(matrix[i][0])
        sum_longitud = sum_longitud + float(matrix[i][1])
        i += 1
    coord_prom = [round(sum_latitud / 3, 3), round(sum_longitud / 3, 3)]
    print("La coordenada promedio es: " + str(coord_prom))


#Definir lista opciones de menú
opcionesmenu = ['1. Cambiar contraseña', '2. Ingresar coordenadas actuales', '3. Ubicar zona wifi más cercana', '4. Guardar archivo con ubicación cercana', '5. Actualizar registros de zonas wifi desde archivo', '6. Elegir opción de menú favorita', '7. Cerrar sesión']
contador = 0
useropc = 0
contrasenap = int(34715)

def imprimir_menu():
    for opc in opcionesmenu:
        print(opc)
    print("\n")

#Definición zonas Wifi disponibles
zonas_wifi = [[  2.698, -76.68 ,  63   ], [  2.724, -76.693,  20   ], [  2.606, -76.742, 680   ], [  2.698, -76.69 ,  15   ]]
R = 6372.795477589 * 100
velprombus = 16.67 # m/S
velprombici = 3.33 # m/s


def calcular_distancia(coordact, zonawifi):
    a = pow(math.sin((zonawifi[0]-coordact[0])/2),2)
    b = math.cos(coordact[0])
    c = math.cos(zonawifi[0])
    d = pow(math.sin((zonawifi[1]-coordact[1])/2),2)
    distancia = 2 * R * math.asin(math.sqrt((a+(b*c*d))))
    return distancia

def calcula_zonas_cercanas(ubica_act, zonas_wifi):
    distancias = []
    for zona in zonas_wifi:
        distancias.append(calcular_distancia(ubica_act, zona))
    cercanas = np.argsort(distancias)[:2]
    return cercanas


usuario = int(input("Por favor ingrese su usuario: "))
if usuario == usuariop:
    contrasena = int(input("Por favor ingrese su contraseña: "))
    if contrasena == contrasenap:
        captcha = int(input("Por favor ingrese el Captcha " + sumando1 + " + " + str(operacionc) + " = " )) #operacionc tambien se puede reemplazar por str(operaciona), str(operacionb) ó sumando2
        if captcha == captchap:
            print("Sesión iniciada")
            print("\n")                                
            imprimir_menu()    
            useropc = int(input("Elija una opción "))

            while contador <= 3: # Se controla la cantidad de veces que se puede equivocar el usuario si >3 genera error
                print("Usted ha elegido la opción " + str(useropc))
                if useropc == 1:
                    contrasena_act = int(input("Por favor confirme su contraseña actual: "))
                    if contrasena_act == contrasenap:
                        contrasena_nuv = int(input("Por favor ingrese la nueva contraseña: "))
                        contrasenap = contrasena_nuv
                        imprimir_menu()
                        useropc = int(input("Elija una opción "))
                        continue
                    else:
                        print("Error")
                        exit(0)
                        
                if useropc == 2:
                    if sitiosVacios(coordenadas) != True:
                        imprimir_coordenadas(coordenadas)
                        coordenadaNorte(coordenadas)
                        coordenada_promedio(coordenadas)
                        modifica_coor = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. \nPresione 0 para regresar al menú "))
                        if modifica_coor >= 0 and modifica_coor <= 3:
                            if modifica_coor >= 1 and modifica_coor <= 3:
                                #modifica coordenada
                                lat = float(input("Ingrese la latitud: "))
                                long = float(input("Ingrese la longitud: "))
                                coordenadas[modifica_coor-1][0] = lat
                                coordenadas[modifica_coor-1][1] = long
                                if esCoordenadaenRango(coordenadas) == True:
                                    imprimir_menu()
                                    useropc = int(input("Elija una opción "))
                                    continue
                                else:
                                    print("Error coordenada")
                                    exit(0)
                            elif modifica_coor == 0:
                                imprimir_menu()
                                useropc = int(input("Elija una opción "))
                                continue
                        else:
                            print("Error actualización")
                            exit(0)
                    elif sitiosVacios(coordenadas) == True: #Para la primera vez
                        #ingreso datos
                        ingresarCoordenadas()
                        #imprimir_coordenadas(coordenadas) #comentar lfsz
                        if tieneCoordVacia(coordenadas) == False:
                            if esCoordenadaenRango(coordenadas) == True:
                                imprimir_menu()
                                useropc = int(input("Elija una opción "))
                                continue                        
                            else:
                                print("Error coordenada")
                                exit(0)
                        else:
                            print("Error")
                            exit(0)
                    else:
                        print("Error")
                        exit(0) 
                if useropc == 3:
                    if tieneCoordVacia(coordenadas) == True:
                        print("Error sin registro de coordenadas")
                        exit(0)
                    else:
                        imprimir_coordenadas(coordenadas)
                        ubicacionact = int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión "))
                        if 1 <= ubicacionact <= 3:
                            cooract = coordenadas[ubicacionact-1]
                            zonas_cercanas = calcula_zonas_cercanas(cooract, zonas_wifi)
                            doscercanas = [zonas_wifi[zonas_cercanas[0]] , zonas_wifi[zonas_cercanas[1]]]
                            doscercanasord = sorted(doscercanas, key=lambda doscercana: doscercana[2])
                            doscercanasordi = np.delete(doscercanasord, 2, 1)
                            distanciacer1 = calcular_distancia(cooract, doscercanasordi[0])
                            distanciacer2 = calcular_distancia(cooract, doscercanasordi[1])
                            print(f"La zona wifi {(calcula_zonas_cercanas(cooract, zonas_wifi)[0])+1}: ubicada en " + str(doscercanasordi[0]) + " a " + str(round(distanciacer1)) + " metros, tiene en promedio " + str(doscercanasord[0][2]) + " usuarios")
                            print(f"La zona wifi {(calcula_zonas_cercanas(cooract, zonas_wifi)[1])+1}: ubicada en " + str(doscercanasordi[1]) + " a " + str(round(distanciacer2)) + " metros, tiene en promedio " + str(doscercanasord[1][2]) + " usuarios")
                            zonawfdestino = int(input("Elija 1 o 2 para recibir indicaciones de llegada "))
                            if 1 <= zonawfdestino <= 2:
                                distzonaeleg = calcular_distancia(cooract, zonas_wifi[zonawfdestino-1])
                                tprombus = distzonaeleg / velprombus
                                tprombici = distzonaeleg / velprombici
                                #calculo la direccion:
                                if cooract[0] - doscercanasordi[zonawfdestino-1][0] < 0:
                                    dlatitud = "norte"
                                else:
                                    dlatitud = "sur"
                                if cooract[1] - doscercanasordi[zonawfdestino-1][1] > 0:
                                    dlongitud = "oriente"
                                else:
                                    dlongitud = "occidente"
                                print(f"Para llegar a la zona wifi dirigirse primero al {dlongitud} y luego hacia el {dlatitud} ")
                                print(f"Tiempo promedio en bus: " +str(round(tprombus)) + " seg")
                                print(f"Tiempo promedio en bici: " +str(tprombici) + " seg")
                                salir = int(input(("Presione 0 para salir")))
                                if salir == 0: 
                                    imprimir_menu()
                                useropc = int(input("Elija una opción "))
                                continue
                            else:
                                print("Error zona wifi")
                                exit(0)                            
                        else:
                            print("Error ubicación")
                            exit(0)
                        #calcular 
                # if useropc == 4:
                # if useropc == 5:

                if useropc == 6:
                    fav = input("Seleccione opción favorita ")
                    if int(fav) >=1 and int(fav) <= 5:
                        adivinanzaa = int(input("Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "))
                        if adivinanzaa == operando5:
                            adivinanzab = int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es: "))
                            if adivinanzab == operando4:
                                contador = 4
                                laopc = opcionesmenu.pop(int(fav)-1)
                                opcionesmenu.insert(0,laopc)
                                print("Usted ha elegido la opción " + str(fav))
                                print("\n")
                            else:
                                print("Error")
                                system('cls')
                                contador += 1
                        else:
                            print("Error")
                            system('cls')
                            contador += 1
                        imprimir_menu()
                        useropc = int(input("Elija una opción"))
                        print("Usted ha elegido la opción " + str(useropc))
                    else:
                        contador = 4
                        print("Error")

                if useropc == 7:
                    print("Hasta pronto")
                    exit(0)
                
                else:
                    print("Error")    
                contador += 1
                #print(contador)
                exit()

            else:
                print("Error")
                exit(0)
        else:
            print("Error")
            exit(0)
    else:
        print("Error")
        exit(0)   
        captcha = int(input("Por favor ingrese el Captcha " + sumando1 + " + " + str(operacionc) + " = " )) #operacionc tambien se puede reemplazar por str(operaciona), str(operacionb) ó sumando2
        if captcha == captchap:
                print("Sesión iniciada")
                print("\n")
                show_menu()
        else:
            print("Error")
            exit(0)
else:
    print("Error")
    exit(0)

def run():
    show_menu()
    run()

if __name__ == '__main__':
    initial_validation()
    run()

initial_validation()
show_menu()