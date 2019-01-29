def troca(Cima, Baixo, i , j):
    CimaFinal = Cima[0:i] + Baixo[i:j+1] + Cima[j+1:len(Cima)]
    BaixoFinal = Baixo[0:i] + Cima[i:j+1] + Baixo[j+1:len(Baixo)]
    return CimaFinal, BaixoFinal

N,NT = list(map(int,input().split()))
Cima = list(map(int,input().split()))
Baixo = list(map(int,input().split()))
Trocas = [ list(map(int,input().split())) for i in range(NT)]
for T in Trocas:
    Cima, Baixo = troca(Cima, Baixo, T[0]-1, T[1]-1)
print(*Cima)