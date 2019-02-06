C,N = list(map(int,input().split()))
Instalados = dict( [list(map(int,input().split())) for i in range(C) ] )
Net = dict()
for i in range(N):
    P,V = list(map(int,input().split()))
    if P in Instalados:
        if V > Instalados[P]:
            if P in Net:
                if P > Net[P]:
                    Net[P] = V
            else:
                Net[P]=V

R = ['{} {}'.format(key,value) for (key,value) in sorted(Net.items())]
print(*R, sep = '\n')
