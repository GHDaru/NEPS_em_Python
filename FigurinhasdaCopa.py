Ent = list(map(int, input().split()))
N, CQ, M = Ent[0], Ent[1], Ent[2]
Carimbadas = list(map(int, input().split()))
Compradas = list(map(int,input().split()))
ConjComp = set()
for i in Compradas:
    ConjComp.add(i)
QtdeCarimbadas = 0
for i in ConjComp:
    if i in Carimbadas:
        QtdeCarimbadas+=1
print(CQ - QtdeCarimbadas)