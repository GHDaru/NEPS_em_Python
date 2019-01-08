Total = int(input())
V = []
for i in range(3):
    V.append(int(input()))
    #print(V)
V.sort()
qtde = 0
acum = 0
for i in V:
    acum += i
    if acum <= Total:
        qtde += 1
    else:
        break
print(qtde)
