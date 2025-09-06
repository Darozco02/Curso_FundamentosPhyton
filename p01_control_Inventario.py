print("Bienvenido al Sistema de control de inventario!")
print("-" * 50)

#Creacion de listas
lista_productos = []

#Menu
while True:
    opc = int(input("Por favor ingrese la opcion deseada: \n1. Ingresar nuevo producto \n2. Ver inventario \n3. Eliminar producto \n 4. Salir \n"))

    #Agregar Productos al Inventario
    if opc == 1:
        
        while True:
            #Solicitar los datos del producto
            nombre_producto = input("Por favor ingrese el nombre del producto: ").title().strip()
            cantidad = int(input("Por favor ingrese la cantidad de productos: "))
            precio_unitario = float(input("Por favor ingrese el precio del producto: "))
            lista_productos.append((nombre_producto, cantidad, precio_unitario))
            print("Producto ingresado con exito!")
            print("-" * 50)

            #Ingresar nuevo producto
            nuevo_producto = input("Desea ingresar otro producto? (s/n): ").title().strip()
            if nuevo_producto != "S":
                break

    #Ver inventario
    elif opc == 2:
        for indice, producto in enumerate(lista_productos, 1):
            print(f"Producto {indice}: Nombre: {producto[0]}, Cantidad: {producto[1]}, Precio Unitario: {producto[2]} Colones")
            #Realizar el calculo total por producto
            calculo_total = producto[1] * producto[2]
            print(f"El valor total del inventario de {producto[0]} es: {calculo_total} Colones")
            
        else:
            print("El inventario esta vacio, por favor ingrese un producto.")
            continue

    #Eliminar productos
    elif opc == 3:
        producto_eliminar = input("Digite el nombre del producto que desea eliminar: ").title().strip()
        for producto in lista_productos:
            if producto_eliminar == producto[0]:
                lista_productos.remove(producto)
                print(f"✅ El producto {producto_eliminar} ha sido eliminado del inventario con exito!")

    #Salir del sistema
    elif opc == 4:
        print("Gracias por usar el sistema de control de inventario, hasta pronto! 👋")
        break

    else:
        print("Opcion no valida, por favor intente de nuevo.")
        continue
