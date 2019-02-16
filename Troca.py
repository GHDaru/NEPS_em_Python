
N,NT = list(map(int,input().split()))
Cima = list(map(int,input().split()))
Baixo = list(map(int,input().split()))
Operacoes = [0]*N
Resultado = [0]*N
Trocas = [ list(map(int,input().split())) for i in range(NT)]
for T in Trocas:
    Operacoes[T[0]-1] +=1
    if T[1] < N:
        Operacoes[T[1]] -=1
Resultado[0] = Operacoes[0]
for i in range(1,N):
    Resultado[i] =  Resultado[i-1] + Operacoes[i]

for i in range(N):
    print( Cima[i] if (Resultado[i]%2==0) else Baixo[i] , end = ' ')
