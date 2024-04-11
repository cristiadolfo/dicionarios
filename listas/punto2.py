inventario = {}

while True:
    print("\nBienvenido al sistema de inventario de productos")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Salir")

    opcion = input("Por favor seleccione una opción: ")

    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = input("Ingrese la cantidad disponible: ")
        inventario[nombre_producto] = cantidad
        print("Producto agregado al inventario exitosamente")
    elif opcion == "2":
        nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")
        if nombre_producto in inventario:
            print(f"La cantidad disponible de {nombre_producto} es: {inventario[nombre_producto]}")
        else:
            print("El producto no se encuentra en el inventario")
    elif opcion == "3":
        print("Gracias por usar el sistema de inventario")
        break
    else:
        print("Opción inválida Por favor seleccione una opción válida")