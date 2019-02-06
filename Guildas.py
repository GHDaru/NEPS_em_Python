peso = dict()
def find(x):
        if Pai[x] == x:
            return x
        else:
            Pai[x] = find(Pai[x])
            return Pai[x]
def join(x,y):
    #Pai[find(x)] = find(y)
    x = find(x)
    y = find(y)

    if x==y:
        return
    if peso[x] < peso[y]:
        Pai[x]=y
        #como o patriarca passa a ser y, então ele recebe a pontuação da Guilda de x
        Pontos[y-1]+=Pontos[x-1]
    if peso[y]<peso[x]:
        Pai[y] = x
        #como o patriarca passa a ser x, então ele recebe a pontuação da Guilda de y
        Pontos[x-1]+=Pontos[y-1]
    if peso[x] == peso[y]:
        Pai[x]=y
        # como o patriarca passa a ser y, então ele recebe a pontuação da Guilda de x
        Pontos[y - 1] += Pontos[x - 1]
        peso[y]+=1


Resp = []
N,K = list(map(int,input().split()))
while N!=0 and K!=0:
    Pai = [0]*(N+1)
    #Cada jogador tem um número de pontos e cada jogador no início é uma Guilda
    #A notação começa de 0, assim, o jogador 1 é a posição 0, e assim por diante.
    Pontos = list(map(int,input().split()))
    OP = [ list(map(int,input().split())) for i in range(K)]
    for i in range(1,N+1):
        Pai[i]=i
        peso[i]=0
    #print(Pai)
    #print(OP)
    R = 0
    for i in OP:
        if  i[0]==1:
            join(i[1], i[2])
        else:
            Guilda01 = find(i[1])
            Guilda02 = find(i[2])
            GuildaRafa = find(1)
            if Guilda01 == GuildaRafa and Pontos[Guilda01-1]>Pontos[Guilda02-1]:
                R+=1
            if Guilda02 == GuildaRafa and Pontos[Guilda02-1]>Pontos[Guilda01-1]:
                R+=1
    Resp.append(R)
    N, K = list(map(int, input().split()))

print(*Resp, sep = '\n')

