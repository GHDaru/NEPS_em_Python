Ordem = int(input())
Matriz = [list(map(int,input().split())) for j in range(Ordem)]
#for i in range(Ordem):
#    Matriz.append(list(map(int,input().split())))
#Monta a Matriz soma
Max = 0
S = [[0 for i in range(Ordem)] for j in range(Ordem)]
for i in range(Ordem):
    for j in range(Ordem):
        somalinha = sum(Matriz[i][:]) - Matriz[i][j]
        somacoluna = sum([Matriz[k][j] for k in range(Ordem)]) - Matriz[i][j]
        S[i][j] = somalinha + somacoluna
        if Max < S[i][j]:
            Max = S[i][j]
print(Max)

