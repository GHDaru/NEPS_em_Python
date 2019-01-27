N = list(map(int,input().split()))
N.sort()
Diff = abs((N[-1]+N[0]) - (N[1]+N[2]))
print(Diff)