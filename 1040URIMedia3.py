Pesos = [2,3,4,1]
N = list(map(float,input().split()))
Media =  sum([ Pesos[i]*N[i] for i in range(4) ])/10
Saida = ['Media: {:.1f}'.format(Media)]
if Media >=7:
    Saida += ['Aluno aprovado.']
elif Media<7 and Media >= 5:
    Saida += ['Aluno em exame.']
    Exame = float(input())
    Saida += ['Nota do exame: {:.1f}'.format(Exame)]
    MediaFinal = (Media + Exame)/2
    if MediaFinal >= 5:
        Saida += ['Aluno aprovado.']
    else:
        Saida += ['Aluno reprovado.']
    Saida += ['Media final: {:.1f}'.format(MediaFinal)]
else:
    Saida+= ['Aluno reprovado.']
print(*Saida, sep = '\n')

