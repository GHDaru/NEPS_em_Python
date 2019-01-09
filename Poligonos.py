#Answer https://mathoverflow.net/questions/96617/determine-if-you-can-build-a-polygon-from-segments

N = int(input())
V = list(map(int,input().split()))
V = sorted(V)
soma = sum(V)
P = 0
for i in range(len(V)-1,1,-1):
    #print(soma, V[i])
    if 2*V[i]< soma:
        P = i+1
        break
    soma -= V[i]
    #print(soma, V[i], P)
print(P)
#print(P if P > 2 else 0)