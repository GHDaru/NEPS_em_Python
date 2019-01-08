C = []
J = []
for i in range(0,3):
    C.append(int(input()))
for i in range(0,2):
    J.append(int(input()))
M = [0,0]
for j in range(0,len(J)):
    for c in C:
        M[j] += 1 if J[j]<c else 0
print("S" if sum(M) <= 3 and 3 not in M else "N")



