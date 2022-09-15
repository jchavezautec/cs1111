nFilas = int(input("Numero de filas: "))
nColum = nFilas

while nFilas < 1 or nFilas > 9:
    nFilas = int(input("Numero de filas: "))

fil_act = 1

while fil_act <= nFilas:
    col_act = 1
    print_diag = nFilas

    while col_act <= nColum:
        if col_act <= (nFilas - fil_act):
            print(0, end="")
        else:
            print(print_diag, end="")
            print_diag = print_diag - 1
        col_act = col_act + 1
    print()
    fil_act = fil_act + 1

