def limites(L,C,M,N):
    return (L>=0 and C>=0 and L<M and C<N)

def check(L,C):
    global N
    Jogador = T[L][C]
    for i in range(8): #Direções
        Sucesso = True
        for j in range(1,5): #repetições
            NL = L + j*DL[i]
            NC = C + j*DC[i]
            #Verifica se está dentro dos limites
            if not limites(NL,NC,N,N):
                Sucesso =  False
                break
            elif T[NL][NC] != Jogador:
                Sucesso = False
                break
        if Sucesso:
            return True
    return False


DL = [0,  0, 1, -1, 1,  1, -1, -1]
DC = [1, -1, 0,  0, 1, -1,  1, -1]
T = [ list(map(int,input().split())) for i in range(15)]
N = 15
i=0
j=0
t=0
Cor = 0
while True:
    Cor = T[i][j]
    if Cor !=0:
        R = check(i,j)
        if R:
            break
    t += 1
    i = t//N
    j = t%N
    if t >= N * N:
        Cor = 0
        break
print(Cor)
#print(i,j)







