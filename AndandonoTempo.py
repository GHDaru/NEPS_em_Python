N = list(map(int,input().split()))
N.sort()
#Condições
#1) primeiro crédito igual ao segundo
#2) segundo crédito igual ao  terceiro
#3) primeiro + segundo igual ao terceiro
print( "S" if N[0] == N[1] or N[1] == N[2] or (N[0]+N[1]==N[2]) else "N")