C = int(input())
A = int(input())
print( (A // (C-1)) + (1 if A % (C-1) > 0 else 0) )