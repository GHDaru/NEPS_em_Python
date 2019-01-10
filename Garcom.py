N =  int(input())
cont = 0
for i in range(N):
    V = list(map(int,input().split()))
    cont+= V[1] if V[0]>V[1] else 0
print(cont)
