N = int(input())
R = [ int(input()) for i in range(N)]
F = list(range(1,13))
C = [0] * 12
for i in R:
    C[i-1]+=1
#Gera tabela
T = list(zip(F,C))
#Ordena Tabela pelo número de ocorrências
T.sort(key = lambda x: x[1], reverse = True)
#Gera o vetor com os maiores valores
M = []
M.append(T[0][0])
MO = T[0][1]
i = 1
while i < len(T) and T[i][1]== MO:
    M.append(T[i][0])
    i+=1
print(*M)
