V = []
#V[0] = Quantidade de posições
#V[1] = Posição do Disco Voador
#V[2] = Posição do Avião
for i in range(3):
    V.append(int(input()))
#Cálculo
if V[2] <= V[1]:
    Apertos = V[1] - V[2]
else:
    Apertos = V[0] - V[2] + V[1]
    #Quanto falta para ir até o final + a posição do disco
print(Apertos)