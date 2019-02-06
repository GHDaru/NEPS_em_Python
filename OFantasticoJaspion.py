T = int(input())
for j in range(T):
    M,N = list(map(int,input().split()))
    Dicionario = dict()
    for i in range(M):
        key = str(input())
        value = str(input())
        Dicionario[key] = value
    #print(Dicionario)
    Texto = [ list(map(str,input().split())) for i in range(N) ]
    Linha = [ [(Dicionario[palavra] if palavra in Dicionario else palavra) for palavra in linha] for linha in Texto]
    S = [ ' '.join(saida) for saida in Linha ]
    print(*S, sep = '\n')
    print()


