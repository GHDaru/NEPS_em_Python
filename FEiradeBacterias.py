import math
Q = int(input())
Catalogo = [ list(map(int,input().split())) for i in range(Q) ]
Qln = [ C[1] * math.log(C[0]) for C in Catalogo]
print(Qln.index(max(Qln)))

