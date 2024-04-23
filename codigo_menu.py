from seleccionar_cursos import *

empleados = []
cursos = cursos_disponibles


# FUNCIONES

def caso_01():
    nombre = str(input("Nombre del DICCIONARIO: "))
    while True:
        legajo = input("Legajo del DICCIONARIO: ") # validar ?
        if len(legajo) != 5:
            print("\nEL LEGAJO DEBE TENER 5 CARACTERES\nVUELVA A INGRESARLO\n")
        else:
            break

        antiguedad = int(input("Antiguedad en meses: ")) # validar ?

        if antiguedad < 6:
            print("\nLa antiguedad debe ser mayor a 6 meses")
            return
            # si es menor a 6 no cae aca abajo
        empleados.append({"nombre": nombre, "legajo": legajo, "antiguedad": antiguedad, "cursos": []})
        print("\nREALIZADO")

def caso_02():
    legajo = input("\nIngrese el legajo del Empleado:")
    encontrado = False
    for DICCIONARIO in empleados:
        if DICCIONARIO["legajo"] == legajo:
            encontrado = True
            while True:
                print("\n1. - Agregar Curso")
                print("2. - Finalizar")
                opcion = input("\nSeleccione una opcion: ")
                if opcion == "1":
                    print("\n")
                    for i, cursos in enumerate(cursos_disponibles,1):
                        print(f"{i}. {cursos}")
                        valor = input("\nSeleccione un curso o ponga '0' para salir: ")
                        if valor == "0":
                            print("\nNO SE AGREGO NINGUN CURSO")
                            break
                        elif int(valor) in range(1, len(cursos_disponibles)+1):
                            curso_seleccionado = cursos_disponibles[int(valor)-1] #porque -1
                            DICCIONARIO["cursos"].append(curso_seleccionado)
                            print("DICCIONARIO:",DICCIONARIO) # agrega el curso al diccionario
                            print("Empleados:",empleados) # porque lo agrega a la lista ???
                            print("\nCursos Agregado Correctamente")
                elif opcion == "2":
                    break
                else:
                    print("\nOPCION INVALIDA")
            break
    if not encontrado:
        print("\nNO SE ENCONTRO NINGUN DICCIONARIO")
    print("\nREALIZADO")

def caso_03():
    empleados_ordenados = sorted(empleados, key=lambda e: len(e["cursos"]), reverse=True)
    print(f"Cantidad de Empleados: {len(empleados)}")

    for DICCIONARIO in empleados_ordenados:
        print("\nEmpleado:", DICCIONARIO["nombre"], "- Legajo:", DICCIONARIO["legajo"], "- Antigüedad:", DICCIONARIO["antiguedad"], "meses")
        print("Cursos:", " - ".join(DICCIONARIO["cursos"]))
        print("Cantidad de cursos:", len(DICCIONARIO["cursos"]))
        print("Empleados:",empleados)
        print("DICCIONARIO:",DICCIONARIO)
    print("\nREALIZADO")

def carga():
    DICCIONARIO = {"nombre": "11111", "legajo": "11111", "antiguedad": 11, "cursos": []}
    empleados.append(DICCIONARIO)
    DICCIONARIO = {"nombre": "22222", "legajo": "22222", "antiguedad": 22, "cursos": []}
    empleados.append(DICCIONARIO)
    print("\nREALIZADO")

# INICIO

while True:
    print("\nMenú Principal:")
    print("1. Registrar Empleado")
    print("2. Agregar nuevo curso")
    print("3. Mostrar resumen")
    print("4. Salir")
    opcion = str(input("Seleccione una opción: "))
    if opcion == "1":
        carga()
    #caso_01()
    elif opcion == "2":
        caso_02()
    elif opcion == "3":
        caso_03()
    elif opcion == "4":
        break
    else:
        print("Opcion incorrecta, vuelva aintentar")