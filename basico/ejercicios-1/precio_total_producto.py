nombre_producto = input("Introduzca el nombre del producto: ")
precio_producto = input("Introduzca el precio del producto: ")
cantidad_producto = input("Introduzca la cantidad del producto: ")

if nombre_producto.isalpha() and precio_producto.replace(".", "").isnumeric() and cantidad_producto.isnumeric():
    precio_producto = float(precio_producto)
    cantidad_producto = int(cantidad_producto)
    
    print(f"El producto {nombre_producto} vale {precio_producto:.2f} € con una cantidad de {cantidad_producto} unidades y un precio total de {precio_producto * cantidad_producto:.2f} €")
else:
    print("Error. Por favor introduzca datos correctos.")
