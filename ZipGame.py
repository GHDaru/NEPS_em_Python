V = []
for i in range(0,4):
    V.append(int(input()))
Lia = (V[0] + V[1])* (3 if V[0]-V[1] in [-1,1] else (2 if V[0]==V[1] else 1))
Carolina = (V[2] + V[3]) * (3 if V[2]-V[3] in [-1,1] else (2 if V[2]==V[3] else 1))
#print(Lia, Carolina)
if Lia > Carolina:
    print("Lia")
elif Lia == Carolina:
    print("empate")
else:
    print("Carolina")
