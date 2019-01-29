def  buscaFaixa(x, vetor):
    ini = 0
    fim = len(vetor)-1
    #Verifica se o valor não é menor que o início ou maior igual ao fim
    if x < vetor[0]: return 0
    if x >= vetor[-1]: return len(vetor)
    #Procura pelo intervalo
    while ini<=fim:  # enquanto houver algum elemento no intervalo
        meio=(ini+fim)//2 #meio igual a media de início e fim, arredondada para baixo
        if x >= vetor[meio] and x<vetor[meio+1]:
            return meio+1# se achei o número, retorno o valor de meio
        ini = meio + 1 if x>vetor[meio] else ini # se o número está na frente, olho para a metade depois de meio
        fim = meio - 1 if x<vetor[meio] else fim #se o número está atrás, olho para a metade antes de meio

#N = número de  faixas,  O = número de ogros
N, O =  list(map(int,input().split()))
# #Limites das faixas
F = list(map(int,input().split()))
# #Valores  dos prêmios
P = list(map(int,input().split()))
# #Força de cada Ogro
M = list(map(int,input().split()))
R = [P[buscaFaixa(m,F)] for m in M]
print(*R)
