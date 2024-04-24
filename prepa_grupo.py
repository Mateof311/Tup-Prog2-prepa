#nose que se podria poner en el input

"""
Crea un programa que permita llevar un registro de estudiantes y sus calificaciones. 
El programa debe permitir al usuario realizar las siguientes operaciones:

Agregar estudiantes y sus calificaciones al registro.
Buscar la calificación de un estudiante en particular.
Mostrar todas las calificaciones almacenadas en el registro.
Calcular y mostrar el promedio de calificaciones de todos los estudiantes.
Salir del programa.
"""
#alumnos=lista de diccionarios {nombre_alumno y su calificacion}
lista_alumnos=[]
def caso_1():
    nombre=input("Ingrese el nombre del alumno: ")
    while True:
        nota=int(input("Ingrese su calificacion: "))
        if nota<1 or nota>10:
            print("ingreso incorreto, vuelva a intentar")
        else:
            break
    lista_alumnos.append({"Alumno":nombre, "Calificacion":nota})

def caso_2():
    buscar_alumno=input("Ingrese el nombre del alumno para obtener su calificacion: ")
    encontrado=False
    for alumno in lista_alumnos:
        if buscar_alumno == alumno["Alumno"]:
            encontrado=True
            break
    if encontrado:
        print("La nota del alumno es: ",alumno["Calificacion"])
    else:
        print("El alumno que busca no esa registrado")
#otra opcion es poner el print de nota seguido del encontrado=true (para no usar break)
#y despues el if seria (not encontrado) y la sentencia que esta ahora en el else

def caso_3():
    cant_alumnos=len(lista_alumnos)
    prom=0
    for alumno in lista_alumnos:
        prom+= alumno["Calificacion"]
    prom= prom/cant_alumnos
    print("El promedio de calificaciones general es de ",prom,)




while True:
    print("\n\n1- Agregar estudiante y su calificacion")
    print("2- Buscar calificacion en particular")
    print("3- Promedio de calificaciones general")
    print("4- Salir")
    option=int(input("Ingrese una opcion: "))
    if option==1:
        caso_1()
    elif option==2:
        caso_2()
    elif option==3:
        caso_3()
    elif option==4:
        print("Que tenga buen dia\n")
        break
    else:
        print("Ingreso una opcion incorrecta, vuelva a intentar\n")
