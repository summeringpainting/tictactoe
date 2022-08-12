import numpy as np

field = np.empty(([3, 3]), dtype="str")

field[:] = '-'

while True:
    print(field)

    Xcolumn = int(input("You're X's what row?"))
    Xrow = int(input("Now what column?"))

    if field[Xcolumn, Xrow] == '-':
        field[Xcolumn, Xrow] = "X"

    if ["X", "X", "X"] in field.tolist():
        print("X's WIN!!!")
        break

    elif ["X", "X", "X"] in field.T.tolist():
        print("X's WIN!!!")
        break

    elif field[0, 0] and field[1, 1] and field[2, 2] == "X":
        print("X's WIN!!!")
        break

    elif field[0, 2] and field[1, 1] and field[2, 0] == "X":
        print("X's WIN!!!")
        break

    print(field)

    Ocolumn = int(input("You're O's what row?"))
    Orow = int(input("Now what column?"))

    if field[Ocolumn, Orow] == '-':
        field[Ocolumn, Orow] = "O"

    if ["O", "O", "O"] in field.tolist():
        print("O's WIN!!!")
        break

    elif ["O", "O", "O"] in field.T.tolist():
        print("O's WIN!!!")
        break

    elif field[0, 0] and field[1, 1] and field[2, 2] == "O":
        print("0's WIN!!!")
        break

    elif field[0, 2] and field[1, 1] and field[2, 0] == "O":
        print("0's WIN!!!")
        break

    print(field)

