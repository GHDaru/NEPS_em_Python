
peso = dict()
def find(x):
        if Pai[x] == x:
            return x
        else:
            Pai[x] = find(Pai[x])
            return Pai[x]
def join(x,y):
    #Pai[find(x)] = find(y)
    x = find(x)
    y = find(y)

    if x==y:
        return
    if peso[x] < peso[y]:
        Pai[x]=y
    if peso[y]<peso[x]:
        Pai[y] = x
    if peso[x] == peso[y]:
        Pai[x]=y
        peso[y]+=1

N,K = list(map(int,input().split()))
Pai = [0]*(N+1)
OP = [ list(map(str,input().split())) for i in range(K)]
for i in range(1,N+1):
    Pai[i]=i
    peso[i]=0
#print(Pai)
#print(OP)
R = []
for i in OP:
    i[1] = int(i[1])
    i[2] = int(i[2])
    if  i[0]=='F':
        join(i[1], i[2])
    else:
        R.append('S' if find(i[1]) == find(i[2]) else 'N')

print(*R, sep = '\n')

