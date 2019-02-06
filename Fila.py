def Operacao(Tipo, Posicao, arg01, Lista):
    if Tipo == 0:
        Lista.insert(Posicao,arg01)
    else:
        limite = Lista[Posicao - 1] + arg01
        for i in range(Posicao-2,-1,-1):
            if Lista[i] > limite:
                return i + 1
        return 0

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
Op = [ list(map(int,input().split())) for i in range(Q)]
R =  [ Operacao(t[0],t[1],t[2],A) for t in Op ]
R = [ i for i in R if i is not None]
print(*R, sep='\n')
