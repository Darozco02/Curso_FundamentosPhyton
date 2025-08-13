print("Bienvenido al Sistema de control de inventario!")
print("-" * 50)

nombre_producto = input("Por favor ingrese el nombre del producto: ").title().strip()
cantidad = input("Por favor ingrese la cantidad de productos: ")
precio_unitario = float(input("Por favor ingrese el precio del producto: "))

print(f"Los datos ingresados son los siguientes: " + "\n" +
      "-" + f"Nombre del producto: {nombre_producto.title().strip()}" + "\n" + 
      "-" + f"Cantidad de productos: {cantidad} unidades"  + "\n" + 
      "-" + f"Precio unitario del producto: {precio_unitario:.2f} Colones" + "\n" +
      "-" * 50)

calculo_total = int(cantidad) * float(precio_unitario)
#El .2f indica que se mostrará el número con dos decimales nada mas
print(f"El precio total del inventario es de: {calculo_total:.2f} Colones")