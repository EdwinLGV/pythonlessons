def palindromo(word):
    word = word.lower().replace(' ','')
    if word == word[::-1]:
        return f'{word} es palíndromo'
    else:
        return f'{word} no es palíndromo'
    
print(palindromo('oso'))  


#con lambda
es_palindromo = lambda word: 'Si es' if word.lower().replace(' ','')==word.lower().replace(' ','')[::-1] else 'No es'

print(es_palindromo('oso'))  

#verificar mayor
""" verificar_mayor = lambda num1, num2: "Numero 1 es mayor" if num1 > num2 else "Numero 2 es mayor"
print(verificar_mayor(3,4)) """  

#el triple del primero es igual al doble de la raiz del segundo
""" triple = lambda num1, num2:"Es igual"if num1*3 == (num2**(1/2))*2 else "No es igual"
print(triple(6, 81)) """

