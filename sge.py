estudiantes = []
contador_estudiantes = 0
flag = False

while not flag:
    print("==== SISTEMA DE GESTIÓN DE ESTUDIANTES ====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        id_estudiante = input("Ingrese el ID del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        carrera = input("Ingrese la carrera del estudiante: ")

        estudiante = {
            "ID": id_estudiante,
            "Nombre": nombre,
            "Edad": edad,
            "Carrera": carrera
        }
        estudiantes.append(estudiante)
        contador_estudiantes += 1
        print("Estudiante agregado exitosamente.")

    elif opcion == 2:
        if contador_estudiantes == 0:
            print("No hay estudiantes registrados.")
        else:
            for estudiante in estudiantes:
                print("-----------------------------")
                print(f"ID: {estudiante['ID']}")
                print(f"Nombre: {estudiante['Nombre']}")
                print(f"Edad: {estudiante['Edad']}")
                print(f"Carrera: {estudiante['Carrera']}")
            print("-----------------------------")

    elif opcion == 3:
        if contador_estudiantes == 0:
            print("No hay estudiantes registrados.")
        else:
            id_buscar = input("Ingrese el ID del estudiante a buscar: ")
            encontrado = False
            for estudiante in estudiantes:
                if estudiante["ID"] == id_buscar:
                    print("Estudiante encontrado:")
                    print(f"ID: {estudiante['ID']}")
                    print(f"Nombre: {estudiante['Nombre']}")
                    print(f"Edad: {estudiante['Edad']}")
                    print(f"Carrera: {estudiante['Carrera']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Estudiante no encontrado.")

    elif opcion == 4:
        flag = True
    else:
        print("Opción no válida. Intente de nuevo.")


            
