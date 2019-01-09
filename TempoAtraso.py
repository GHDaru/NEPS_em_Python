#https://neps.academy/problem/149
Ha = int(input())
Ma = int(input())
Hr = int(input())
Mr = int(input())
Atual = Ha*60 + Ma  +  45
Reuniao = Hr*60 + Mr

if Atual <= Reuniao:
    print("Sucesso")
else:
    print("Atrasado", Atual - Reuniao)