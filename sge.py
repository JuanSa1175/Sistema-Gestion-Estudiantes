# Lista donde se almacenarán todos los estudiantes registrados.
# Cada estudiante se guardará como un diccionario.
estudiantes = []

# Variable contador que lleva el número total de estudiantes registrados.
contador_estudiantes = 0

# Variable bandera que controla la ejecución del programa.
# Mientras sea False, el menú seguirá mostrándose.
flag = False


# Bucle principal del programa.
# Se ejecuta repetidamente hasta que flag cambie a True.
while not flag:

    # Mostrar el menú principal al usuario.
    print("==== SISTEMA DE GESTIÓN DE ESTUDIANTES ====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Salir")

    # Solicitar al usuario la opción que desea ejecutar.
    opcion = int(input("Seleccione una opción: "))

    # Opción 1: Agregar un nuevo estudiante.
    if opcion == 1:

        # Solicitar los datos del estudiante.
        id_estudiante = input("Ingrese el ID del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        carrera = input("Ingrese la carrera del estudiante: ")

        # Crear un diccionario con la información del estudiante.
        estudiante = {
            "ID": id_estudiante,
            "Nombre": nombre,
            "Edad": edad,
            "Carrera": carrera
        }

        # Agregar el diccionario a la lista de estudiantes.
        estudiantes.append(estudiante)

        # Incrementar el contador de estudiantes.
        contador_estudiantes += 1

        # Confirmar que el estudiante fue agregado correctamente.
        print("Estudiante agregado exitosamente.")

    # Opción 2: Mostrar todos los estudiantes registrados.
    elif opcion == 2:

        # Verificar si no hay estudiantes registrados.
        if contador_estudiantes == 0:
            print("No hay estudiantes registrados.")
        else:
            # Recorrer la lista de estudiantes e imprimir sus datos.
            for estudiante in estudiantes:
                print("-----------------------------")
                print(f"ID: {estudiante['ID']}")
                print(f"Nombre: {estudiante['Nombre']}")
                print(f"Edad: {estudiante['Edad']}")
                print(f"Carrera: {estudiante['Carrera']}")

            print("-----------------------------")

    # Opción 3: Buscar un estudiante por su ID.
    elif opcion == 3:

        # Verificar si la lista está vacía.
        if contador_estudiantes == 0:
            print("No hay estudiantes registrados.")
        else:
            # Solicitar el ID que se desea buscar.
            id_buscar = input("Ingrese el ID del estudiante a buscar: ")

            # Variable booleana para indicar si el estudiante fue encontrado.
            encontrado = False

            # Recorrer la lista de estudiantes.
            for estudiante in estudiantes:

                # Comparar el ID del estudiante actual con el ID buscado.
                if estudiante["ID"] == id_buscar:

                    # Mostrar los datos del estudiante encontrado.
                    print("Estudiante encontrado:")
                    print(f"ID: {estudiante['ID']}")
                    print(f"Nombre: {estudiante['Nombre']}")
                    print(f"Edad: {estudiante['Edad']}")
                    print(f"Carrera: {estudiante['Carrera']}")

                    # Cambiar la variable a True porque se encontró el estudiante.
                    encontrado = True

                    # Salir del ciclo for para no seguir buscando.
                    break

            # Si al finalizar el recorrido no se encontró el estudiante.
            if not encontrado:
                print("Estudiante no encontrado.")

    # Opción 4: Salir del sistema.
    elif opcion == 4:

        # Cambiar la bandera a True para terminar el ciclo while.
        flag = True

    # Si el usuario ingresa una opción diferente a 1, 2, 3 o 4.
    else:
        print("Opción no válida. Intente de nuevo.")
