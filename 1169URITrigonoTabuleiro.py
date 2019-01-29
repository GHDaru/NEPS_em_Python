def qtde(Casas):
    return (2**Casas - 1 ) // 12000

N = int(input())
R = [ '{:d} kg'.format(qtde(int(input()))) for i in range(N) ]
print(*R, sep = '\n')