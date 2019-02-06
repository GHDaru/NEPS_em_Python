def ValidaExpressao( E ):
    Abre = ['(','[','{']
    Fecha = [')',']','}']
    Balanco = dict(zip(Fecha, Abre))
    Pilha = []
    Resp = 'S'
    for i in E:
        if i in Abre:
            Pilha.append(i)
        if i in Fecha:
            if len(Pilha) > 0:
                if Balanco[i]==Pilha[-1]:
                    Pilha.pop()
                else:
                    Resp = 'N'
                    break
            else:
                Resp = 'N'
                break
    if len(Pilha)>0:
        Resp = 'N'
    return Resp

N = int(input())
Expressoes = [str(input()) for i in range(N)]
R = list(map(ValidaExpressao, Expressoes))
print(*R, sep = '\n')

