import numpy as np

N = int(input())
L = np.array(list(map(int,input().split())))
P = np.linspace(0,len(L),len(L), endpoint=False, dtype=int)
P0 = P[L==0]
pos = 0
for i in range(0,len(L)):
    #duas exceções: antes do primeiro e após o último
    if i <= P0[0]:
        L[i] = P0[0]-i
    elif i >= P0[-1]:
        L[i] = i - P0[-1]
    else:
        L[i] = min(i-P0[pos-1], P0[pos]-i)
    if i == P0[pos] and pos<len(P0)-1:
        pos+=1
print(*L, sep=' ')
#print(P)
#print(P0)