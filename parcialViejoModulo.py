def seleccionar_curso():
    cursos = ["PHP", "Python", "C#", "HTML y CSS", "Java", "JS", "Ruby", "Git"]
    print("Selecciona un curso:")
    for i, curso in enumerate(cursos):
        print(f"{i+1}. {curso}")
    opcion = int(input("Ingresa el número del curso: "))
    return cursos[opcion-1]