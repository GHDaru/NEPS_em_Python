N = int(input())
L = list(map(int,input().split()))
P = []
for i in  range(0,len(L)):
    if L[i]==0:
        P.append(i)
pos =  0
for i in range(0,len(L)):
    #duas exceções: antes do primeiro e após o último
    if i <= P[0]:
        L[i] = P[0]-i
    elif i >= P[-1]:
        L[i] = i - P[-1]
    else:
        L[i] = min(i-P[pos-1], P[pos]-i)
    if i == P[pos] and pos<len(P)-1:
        pos+=1
for i in range(0, len(L)):
    L[i] = L[i] if L[i]<=9 else 9
print(*L, sep=' ')