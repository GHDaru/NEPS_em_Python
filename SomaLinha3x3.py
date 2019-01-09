V = []
for i in range(9):
    V.append(int(input()))
SL=[0,0,0]
for i in range(3):
    SL[i] = sum(V[i*3:(i+1)*3])
    print('Linha {}: {}'.format(i,SL[i]))