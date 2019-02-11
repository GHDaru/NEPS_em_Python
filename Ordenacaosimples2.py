V = [int(input()) for i in range(10)]
V.sort()
print(*V, sep=' ')
V.reverse()
print(*V,sep=' ')