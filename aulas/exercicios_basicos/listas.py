convidados = ['pedro', 'felipe', 'miguel']

for i in convidados:
    print(f'Te convido para um jantar em minha casa, caro(a), {i}')

#convite feito, porém um não veio e eu chamarei outro.
print('Infelizmente Miguel não poderá vir e terei que chamar outra pessoa no lugar dele.')
popped_convidado = convidados.pop()

convidados_novo = input('Digite o nome do novo convidado: ')
convidados.append(convidados_novo)

#novos convidados

convidado_novo1 = input('Nome do novo convidado: ')
convidados.insert(0, convidado_novo1)

convidado_novo2 = input('Nome do novo convidado: ')
convidados.insert(2, convidado_novo2)

convidado_novo3 = input('Digite o nome do novo convidado: ')
convidados.append(convidado_novo3)

print(convidados)

for i in convidados:
    print(f'Te convido para um jantar em minha casa, caro(a), {i}.')

excluidos = convidados.pop()
print(f'Sinto muito por revogar os convites {excluidos}')

print(convidados)