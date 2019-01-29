P, F = list(map(int,input().split()))
R = list(map(int,input().split()))
NP = P
for i in R:
    NP += i
    NP = 0 if NP < 0 else (100 if NP > 100 else NP)
print(NP)
