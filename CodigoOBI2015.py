N =  int(input())
V = list(map(int, input().split()))
cont = 0
for i in range(N-2):
    if V[i] == 1 and V[i+1]==0 and V[i+2]==0:
        cont+=1
print(cont)