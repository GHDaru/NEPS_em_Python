N =  int(input())
V = [int(input()) for i in range(N)]
M = V[:]
for i in range(0,N-1):
    M[i]+=V[i+1]
    M[i+1]+=V[i]
print(*M,sep='\n')