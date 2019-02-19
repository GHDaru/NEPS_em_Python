A,B = list(map(int,input().split()))
CA = set(map(int,input().split()))
CB = set(map(int,input().split()))
#Cartas exclusivas de A
#ou  seja A - A /\ B
CEA = CA.difference(CB)
#Cartas exclusivas de B
#ou seja B - A/\B
CEB = CB.difference(CA)
#O menor conjunto é o máximo de trocas
R = min(len(CEA),len(CEB))
print(R)