A,B = list(map(int,input().split()))
CA = set(map(int,input().split()))
CB = set(map(int,input().split()))
#Cartas exclusivas de A
CEA = CA.difference(CB)
#Cartas exclusivas de B
CEB = CB.difference(CA)
#O menor conjunto é o máximo de trocas
R = min(len(CEA),len(CEB))
print(R)