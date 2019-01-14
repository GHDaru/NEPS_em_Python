#https://olimpiada.ic.unicamp.br/passadas/OBI2002/programacao/
def addNode(G,N):
    G["Nós"].add(N)
    return G

def addEdge(G,E):
    G = addNode(G,E[0])
    G = addNode(G,E[1])
    G["Arcos"].append(E)
    return G

def InitGrafo():
    return {"Nós":set(), "Arcos":[]}

def readEdge(G):
    N = list(input().split())
    return addEdge(G,N)

def Trans(Mat):
    A = [[linha[i] for linha in Mat] for i in range(len(Mat[0]))]
    return A

def Grau(G):
    A = [ list(G["Nós"]) ] + [ [0]*len(G["Nós"]) ]
    A = Trans(A)
    A = dict(A)
    for a in G["Arcos"]:
        A[a[0]]+=1
        A[a[1]]+=1
    return dict(sorted(A.items(), key=lambda kv: kv[1]))

def MaiorGrau(G):
    GrafoList = Grau(G)
    #print(GrafoList)
    GrafoList = list(GrafoList.items())
    #print(GrafoList)
    MaiorQtde = GrafoList[-1][1]
    #print(MaiorQtde)
    MaiorLista = [GrafoList[-1][0]]
    #print(MaiorLista)
    for i in range(len(GrafoList)-2,-1,-1):
        #print(GrafoList[i][1])
        if GrafoList[i][1] == MaiorQtde:
            MaiorLista.append(GrafoList[i][0])
        else:
            break
    MaiorLista.reverse()
    return MaiorLista

A,V = list(map(int,input().split()))
cont = 1
while A!=0:
    #print(A,V)
    G = InitGrafo()
    for i in range(V):
        G = readEdge(G)
    #print(Grau(G))
    Resultados = map(int,MaiorGrau(G))
    Resultados = sorted(Resultados)
    #print(Resultados)
    print("Teste",cont)
    print(*Resultados, sep = ' ')
    print()
    #for i in MaiorGrau(G):
    #    print(int(i))
    A, V = list(map(int, input().split()))
    cont+=1