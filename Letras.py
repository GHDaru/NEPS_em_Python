L = input()
W = input().split()
cont = 0
for i in W:
    cont += 1 if L in  i else 0
print('{:.1f}'.format(cont/len(W)*100))
