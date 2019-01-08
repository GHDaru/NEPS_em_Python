N = int(input())
V = list(map(int,input().split()))
r = 'N'
for i in range(1,len(V)-1):
    if V[i] < V[i-1] and V[i]<V[i+1]:
        r = 'S'
print(r)