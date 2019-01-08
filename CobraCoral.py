v = input().split()
for i in range(4):
    v[i] = int(v[i])
#Verdadeira - distância de 2
if v[0]==v[2] or v[1]==v[3]:
    print("V")
else:
    print("F")