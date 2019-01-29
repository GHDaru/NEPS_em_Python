P = str(input())
Vogais = ['a','e','i','o','u']
V = ''.join([i for i in P if i in Vogais])
C = ''.join([i for i in P if i not in Vogais])
print('Vogais:', V)
print('Consoantes:', C)