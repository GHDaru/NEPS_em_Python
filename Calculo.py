M,N = list(map(int,input().split()))
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
if M < N:
    X = X + [0]*(N-M)
else:
    Y = Y + [0]*(M-N)
R = [0]*len(X)
V = 0
for i in range(max(M,N)-1,-1,-1):
    R[i] = (X[i]+Y[i]+V) % 2
    V = (X[i]+Y[i]+V) // 2
print(*R,sep=' ')

