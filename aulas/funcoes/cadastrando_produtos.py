def cadastro_produtos():
    produto = input('Digite o nome de um produto: ')
    produto = produto.lower()
    produto = produto.strip()
    return produto


produto = cadastro_produtos()
print(produto)