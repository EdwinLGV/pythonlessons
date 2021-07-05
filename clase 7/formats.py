num1 = 15
num2 = 43

mensaje = 'Los números son ' + str(num1) +', ' +str(num2)
print(mensaje)
mensaje = 'Los números son {}, {}'.format(num1, num2)
print(mensaje)
mensaje = 'Los números son {1}, {0}, {2}'.format(num1, num2, 58)
print(mensaje) 
mensaje = 'Los números son %d'%(num1)
print(mensaje)
mensaje = f'Los números son {num1}, {num2}'
print(mensaje)
