N = int(input())
H = [int(input()) for i in range(N) ]
M = H[0]
P = []
C = 0
for i in range(1,len(H)):
    if H[i] < M and i<len(H)-1:
        P.append(H[i])
    else:
        M = H[i]
        while len(P)>0:
            if P[-1] < H[i]:
                C+=1
            P.pop()
print(C)

