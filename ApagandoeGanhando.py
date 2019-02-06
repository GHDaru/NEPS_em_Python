def limpar(V,T):
    Apagados = 0
    #Inicializa pilha com último valor
    Pilha = []
    for i in V:
        if len(Pilha) !=0:
            while i > Pilha[-1] and Apagados < T:
                Apagados+=1
                Pilha.pop()
                if len(Pilha) == 0: break
        if len(Pilha) < len(V)-T: Pilha.append(i)
    return ''.join(Pilha)

N,T = list(map(int,input().split()))
R = []
while N!=0 and T!=0:
    V = list(str(input()))
    R.append(limpar(V,T))
    N, T = list(map(int, input().split()))

print(*R, sep = '\n')
