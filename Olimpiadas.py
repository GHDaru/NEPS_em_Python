#consulta https://www.geeksforgeeks.org/python-sort-list-of-list-by-specified-index/
#https://www.geeksforgeeks.org/python-list-sort/
NP,NM = map(int, input().split())
#Leitura dos resultados das modalidades
Rank = [ list(range(1,NP+1)) ] + [[0]*NP]*4
Rank = [[linha[i] for linha in Rank] for i in range(len(Rank[0]))]
#print(Rank)
for i in range(NM):
    R = list(map(int,input().split()))
    #Acumula as medalhas
    for j in range(len(R)):
        Rank[R[j]-1][j+1]+=1
#Cria um número índice usando  base NP (Número de Países) com quatro dígitos
#Ouro * NP^3 + Prata *  NP^ 2 + Bronze * NP + Código do País
for i in range(NP):
    Rank[i][4] =  Rank[i][1]*(NP**3) + Rank[i][2]*(NP**2) + Rank[i][3]*(NP) + (NP - Rank[i][0] -1)
#print(Rank)
Rank.sort(key = lambda Rank: Rank[4], reverse = True)
print(*([linha[0] for linha in Rank]), sep=' ')

