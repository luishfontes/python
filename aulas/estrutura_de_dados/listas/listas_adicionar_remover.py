produtos = ['Iphone 8', 'Iphone x', 'Iphone 11', 'Iphone 13', 'Iphone 15']

print(f'Lista atual {produtos}.')

rmv_produto = input('Insira o nome do produto que deseja remover: ')
produto = input('Insira o nome de um novo produto para substituir um existente: ')

if rmv_produto in produtos: #Aqui eu fiz por if e else
    i = produtos.index(rmv_produto)
    produtos[i] = produto
    print(f'Nova lista:\n{produtos}')
else:
    print('Produto não encontrado.')

#Agora por try e exception.

'''try:
    i = produtos.index(rmv_produto)
    produtos[i] = produto
    print(f'Nova lista:\n{produtos}')
except KeyboardInterrupt:
    print('O usuário decidiu interromper o programa.')
except (ValueError, TypeError):
    print('Erro na hora de inserir o valor ou tipo de dado.')
except:
    print('Produto não encontrado.')
    pass
finally:
    print('Fim do programa, obrigado por testar :).')'''