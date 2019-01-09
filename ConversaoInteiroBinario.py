N = int(input())
if N==0:
    print(0)
else:
    B = []
    while N > 0:
        B.append(N%2)
        N = N // 2
    B = B[::-1]
    print(*B,sep='')