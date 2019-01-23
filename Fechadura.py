N, M = list(map(int,input().split()))
P = list(map(int,input().split()))
Q = 0
Resto = 0
i = 0
#print(Delta)
while i < len(P)-1:
    Delta = M - P[i]
    P[i] += Delta
    Q += abs(Delta)
    P[i+1] += Delta
    i+=1

print(Q)


