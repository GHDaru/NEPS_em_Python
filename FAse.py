N = int(input())
K = int(input())
V = [ int(input()) for i in range(N)]
V.sort(reverse = True)
Ultimo = V[K-1]
cont = K
while cont<N:
    if V[cont] != Ultimo:
        break
    cont+=1
print(cont)