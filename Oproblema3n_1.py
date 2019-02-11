def collatz(i,q):
    if i == 1:
        return q
    if i % 2 == 0:
        return collatz(i//2,q+1)
    else:
        return collatz(3*i+1,q+1)

N = int(input())
print(collatz(N,0))
