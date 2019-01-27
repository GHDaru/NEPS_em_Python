N = int(input())
C = [int(input()) for i in range(N)]
Q =  int(input())
T = [int(input()) for i in range(Q)]
R = [ ("Sim" if T[i] in C else "Nao") for i in range(Q)]
print(*R, sep = '\n')