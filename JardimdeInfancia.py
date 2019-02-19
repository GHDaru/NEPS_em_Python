import math

def escalar(V1, V2):
    return V1[0]*V2[0] + V1[1]*V2[1]
def norma(V):
    return (V[0]*V[0] + V[1]*V[1])**(1/2)
def vetor(P1,P2):
     return [P2[0] - P1[0], P2[1] - P1[1]]
def avet(V1,V2):
    return math.acos(escalar(V1, V2) / (norma(V1) * norma(V2)) )
def cosvet(V1,V2):
    return escalar(V1, V2) / (norma(V1) * norma(V2))
def pontomedio(P1,P2):
    return [[P1[0] + (P2[0] - P1[0])/2, P1[1] + (P2[1] - P1[1])/2]]


#Entrada dos pontos
Ponto = [list(map(int,input().split())) for i in range(7)]
#Gerar Vetores
V = dict()
#Norma = dict()
for i in range(1,7):
    for j in range(i+1,8):
        V[ i*10+j] = vetor(Ponto[i-1],Ponto[j-1])

#Testes
Teste = [0, 0, 0, 0, 0, 0, 0, 0]
#Se ocorrer um teste de reprovação não é pinheiro
#teste 01: O ângulo P2P1P3 deve ser agudo
#Para isto deve-se verificar o ângulo entre os vetor P1P2 e P1P3
#A partir da Geometria Analítica tem-se que cos alfa = produto escalar / (norma de u * norma de v)
#como se deseja que cos alfa seja positivo, então basta fazer o teste de cos alfa > 0
#Vetor 01 = P1P2 ou P2 - P1
#Vetor 02 = P1P3 ou P3 - P1
Teste[0] = cosvet( V[12], V[13]) > 0
#teste 02 os segmentos P1P2 e P1P3 tem o mesmo comprimento
Teste[1] = norma( V[12] ) == norma( V[13] )
#teste 03 os pontos P2, P3, P4 e P5 são colineares
#angulo entre V[23] e V[24] = 0 e V[23] e V[25] = 0
Teste[2] = cosvet( V[23], V[24] ) == 1 and cosvet( V[23], V[25] ) == 1
#teste 04: O ponto médio entre P2P3 e P4P5 são iguais
Teste[3] = pontomedio( Ponto[1], Ponto[2]) == pontomedio( Ponto[3], Ponto[4] )
#teste 05: O comprimento de P2P3 é maior que o comprimento de P4P5
Teste[4] = norma(V[23]) > norma(V[45])
#teste 06: Os segmentos P4P6 e P5P7 são perpendiculares ao segmento P2P3
Teste[5] = escalar(V[46], V[23]) == 0 and escalar(V[57], V[23]) == 0
#teste 07: P4P6 e P5P7 tem o mesmo comprimento
Teste[6] = norma(V[46]) == norma(V[57])
Teste[7] = norma( V[14]) < norma( V[16])
Passou = 1
for i in Teste:
    Passou = Passou * i
print("S" if Passou else "N")


