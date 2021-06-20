precio_producto = input('Digite el precio: ')
precio_producto = float(precio_producto)
iva = 0.19
print('El iva es: '+ str(precio_producto * iva) )
print('El total es: '+str(precio_producto + (precio_producto * iva)))