precio_producto = input('Digite el precio: ')
precio_producto_num = float(precio_producto)
iva = 0.19
valor_iva = precio_producto_num * iva
valor_iva_str = str( valor_iva )
print('El iva es: '+ valor_iva_str )