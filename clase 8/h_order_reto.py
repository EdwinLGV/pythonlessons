numeros = [3.1, 4.2, 4, 3.9, 3.2, 3.68, 4.01, 2.99]

def menor(collection):
    return min(collection)

def evaluar_lista(funcion, collection):
    print(funcion(collection))
    
evaluar_lista(menor, numeros)    

#crear función que regrese el núme