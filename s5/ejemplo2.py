nFilas = int(input("Numero de filas: "))
nColum = nFilas

while nFilas < 1 or nFilas > 9:
    nFilas = int(input("Numero de filas: "))

fil_act = 1

while fil_act <= nFilas:
    col_act = 1
    while col_act <= fil_act:
        print(col_act, end="")
        col_act = col_act + 1
    print()
    fil_act = fil_act + 1

