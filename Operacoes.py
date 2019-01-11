OP = input()
V = list(map(float,input().split()))
Resp = V[0]*V[1] if OP == 'M' else V[0]/V[1]
print('{:.2f}'.format(Resp))