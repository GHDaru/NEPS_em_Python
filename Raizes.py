N =  int(input())
V = list(map(float, input().split()))
print()
for i in range(N):
    print('{:.4f}'.format(V[i]**(1/2)))