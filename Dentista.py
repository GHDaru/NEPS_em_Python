N = int(input())
C = [list(map(int,input().split())) for i in range(N)]
#print(C)
C.sort(key = lambda C: C[1])
Qtde = 1
Fim = C[0][1]
Current = 1
while Current < len(C):
    if C[Current][0] >= Fim:
        Fim = C[Current][1]
        Qtde+=1
    Current +=1
print(Qtde)