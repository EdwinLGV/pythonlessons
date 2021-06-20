def calcular_total(num1, num2, num3):
    return num1 + num2 + num3
    # return total_local

def promedio():
    numero_1 = float(input('Primer número: '))
    numero_2 = float(input('Segundo número: '))
    numero_3 = float(input('Tercero número: '))
    return  calcular_total(numero_1, numero_2, numero_3) / 3
    # return total/3

print(promedio())