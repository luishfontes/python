#Defina um usuário e senha e depoisi verifique se o login é valido.

#Essa primeira parte é o cadastro, mas não vejo necessidade de por no código só por questão "visual"

usuario = input('Digite o nome de usuário: ')
senha = input('Digite a sua senha: ')

print('--------------------\nlogin\n--------------------')

while True:

    usuario_login = input('Digite o nome de usuário: ')
    senha_login = input('Digite sua senha: ')

    if usuario_login == usuario and senha_login == senha:
        print('Usuário logado com sucesso.')
        break

    print('Dados incorretos, tente novamente.')