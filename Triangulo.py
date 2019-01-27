T = list(map(int,input().split()))
T.sort(reverse=True)
print('S' if T[0] <= T[1]+T[2] or T[1]<T[2]+T[3] else 'N')
