
abordados = int(input("Ingrese pasajeros abordados: "))
descendidos = int(input("Ingrese pasajeros descendidos: "))


def calcular_tiempo(abordados, descendidos) -> int:

    recorrido_promedio = (90/30)*60
    recorrido_total = recorrido_promedio + ((abordados*2) + (descendidos*2))
    return recorrido_total 

print(calcular_tiempo(abordados,descendidos))