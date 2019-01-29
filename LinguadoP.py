Texto = input().split()
NovoTexto = []
for palavra in Texto:
    nova_palavra = ''.join([palavra[i] for i in range(1,len(palavra),2)])
    NovoTexto.append(nova_palavra)

print(' '.join(NovoTexto))
