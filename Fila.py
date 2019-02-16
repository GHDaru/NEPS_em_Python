def Operacao(Tipo, Posicao, arg01, Lista):
    if Tipo == 0:
        Lista.insert(Posicao,arg01)
    else:
        limite = Lista[Posicao - 1] + arg01
        for i in range(Posicao-2,-1,-1):
            if Lista[i] > limite:
                return i + 1
        return 0

N = int(input())
H = list(map(int,input().split()))
Q = int(input())
Op = [ list(map(int,input().split())) for i in range(Q)]
R = []
for i in Op:
    #print(i)
    if i[0]==0:
        H.insert(i[1],i[2])
        #print(H)
    else:
        check = i[1]-2
        limite = H[i[1]-1]+i[2]
        ok = False
        while check >=0:
            if H[check]>limite:
                R.append(check+1)
                ok = True
                break
            check-=1
        if not ok:
            R.append(0)
    #print(R)
print(*R,sep='\n')

