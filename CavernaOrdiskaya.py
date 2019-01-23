M, F = list(map(int,input().split()))
D = list(map(int,input().split()))
#Passo  0
# Quatro combinações
# D[i] com D[i+1]
# D[i] com F - D[i+1]
# F-D[i] com D[i+1]
# F-D[i] com F-D[i+1]
D[0] = D[0] if D[0] <= F-D[0] else F-D[0]
T =  D[0]
i = 1
while i < len(D):
    #Se ambos as medidas D[i] e F-D[i] são  menores que anterior impossível
    if D[i]<D[i-1] and F-D[i]<D[i-1]:
        T = -1
        break
    #Uma das medidas pelo menos é maior que a anterior
    #Seleciona o menor valor maior que a medida anterior
    if D[i] >= D[i-1] and F-D[i]>=D[i-1]:
        D[i] = D[i] if D[i]<=F-D[i] else F-D[i]
    elif F-D[i] >= D[i-1]:
        D[i] = F-D[i]
    #Senão D[i] = D[i] ou seja não faz nada
    T+=D[i]
    i+=1

print(T)