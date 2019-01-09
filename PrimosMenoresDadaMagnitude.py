#http://marathoncode.blogspot.com/2012/03/numeros-primos-iii.html
#https://tiagomadeira.com/2007/06/crivo-de-eratostenes/

def crivo_erastostenes(N,crivo):
    crivo[1]=True
    for i in range(1,N+1):
        if not crivo[i]:
            j = 2
            while i*j<=N:
                crivo[i*j] = True
                j+=1
    return crivo
N = int(input())
crivo = list(range(0,N+1))
crivo = [False] * (N + 1)
#print(crivo)
crivo = crivo_erastostenes(N,crivo)
for i in range(1,N+1):
    if not crivo[i]:
        print(i, end=' ')