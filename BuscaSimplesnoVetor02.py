V = list(map(int,input().split()))
X = int(input())
if X not in V:
    print('Mia x')
else:
    T = [X == i for i in V]
    S = [ i for i in range(len(T)) if T[i]]
    print(sum(T))
    #print(S)
    print(*S)