M,N = list(map(int,input().split()))
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
if M < N:
    X = X + [0]*(N-M)
else:
    Y = Y + [0]*(M-N)
R = [0]*len(X)
V = 0
Descartar = 0
PrimeiroUm = False
for i in range(max(M,N)-1,-1,-1):
    R[i] = (X[i]+Y[i]+V) % 2
    V = (X[i]+Y[i]+V) // 2
    Descartar += 1 if R[i]==0 and not PrimeiroUm else 0
    PrimeiroUm = PrimeiroUm or R[i]==1
if len(R)==Descartar:
    print(0)
else:
    R =  R[0:len(R)-Descartar]
    print(*R,sep=' ')

