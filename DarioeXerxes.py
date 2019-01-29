#Armazena o resultado R[i][j] = 1 se i ganha de j ou 2 caso j ganhe de i, 0 é um resultado de empate
R=[[0, 1, 1, 2, 2], [2, 0 , 1 , 1, 2], [2, 2, 0, 1, 1], [1,2,2,0,1], [1,1,2,2,0]]
N = int(input())
J = [ list(map(int,input().split())) for i in range(N)]
#Determina o ganhador de cada rodada
G = [ 0,0 ]
for j in J:
    G[ R[j[0]][j[1]] - 1 ] += 1
print('dario' if G[0]>G[1] else 'xerxes')