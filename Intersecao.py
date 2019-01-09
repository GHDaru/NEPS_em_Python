P = list(map(int,input().split()))
Q = list(map(int,input().split()))
XEntre = True if (Q[0] >= P[0] and Q[0]<=P[2]) or ((Q[2] >= P[0] and Q[2]<=P[2])) else False
YEntre = True if (Q[1] >= P[1] and Q[1]<=P[3]) or ((Q[3] >= P[1] and Q[3]<=P[3])) else False
XEntre = XEntre or (True if (P[0] >= Q[0] and P[0]<=Q[2]) or ((P[2] >= Q[0] and P[2]<=Q[2])) else False)
YEntre = YEntre or (True if (P[1] >= Q[1] and P[1]<=Q[3]) or ((P[3] >= Q[1] and P[3]<=Q[3])) else False)


print("1" if XEntre and YEntre else "0")
