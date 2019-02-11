N = int(input())
Ti = [int(input()) for i in range(N)]
F = 0
Tf = 0
for i in range(N):
    Tfa = Tf if Tf > Ti[i] else Ti[i]
    Tf = Ti[i] +  10
    F += Tf - Tfa
print(F)