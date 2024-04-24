class Empleado:
    def __init__(self, nombre, legajo, antiguedad):
        self.nombre = nombre
        self.legajo = legajo
        self.antiguedad = antiguedad
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

from cursos import seleccionar_curso
empleados = []

def registrar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    legajo = input("Ingrese el legajo del empleado: ")
    antiguedad = int(input("Ingrese la antigüedad en meses del empleado: "))
    
    while antiguedad <= 6:
        print("La antigüedad en meses debe ser superior a 6.")
        antiguedad = int(input("Ingrese la antigüedad en meses del empleado: "))
    
    empleado = empleado(nombre, legajo, antiguedad)
    empleados.append(empleado)
    print("Empleado registrado exitosamente.")

def agregar_curso():
    legajo = input("Ingresa el legajo del empleado: ")
    for empleado in empleados:
        if empleado.legajo == legajo:
            while True:
                curso = seleccionar_curso()
                if curso in empleado.cursos:
                    print(f"El empleado {empleado.nombre} ya ha realizado el curso {curso}. Por favor, selecciona otro curso.")
                else:
                    empleado.agregar_curso(curso)
                    print(f"Curso {curso} agregado exitosamente al empleado {empleado.nombre}.")
                    break
            break
    else:
        print("Legajo incorrecto.")


def mostrar_resumen():
    empleados_ordenados = sorted(empleados, key=lambda x: len(x.cursos), reverse=True)
    for empleado in empleados_ordenados:
        print("------------")
        print(f"Empleado: {empleado.nombre} - Legajo: {empleado.legajo} - Antigüedad: {empleado.antiguedad} meses")
        print(f"Cursos: {' - '.join(empleado.cursos)}")
        print(f"Cantidad de cursos: {len(empleado.cursos)}")
        print("------------")




while True:
    print("----- MENÚ -----")
    print("1. Registrar empleado")
    print("2. Agregar nuevo curso")
    print("3. Mostrar resumen")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_empleado()
    elif opcion == "2":
        agregar_curso()
    elif opcion == "3":
        mostrar_resumen()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")