N = int(input())
Resp = "S"
if N==1:
    Resp = "N"
else:
    i = 2
    while i*i<=N:
        if N % i == 0:
            Resp = "N"
        i += 1
print(Resp)