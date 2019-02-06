def f(n,k,m,A,F,R):
    if R[k]!=None:
        return R[k]
    R[k] = 0
    for i in range(1,n+1):
        R[k] += A[i]*f(n,k-i,m,A,F,R)
    return (R[k] % m)

N,K,M = list(map(int,input().split()))
A = [None] + list(map(int,input().split()))
F = [None] + list(map(int,input().split()))
R = [None] + F[1:] + [None]*(K-N)
Fk = f(N,K,M,A,F,R)
print(Fk)



