def addalg(N,A):
    for i in N:
        A[int(i)]+=1
    return A

A = [0,0,0,0,0,0,0,0,0,0]
N = int(input())
for i in range(0,N):
    V =  input()
    A = addalg(V,A)

for i in range(0,10):
    print(i,'-',A[i])

