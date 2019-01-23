def Campeao(Resultados, Sistema):
    #Para cada resultado acumular a pontuação
    Pontuacao = [0]*len(Resultados[0])
    for R in Resultados:
        for i in range(0,len(R)):
            if R[i] < len(Sistema):
                Pontuacao[i] += Sistema[R[i]]
    Pontuacao =dict( list(zip(list(range(1,len(Pontuacao)+1)) , Pontuacao)))
    Pontuacao = sorted(Pontuacao.items(), key = lambda x: x[1], reverse = True)
    ScoreCampeao = Pontuacao[0][1]
    Campeoes = [ Pontuacao[0][0] ]
    i = 1
    while i < len(Pontuacao) and Pontuacao[i][1] == ScoreCampeao:
        Campeoes.append(Pontuacao[i][0])
        i+=1
    return Campeoes

#Leitura do número de grandes prêmios G e número de pilotos P
I = []
G,P = list(map(int,input().split()))
while G!=0:
    #Leitura dos resultados
    R = [ list(map(int,input().split())) for i in range(G)]
    #Número de sistemas de pontuação
    S = int(input())
    #Armazenagem dos sistemas de pontuação
    M = []
    for i in range(S):
        M.append(list(map(int,input().split())))
    for m in M:
        C = Campeao(R, m)
        I.append( C )
    G, P = list(map(int, input().split()))
for i in I:
    print(*i)
#print(G,P,R,S,M)