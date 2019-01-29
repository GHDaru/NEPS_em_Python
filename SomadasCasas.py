def  buscaCasas(x, vetor):
    ini = 0
    fim = len(vetor)-1
    #Procura pela localização das casas com soma x
    #teste dos extremos
    if vetor[0] + vetor[1] == x: return vetor[0:2]
    if vetor[-2] + vetor[-1] == x: return vetor[-2:]
    while ini<=fim:  # enquanto houver algum elemento no intervalo
        meio=(ini+fim)//2 #meio igual a media de início e fim, arredondada para baixo
        soma = vetor[meio]+vetor[meio+1]
        if soma == x:
            return vetor[meio:meio+2]
        ini = meio + 1 if x>soma else ini # se o número está na frente, olho para a metade depois de meio
        fim = meio - 1 if x<soma else fim #se o número está atrás, olho para a metade antes de meio

#C = número de  casas
C = int(input())
# Número das casas
N = [int(input()) for i in range(C)]
# S = Soma dos valores das casas
S = int(input())
Casas = buscaCasas(S,N)
print(*Casas)