try:
    print('Adicionador de números para sua lista.\nCaso deseje encerrar o programa, digite "fim".')
    numeros = []

    while True:
        try:
            numero = input('Insira um número: ')
            if numero.lower() != "fim":
                numeros.append(int(numero))
            else:
                print('Sua lista está feita!')
                break
        except ValueError:
            print(f'O valor {numero} não é um numero, por favor, tente novamente.')

    print(numeros)

    pergunta = input('Deseja remover ou alterar algum item da lista?\n')
    if pergunta.lower() == "sim":
        while True:
            opcao = input('Certo, selecione uma opção: \n1 - remover\n2 - alterar\n3 - sair\n')
            
            if opcao == "1":
                print(f'Lista atual de {numeros}.')
                try:
                    num_remover = int(input('Qual número você deseja remover?\n'))
                    if num_remover in numeros:
                            numeros.remove(num_remover)
                            print(f'O {num_remover} foi retirado da lista.')
                    else:
                            print('Este número não está na lista, tente outro número.')
                except ValueError:
                    print('Por favor, insira um valor válido.')

            elif opcao == "2":
                print(numeros)
                try:
                    num_alterar = int(input('Qual número você deseja alterar?\n'))
                    if num_alterar in numeros:
                        i = numeros.index(num_alterar)
                        num_novo = int(input(f'Qual número você deseja adicionar no lugar de {num_alterar}?\n'))
                        numeros[i] = num_novo
                        print(f'{num_alterar} foi alterado para {num_novo}.')
                        print(f'Nova lista {numeros}.')
                    else:
                        print('Este número não está na lista, tente um outro número.')
                except ValueError:
                    print('Este número não está na lista, tente outro número.')

            elif opcao == "3":
                print('O programa será encerrado, obrigado por testar!')
                break
            else:
                print('Opção inválida, tente novamente.')

    numeros.sort()
    print(f'Sua lista final (ordenada): {numeros}')

except KeyboardInterrupt:
    print('\nO usuário decidiu interromper o programa.')