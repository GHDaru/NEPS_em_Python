V = []
#V[0] = Quantidade de posições
#V[1] = Posição do Disco Voador
#V[2] = Posição do Avião
for i in range(3):
    V.append(int(input()))
if V[0] == V[1]:
    Resp = V[2]
elif V[0] == V[2]:
    Resp = V[1]
else:
    Resp = V[0]
print(Resp)