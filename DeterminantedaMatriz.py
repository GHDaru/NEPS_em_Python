Ordem = 3
M = [list(map(int,input().split())) for j in range(Ordem)]

Determinante = M[0][0]*M[1][1]*M[2][2] + M[1][0]*M[2][1]*M[0][2] +  M[2][0]*M[0][1]*M[1][2] -\
               M[0][0]*M[1][2]*M[2][1] - M[1][1]*M[0][2]*M[2][0] -  M[2][2]*M[1][0]*M[0][1]

print(Determinante)