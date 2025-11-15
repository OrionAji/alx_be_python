rows = 1
column = 9
while rows <= 5:
    for i in {1, 3, 5, 7, 9}:
        print(" " * column + "*" * i)
        rows += 1
        column -= 1
    