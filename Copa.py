#O = list(map(int,input().split()))
O = list(range(1,17))
C = ['final', 'semifinal', 'quartas','oitavas']
K = int(input())
L = int(input())
MasterKung = "{0:b}".format(O.index(K)+16)#Força o binário a "ligar" o 5o Dígito (Caso as posições sejam menores que 8)
MasterLu = "{0:b}".format(O.index(L)+16)
for i in range(1,len(MasterKung)):
    if MasterKung[i]!=MasterLu[i]:
        Confronto = C[i-1]
        break
print(Confronto)