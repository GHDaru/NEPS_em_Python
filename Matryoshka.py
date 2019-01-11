N = int(input())
V = list(map(int,input().split()))
B = set()
##Primeira  posição - se maior que o próximo então está fora de  ordem
if V[0]>V[1]:
    B.add(V[0])
for i in range(1,len(V)-1):
##Para as demais se maior que o próximo e o próximo maior que anterior
    if V[i]>V[i+1]:
        if V[i+1]>V[i-1]:
            B.add(V[i])
        else:
            B.add(V[i+1])
print(len(B))
if len(B)>0:
    print(*B, sep=' ')

