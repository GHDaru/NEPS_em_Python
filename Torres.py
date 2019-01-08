Ordem = int(input())
Matriz = [list(map(int,input().split())) for j in range(Ordem)]
#for i in range(Ordem):
#    Matriz.append(list(map(int,input().split())))
#Monta a Matriz soma
SL = [0 for i in range(Ordem)]
SC = [0 for i in range(Ordem)]
#Calcula soma das linhas
for i in range(Ordem):
    SL[i] = sum(Matriz[i][:])
#Calcula soma das colunas
for j in range(Ordem):
    SC[j] = sum([Matriz[k][j] for k in range(Ordem)])
#Varre para encontrar maior valor
Max = 0
for i in range(Ordem):
    for j in range(Ordem):
        Soma = SL[i]+ SC[j] - 2*Matriz[i][j]
        if Max < Soma:
            Max = Soma
print(Max)

