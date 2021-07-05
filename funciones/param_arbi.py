def recorrerParamArbitrarios(parametro_fijo, *arbitrarios, **kwords):
        
    for clave in kwords:
        print("El valor de", clave, "es", kwords[clave])    
        
recorrerParamArbitrarios(1, 'hola', 'mundo', 'Edwin', clave1 = 123, clave2 = 456)
        