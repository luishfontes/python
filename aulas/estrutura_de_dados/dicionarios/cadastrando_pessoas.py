
pessoas = []

while True:
    try:
        escolha = int(input(f'''
{'-' * 35}
    [1] Cadastrar nova pessoa.
    [2] Ver pessoas cadastradas
    [3] Sair
{'-' * 35}
Opção: '''))
    
        if escolha == 3:
            print('Obrigado por testar!\nEncerrando programa...')
            break
    
        if escolha == 1:
            ''' # Da pra fazer dessa forma
            nome = input('Insira o nome: ')
            idade = int(input('Insira a idade: '))
            altura = float(input('Inira a altura em metros: '))
            pessoa = {'nome': nome, 'idade': idade, 'altura': altura}
            pessoas.append(pessoa)''' 
            pessoa = {'nome': input('Insira um nome: '), 
                      'idade': int(input('Insira a idade: ')), 
                      'altura': float(input('Insira a altura em metros: '))}
            
            if 0 <= pessoa['idade'] <= 100 and 0.30 <= pessoa['altura'] <= 2.51:
                pessoas.append(pessoa)

            elif (pessoa['idade'] > 100 or pessoa['idade'] < 0) and (pessoa['altura'] >= 2.51 or pessoa['altura'] < 0.30):
                print('Altura e idade inválidas.')

            elif pessoa['idade'] > 100 or pessoa['idade'] < 0:
                print('Apenas idades entre 0 e 100 são permitidas neste programa.')

            elif pessoa['altura'] >= 2.51 or pessoa['altura'] < 0.30: 
                print('Apenas alturas entre 0.30 metros e 2.51 metros são permitidas.')


        if escolha == 2:
            usuarios = '; '.join(f"{pessoa['nome'].title()}, {pessoa['idade']} anos e {pessoa['altura']} metros" for pessoa in pessoas)
            print(usuarios)
    
    except ValueError:
        print('Valor inserido não é válido')