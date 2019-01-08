N = int(input())
dist = 0
for i in range(0,N):
    V = list(map(int,input().split()))
    dist += (V[3]-V[1])**2 + (V[2]-V[0])**2
print(dist)