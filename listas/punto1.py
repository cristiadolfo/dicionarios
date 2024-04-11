agenda = {}

def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto agregado exitosamente!")

def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es: {agenda[nombre]}")
    else:
        print("El contacto no se encuentra en la agenda.")

def main():
    while True:
        print("\nBienvenido a la agenda de contactos.")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Salir")

        opcion = input("Por favor, seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agregar_contacto(nombre, telefono)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            buscar_contacto(nombre)
        elif opcion == "3":
            print("Gracias por usar la agenda de contactos. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()