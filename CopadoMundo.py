E = [chr(i) for i in range(ord('A'),ord('P')+1)]
R = [ list(map(int,input().split())) for i in range(15)]
for i in range(15): #varre os resultados
    Jogo = R.pop(0)  #Extrai o resultado da fila
    Jogador01 = E.pop(0) #Extrai o time 01 da fila de times
    Jogador02 = E.pop(0) #Extrai o time 02 da fila de times
    #Insere no Final da fila o ganhador
    E.append(Jogador01 if Jogo[0]>Jogo[1] else Jogador02)
    #print(Jogo,R,E, sep='\n')
print(*E)

