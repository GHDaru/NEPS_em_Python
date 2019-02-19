#leitura dos dados
#
# A primeira linha contém dois inteiros não negativos, P e S, que indicam respectivamente o comprimento em metros da praia e o número de sorveteiros.
# Seguem-se S linhas, cada uma contendo dois números inteiros U e V que descrevem o intervalo de trabalho de cada um dos sorveteiros,
# em metros contados a partir do início da praia.
#ideia de solucao: criar um vetor com os limites e para cada intervalo acrescentar 1 ao valor inicial e -1 ao valor final
#Exemplo:
#1000 3
# 10 400 [10 +1] [400 -1]
# 80 200 [80 +1] [200 -1]
# 400 1000 [400 +1] [1000 -1]
# Vetor ordenado: [10 +1, 80 +1, 200 -1, 400 0, 1000 -1],
# Vetor acumulado: [10 1, 80 2, 200 1, 400 1, 1000 0]
# Saída : Todos os valores 1 são início de intervalo e 0 são fim de intervalo.
# Assim a resposta é: 10 1000
P,S = list(map(int,input().split()))
A = [ list(map(int,input().split())) for i in range(S)]
V = dict()
for i in A:
    if i[0] in V:
        V[i[0]]+=1
    else:
        V[i[0]] = 1
    if i[1] in V:
        V[i[1]] -=1
    else:
        V[i[1]] = -1
#print(V)
R = list(V.keys())
R.sort()
#print(R)
Acum = 0
Resp = []
Ini = True
Fim = False
for i in R:
    Acum += V[i]
    #V[i] = Acum
    if (Acum >= 1 and Ini) or (Acum==0 and Fim):
        Resp.append(i)
        Ini = not Ini
        Fim = not Fim
#[print(i, V[i]) for i in V.keys() if V[i]==1]
#print(Resp)
if len(Resp) > 1:
    for i in range(0,len(Resp),2):
        print(Resp[i], Resp[i+1])
#print()
