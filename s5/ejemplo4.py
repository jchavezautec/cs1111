numero = int(input("Numero [mayor a 15]: "))

while numero <= 15:
    numero = int(input("Numero [mayor a 15]: "))

numero_actual = 1
factorial     = 1
while numero_actual <= numero:
    factorial = factorial * numero_actual
    print(numero_actual, factorial)
    numero_actual = numero_actual + 1
