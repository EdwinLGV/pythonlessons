def menu():
    print("---Título del menú---")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("---------------------")
    
def default():
    return "Opción no válida"

def switch(case, a, b):
    switcher = {
        1: "opcion1"(a, b),
        2: "opcion2"(a, b),
        3: "opcion3"(a, b),
        4: "opcion4"(a, b,),
    }
    return switcher.get(case, default())

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
menu()
case = int(input("Seliccione una opción:"))
print(switch(case, a, b))

    
    
        