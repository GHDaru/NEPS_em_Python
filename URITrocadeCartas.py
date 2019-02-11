A,B = list(map(int,input().split()))
R = []
while A!=0 and B!=0:
    CA = set(map(int,input().split()))
    CB = set(map(int,input().split()))
    #Cartas exclusivas de A
    CEA = CA.difference(CB)
    #Cartas exclusivas de B
    CEB = CB.difference(CA)
    #O menor conjunto é o máximo de trocas
    R.append(min(len(CEA),len(CEB)))
    A,B = list(map(int,input().split()))
print(*R, sep='\n')