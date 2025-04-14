#faça um código que receba o número de alunos que uma sala de aula depois solicite as notas desses alunos, no final, mostre a média aritmética da turma.
soma = 0
X=1
qtd = int(input("digite o número de alunos: "))
while  X <= qtd:
    notas = int(input("digite a nota: "))
    X = X+1
    soma = soma + notas
    media = soma/qtd
print(media)
