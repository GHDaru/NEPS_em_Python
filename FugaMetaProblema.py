def DFS(L,C,LS,CS,QL,QC,Custo):
    global Otimo
    Lmap = (L-1)//2
    Cmap = (C-1)//2
    Grade[Lmap][Cmap]=1
    if L==LS and C==CS:
        Otimo = max(Otimo,Custo)
    else:
        for i in range(4):
            NL = L + DL[i]
            NC = C + DC[i]
            if NL>=1 and NL<=QL and NC>=1 and NC<=QC:
                if Grade[(NL-1)//2][(NC-1)//2]==0:
                    DFS(NL, NC, LS, CS, QL,QC,Custo + 2)
    Grade[Lmap][Cmap]=0

def label(L):
    return '{}-{}'.format(L[0],L[1])

arq = open('Fuga.txt', 'w')
DL = [ 0, 0, 2, -2]
DC = [ 2,-2, 0, 0]
Linha = dict()
for L in [3,5,7,9,11]:
    Coluna = dict()
    for C in [3,5,7,9,11]:
        P = [[i,j] for j in  range(1,C+1,2) for i in range(1,L+1,2)]
        Entrada = dict()
        for E in range(len(P)-1):
            Saida = dict()
            for S in range(E+1,len(P)):
                #print(L,C,P[E],P[S])
                Custo = 1
                Otimo = 0
                Grade = [ [0 for j in range((C+1)//2)] for i in range((L+1)//2) ]
                DFS(P[E][0],P[E][1],P[S][0],P[S][1],L,C,Custo)
                Saida[label(P[S])] = Otimo
            Entrada[label(P[E])] = Saida
        Coluna[C] = Entrada
    Linha[L] = Coluna
#print(Linha)
arq.write(str(Linha))
arq.close()
