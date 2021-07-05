# ent = input('Introduzca la temperatura en F°: ')
# fahr = float(ent)
# celcius = (fahr - 32.0) * 5.0 / 9.0
# print(celcius)



""" ent = input('Introduzca la temperatura en F°: ')
try:
   fahr = float(ent)
   celcius = (fahr - 32.0) * 5.0 / 9.0
   print(celcius)
except  :
    input('Ingrese un nùmero:') """


# try:
#     num = int("3a")
#     print('no existe')
# except NameError:
#     print('La variable no existe')
# except ValueError:
#     print("El valor no es un número")


ent = input('Introduzca la temperatura en F°: ')
try:
   fahr = float(ent)
   celcius = (fahr - 32.0) * 5.0 / 9.0
   print(celcius)
except:
    input('Ingrese un nùmero:')
else:
    print("Dato ingresado correctamente")
    
    
  
    

        