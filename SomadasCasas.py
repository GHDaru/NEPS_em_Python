def  busca(ini,fim,Soma):
    P = (ini+fim)//2
    S = N[P]+N[P+1]
    if ini > fim:
        return [0,0]
    if S == Soma:
        return N[P:P+2]
    if S<Soma:
        return busca(P+1,fim,Soma)
    else:
        return busca(ini,P-1,Soma)

#C = número de  casas
C = int(input())
# Número das casas
N = [int(input()) for i in range(C)]
# S = Soma dos valores das casas
S = int(input())
Casas = busca(0,C-2,S)
print(*Casas)