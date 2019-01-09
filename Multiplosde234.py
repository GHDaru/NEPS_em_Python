N = int(input())
V = []
M = [0,0,0]
T = [2,3,4]
for i in range(N):
    V.append(int(input()))
    for j in range(0,3):
        M[j]+= 1 if V[i]%T[j]==0 else 0
for i in range(0,3):
    print(M[i])
