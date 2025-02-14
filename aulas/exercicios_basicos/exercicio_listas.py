import emoji

# Criando uma lista vazia para os convidados
convidados = []

# Perguntar o número de convidados
num_conv = int(input('Digite o número de convidados: '))  # Converte para inteiro

# Adicionar os convidados à lista
for i in range(num_conv):
    nome = input(f'Digite o nome do {i+1}° convidado: ')  # Adiciona o nome do convidado
    convidados.append(nome)

# Exibir a lista de convidados
print("\nLista de convidados:", convidados)

# Perguntar o nome do convidado que faltou
convidado_faltou = input('\nDigite o nome do convidado que faltou: ')

# Perguntar o nome do novo convidado para substituir
convidado_subst = input('Digite o nome do novo convidado: ')

# Laço para encontrar e substituir o convidado faltoso
for i in range(len(convidados)):
    if convidados[i] == convidado_faltou:
        convidados[i] = convidado_subst  # Substitui o nome na posição 'i'
        break  # Interrompe o laço após a substituição

# Adicionando novos convidados em posições determinadas
convidados.insert(0, input('Digite o nome do novo convidado para a posição 0: '))
convidados.insert(2, input('Digite o nome do novo convidado para a posição 2: '))
convidados.append(input('Digite o nome do convidado para a última posição: '))

print('-' * 94)
print('Infelizmente não será possivel a presença de todos e alguns convidados ficaram de fora.')
print('-' * 94)

# Laço para remover convidados até o usuário digitar "parar"
while True:
    # Pedir o nome do convidado a ser removido a cada iteração
    convidados_remover = input('Digite o nome do convidado que vai ser removido (caso deseje parar, digite "parar"): ')

    # Verificar se o usuário deseja parar
    if convidados_remover.lower() == 'parar':
        break
    
    # Verificar se o convidado está na lista e removê-lo
    if convidados_remover in convidados:
        indice_remover = convidados.index(convidados_remover)
        convidados.pop(indice_remover)  # Remove o convidado
        print(f'O convidado {convidados_remover} foi removido com sucesso.')
        print(f'Sinto muito {convidados_remover}, mas você foi excluído da lista de convidados.')
    else:
        print(f'O convidado {convidados_remover}, não está na lista, tente novamente.')

# Enviar convites para os convidados restantes
for i in convidados:
    print(f'Olá, {i}! Você está convidado para o jantar, te esperamos por lá!', emoji.emojize(':orange_heart:', language='alias'))

# Exibir a lista final de convidados
print(f'O numero total de convidados é: {len(convidados)}')
print(f'\nLista final de convidados: ', convidados)
