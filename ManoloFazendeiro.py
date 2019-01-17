def colher(M, A):
    T = 0
    for i in range(A[0]-1,A[2]):
        for j in range(A[1]-1,A[3]):
            T += M[i][j]
            M[i][j] = 0
    return M, T

O = int(input())
M = [list(map(int,input().split())) for i in range(O) ]
C = int(input())
AC = [list(map(int,input().split())) for i in range(C) ]
Tot = 0
for i in range(len(AC)):
    M,T = colher(M, AC[i])
    Tot+=T
print(Tot)
