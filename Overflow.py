N = int(input())
P, C, Q = input().split()
P,Q = int(P), int(Q)
print( "OK" if (C == '+' and P+Q<=N) or (C=='*' and P*Q<=N) else "OVERFLOW")