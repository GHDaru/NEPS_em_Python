C = int(input())
P = str(input())
Q = { 'P': 2, 'C':2, 'A':1, 'D':0}
T = 0
for i in P:
    T += Q[i]
print(T)
