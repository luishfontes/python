'''produtos = ['motorola', 'Iphone', 'fone', 'LG', 'headset']
vendas = [1000, 1500, 200, 900, 700]

print(f'O número de {produtos[1]} vendidos, foram de {vendas[1]}.')'''

produtos = ['motorola', 'Iphone', 'fone', 'LG', 'headset']
vendas = [1000, 1500, 200, 900, 700]

produto = input('Insina o nome do produto que deseja procurar:\n')

if produto in produtos:
    i = produtos.index(produto)
    qtd_vendas = vendas[i]
    print(f'O produto {produto} possui {qtd_vendas} vendas realizadas.')
else:
    print(f'Não foi possivel encontrar "{produto}" em nosso sistema, tente novamente.')
    
#print(f'A quantidade de vendas de {produtos[i]} é de {vendas[i]}')