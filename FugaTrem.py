V = input().split()
#print(V)
H,P,F,D = list(map(int, V))
#print(H,P,F,D)

pos = F
policeFlag = False
HeliFlag = False
for i in range(0,16):
    if (F + i*D) % 16 == H and not policeFlag:
        HeliFlag = True
    if (F + i * D) % 16 == P and not HeliFlag:
        policeFlag = True
print( "S" if HeliFlag else "N")
