N = int(input())

V = int(input())

Maior = V
Menor = V
for i in range(1,N):
    V = int(input())
    Maior = V if V > Maior else Maior
    Menor = V if V < Menor else Menor

print(Maior)
print(Menor)
