#faça um código para ler a senha de um usuário e apos 3 tentativas erradas, sair do programa, informando que a senha está bloqueada
tentativa = 1
senha_correta = 123456
mensagem = "acesso bloqueado"
while tentativa <=3:
    senha = int(input("digite a senha: "))
    if senha == senha_correta:
        mensagem = "acesso permitido"
        break
    tentativa += 1
print(mensagem)








