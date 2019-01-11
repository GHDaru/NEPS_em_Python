N = int(input())
Matriz = [ list(map(int,input().split())) for i in range(N) ]
SC = [0 for i in range(N)]
SL = [0 for i in range(N)]
DP = 0
DS = 0
#Calcula soma das colunas e a soma das linhas
for i in range(N):
    SC[i] = sum([Matriz[k][i] for k in range(N)])
    SL[i] = sum([Matriz[i][k] for k in range(N)])
    DP+=Matriz[i][i]
    DS+=Matriz[i][N-i-1]

Iguais = sum([SC[i]==DP for i in range(N)]) + sum([SL[i]==DP for i in range(N)]) + (DS==DP)

print( DP if Iguais == 2*N+1 else -1)