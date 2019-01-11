def fibo(N):
    if N == 0 or N == 1:
        Result = 1
    else:
        Result = fibo(N-1) + fibo(N-2)
    return Result

N = int(input())
print(fibo(N))