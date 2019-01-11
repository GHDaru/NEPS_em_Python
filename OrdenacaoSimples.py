N = int(input())
V = list(map(int,input().split()))
V.sort()
print(*V, sep=' ')