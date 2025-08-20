print("Bienvenido al Sistema de control de inventario!")
print("-" * 50)

# Solicitar al usuario que ingrese los datos del producto 1
nombre_producto = input("Por favor ingrese el nombre del producto: ").title().strip()
cantidad = int(input("Por favor ingrese la cantidad de productos: "))
precio_unitario = float(input("Por favor ingrese el precio del producto: "))
print("-" * 50)

#Confirmacion de los datos ingresados
print(f"Los datos ingresados son los siguientes: " + "\n" +
      "-" + f"Nombre del producto: {nombre_producto.title().strip()}" + "\n" + 
     "-" + f"Cantidad de productos: {cantidad} unidades"  + "\n" + 
      "-" + f"Precio unitario del producto: {precio_unitario} Colones" + "\n" +
     "-" * 50)

# Solicitar al usuario que ingrese los datos del producto 2
nombre_producto2 = input("Por favor ingrese el nombre del producto: ").title().strip()
cantidad2 = int(input("Por favor ingrese la cantidad de productos: "))
precio_unitario2 = float(input("Por favor ingrese el precio del producto: "))
print("-" * 50)

#Confirmacion de los datos ingresados
print(f"Los datos ingresados son los siguientes: " + "\n" +
      "-" + f"Nombre del producto: {nombre_producto2.title().strip()}" + "\n" + 
     "-" + f"Cantidad de productos: {cantidad2} unidades"  + "\n" + 
      "-" + f"Precio unitario del producto: {precio_unitario2} Colones" + "\n" +
     "-" * 50)

# Solicitar al usuario que ingrese los datos del producto 3
nombre_producto3 = input("Por favor ingrese el nombre del producto: ").title().strip()
cantidad3 = int(input("Por favor ingrese la cantidad de productos: "))
precio_unitario3 = float(input("Por favor ingrese el precio del producto: "))
print("-" * 50)

#Confirmacion de los datos ingresados
print(f"Los datos ingresados son los siguientes: " + "\n" +
      "-" + f"Nombre del producto: {nombre_producto3.title().strip()}" + "\n" + 
     "-" + f"Cantidad de productos: {cantidad3} unidades"  + "\n" + 
      "-" + f"Precio unitario del producto: {precio_unitario3} Colones" + "\n" +
     "-" * 50)

#Creacion de listas
lista_producto1 = [nombre_producto, cantidad, precio_unitario]
lista_producto2 = [nombre_producto2, cantidad2, precio_unitario2]
lista_producto3 = [nombre_producto3, cantidad3, precio_unitario3]
lista_mixta = [lista_producto1, lista_producto2, lista_producto3]

# Calculo del total del inventario
suma_cantidades = cantidad + cantidad2 + cantidad3
suma_precios = precio_unitario + precio_unitario2 + precio_unitario3
calculo_total = suma_cantidades * suma_precios

#Creacion de diccionario
inventario_total = {
      "Producto 1": lista_producto1,
      "Producto 2": lista_producto2,
      "Producto 3": lista_producto3,
      "calculo_total": calculo_total
}

#Impresion del inventario
print(f"El inventario total es de: \n {inventario_total['Producto 1']}")
print(f"{inventario_total['Producto 2']}")
print(f"{inventario_total['Producto 3']}")
print(f"El costo total del inventario ingresado es de: {inventario_total['calculo_total']}")
