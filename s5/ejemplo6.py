nGorink = int(input("Numero de gorinkianos: "))
nTomas  = 5

gorink_actual = 1

while gorink_actual <= nGorink:
    toma_actual = 1
    suma = 0
    print("\nGorinkiano %d"%(gorink_actual))

    while toma_actual <= nTomas:
        nota = float(input("Toma %d: "%(toma_actual)))
        suma += nota
        toma_actual = toma_actual + 1

    promedio = suma / nTomas
    print("El promedio para el Gorinkiano %d es %.2f"%(gorink_actual, promedio))    
    gorink_actual = gorink_actual + 1

    if promedio > 130:
        print("Es hipertenso :(")

print("Fin.")
