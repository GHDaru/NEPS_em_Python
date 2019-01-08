#https://olimpiada.ic.unicamp.br/pratique/pj/2016/f2/gincana/
def mdc(A,B):
    while B > 0:
        Resto = A % B
        A,B = B, Resto
    return A

V = input().split()
A = int(V[0])
B = int(V[1])

while mdc(A,B) > 1:
    B -=1

print(B)