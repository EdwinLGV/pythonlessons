def calcular_total(num1, num2, num3):
    total_local = num1 + num2 + num3
    return total_local

numero_1 = input('Primer número: ')
numero_2 = input('Segundo número: ')
numero_3 = input('Tercero número: ')

total = calcular_total(numero_1, numero_2, numero_3)

print(total)