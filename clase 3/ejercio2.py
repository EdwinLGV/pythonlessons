tiempo_ingresos = int(input('número de pasajeros que ingresan:'))*2
tiempo_salidas = int(input('número de pasajeros que salen:'))*1

def calcular_tiempo(pasajeros_suben, pasajeros_bajan) -> int:
    total = pasajeros_suben + pasajeros_bajan + 180
    return total

print(calcular_tiempo(tiempo_ingresos, tiempo_salidas))