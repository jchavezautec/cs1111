nAlumnos = int(input("Numero de alumnos: "))
nNotas  = int(input("Numero de notas por alumno: "))

alumno_actual = 1

while alumno_actual <= nAlumnos:
    nota_actual = 1
    suma = 0
    print("\nAlumno %d"%(alumno_actual))

    while nota_actual <= nNotas:
        nota = float(input("Nota %d: "%(nota_actual)))
        while nota < 0 or nota > 20:
            nota  = float(input("Nota %d: "%(nota_actual)))
        suma += nota
        nota_actual = nota_actual + 1

    promedio = suma / nNotas
    print("El promedio para el alumno %d es %.2f"%(alumno_actual, promedio))    
    alumno_actual = alumno_actual + 1

print("Fin.")
