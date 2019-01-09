def fibo(N):
    if N == 1:
        Result = 0
    elif N == 2:
        Result = 1
    else:
        V = [0,0]
        V[0] = 0
        V[1] = 1
        for i in range(3,N):
            V[0],V[1] = V[1],V[0]+V[1]
        Result = V[1]
    return Result

def fiboprint(N):
    if N == 1:
        V = [0]
    elif N == 2:
        V = [0,1]
    else:
        V = [0,1]
        for i in range(3,N+1):
            V.append(V[i-3]+V[i-2])
    return V

N = int(input())
V = fiboprint(N)
for i in V:
    print(i, end=' ')