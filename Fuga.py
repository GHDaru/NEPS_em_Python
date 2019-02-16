#import time

def dfs(l,c):
    Grade[l][c] = 1
    global custo
    global resp
    global cont
    cont+=1
    custo += 1
    print(*(['\t'] * custo), '-->', l +  1, c +  1, custo,  resp, cont)
    if custo > InVisited[l*M + c]:
        InVisited[l * M + c] = custo
    #print(RespVisited)
    if l==(LS-1) and c==(CS-1): #chegue na saída
        resp = max(resp,custo) #se rota maior, assume como resposta
    else: #vai caminhar em todas as direções
        for i in range(4):
            nl = l + dl[i] #nova linha igual a linha mais delta
            nc = c + dc[i] #nova coluna igual a coluna mais delta
            if nl>=0 and nc>=0 and nl<N and nc<M: #caminhada se encontra dentro do tabuleiro
                if Grade[nl][nc] == 0 and custo >= RespVisited[nl*M + nc]: #novo ponto ainda não foi visitado ou já foi encontrado um caminho melhor
                    #print(*Grade,sep='\n')
                    #print(custo,resp, l,c)
                    custo+=1
                    #print(*(['\t']*custo),'Entrada:',custo, nl + 1, nc + 1)
                    dfs(nl,nc) #visitar ponto
                    #print(*(['\t']*custo),'Saida:',  custo, nl + 1,nc +  1)
                    custo-=1
    print(*(['\t'] * custo), '<--', l + 1, c +  1, custo, resp, cont)
    custo -= 1
    Grade[l][c] = 0
dl = [ 0, 0, 2, -2]
dc = [ 2,-2, 0, 0]
custo = 0
resp = 0
cont = 0
N,M,  = list(map(int,input().split()))
LE,CE = list(map(int,input().split()))
LS,CS = list(map(int,input().split()))
InVisited = [0]*N*M
RespVisited = [0]*N*M
#inicio = time.time()
Grade = [ [ 1 if (((i+1) % 2 == 0) and ((j+1) % 2 == 0)) else 0 for i in range(N)]  for j in range(M) ]
#O número máximo é constante e dado por
#  Nos = N * M -> Número de nós
#  Baus = ((N-1)//2 * (M-1)//2 ) --> Número de baús
#  Como os baús são derrubados ocupam 2 lugares
#  Distancia = Nos - 2*Baus - 2 (onde o 2 representa os nós de início e fim)
#print( N*M - 2 * ((N-1)//2 * (M-1)//2) - 2)
dfs(LE-1,CE-1)
print(resp)
#Respostas.append([N,M,resp])
#print(N,M,resp)
print(resp,cont)
#fim = time.time()
#print(fim - inicio)
#print(*Respostas, sep = '\n')


