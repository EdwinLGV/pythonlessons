def sumar(num1, num2,):
    return num1 + num2

def restar(num1, num2):
    return num2 - num1

def operar(operacion, num1, num2):
    return operacion(num1, num2)

resultado = operar(sumar, 54, 87)
resultado = operar(restar, 54, 87)

print(resultado)










def funcion_superior(funcion_param):
    print(funcion_param())

def decir_hola():
    return 'hola'

def decir_mundo():
    return 'mundo'

funcion_superior(decir_hola)
funcion_superior(decir_mundo)