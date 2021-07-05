import numpy as np

""" matriz = [[21, 22, 23], [34, 35, 36], [47, 48, 49]]

matriz_np = np.array(matriz)

i = 1 
columna = matriz_np[:,i]
print(columna) """


#para matrices irregulares
matriz_irregular = [[21, 22, 23, 24], [34, 35], [47, 48, 49]]

matriz_irregular_np = np.array(matriz_irregular)

i = 2 #columna que se quiere obtener
columna = []
for fila in matriz_irregular_np:
    if i < len(fila):
        columna.append(fila[i])
        print(matriz_irregular_np)


