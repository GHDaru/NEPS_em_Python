N,S = list(map(int,input().split()))
Menor = S
Saldo = S
for i in range(N):
    M = int(input())
    S += M
    Menor = S if S < Menor else Menor
print(Menor)