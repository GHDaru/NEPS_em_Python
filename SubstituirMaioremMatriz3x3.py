Matriz = [ [int(input()) for i in range(3)] for j in range(3) ]
max = Matriz[0][0]
for i in range(3):
    for j in range(3):
        if max < Matriz[i][j]:
            max = Matriz[i][j]
for i in range(3):
    for j in range(3):
        Matriz[i][j] = str(Matriz[i][j]) if Matriz[i][j]!=max else "-1"
for i in range(3):
    print(' '.join(Matriz[i]))
