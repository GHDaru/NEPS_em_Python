N = list(map(float,input().split()))
N.sort()
print('{:.1f}'.format(sum(N[1:(len(N)-1)])))