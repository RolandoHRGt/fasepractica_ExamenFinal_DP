from Estudiante import Estudiante
from Curso import Curso

cursos = []

while True:
    print("Opciones:")
    print("1. Inscribir estudiante en un curso")
    print("2. Crear un nuevo curso")
    print("3. Mostrar estudiantes inscritos en cursos")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        edad = int(input("Edad del estudiante: "))
        estudiante = Estudiante(nombre, edad)

        print("Cursos disponibles:")
        for i, curso in enumerate(cursos):
            print(f"{i + 1}. {curso.nombre} ({curso.codigo})")

        curso_index = int(input("Selecciona un curso por su número: ")) - 1
        cursos[curso_index].inscribir_estudiante(estudiante)
        
    elif opcion == "2":
        nombre_curso = input("Nombre del nuevo curso: ")
        codigo_curso = input("Código del nuevo curso: ")
        nuevo_curso = Curso(nombre_curso, codigo_curso)
        cursos.append(nuevo_curso)
        print(f"Curso '{nombre_curso}' ({codigo_curso}) creado con exito")

    elif opcion == "3":
        for curso in cursos:
            curso.mostrar_estudiantes()

    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")