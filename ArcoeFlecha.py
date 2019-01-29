import numpy
def dist(T):
    return (T[0]**2 + T[1]**2)**(1/2)

N = int(input())
#C contém as coordenadas em formato de lista dos tiros
D = [ dist(list(map(int,input().split()))) for i in range(N) ]
#D contém as distâncias de cada tiro
#D = list(map(dist, C))
#Cálculo das penalidades
PT = 0
for j in range(1,N):
    for i in range(j):
        PT += 1 if D[i] <= D[j] else 0
print(PT)
#print(C)
#print(D)
