V = [ int(input()) for i in range(10)]
Menor = min(V)
O = []
for i in range(10):
    if V[i] == Menor:
        O = O + [i]
        V[i] = -1
print('Menor:',Menor)
print('Ocorrencias:',*O)
print(*V)
