Matriz = [ [int(input()) for i in range(3)] for j in range(3) ]
SC = [0 for i in range(3)]
#Calcula soma das colunas
for j in range(3):
    SC[j] = sum([Matriz[k][j] for k in range(3)])

for i in range(3):
    print('Coluna {}: {}'.format(i,SC[i]))