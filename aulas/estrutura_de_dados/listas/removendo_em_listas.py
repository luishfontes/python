'''nomes = ['Caio', 'Marcos', 'João', 'Pedro']

nomes.append('Maria') #Adiciona um nome sempre no final da lista!!

#nomes[0] = 'Caio Sampaio' pra mudar

print(nomes)

##########################################################################################
# Comando .append()
nomes = []
while True:
    nome = input('Digite -1 para sair ou cadastre um nome: ')
    if nome == '-1':
        break

    nomes.append(nome)

print(nomes)

##########################################################################################
# Comando .insert()
nomes = ['Caio', 'Marcos', 'Carlos', 'Pedro']
nomes.insert(0, 'João') #Diferente do append, com .inset posso adicionar em outras posições

print(nomes)

##########################################################################################
# Comando para remover elementos da lista
# .pop() se n informar a posição, ele elimina o último da lista.
# .remove() elimina o que eu digitar lá dentro da lista.

nomes = ['Caio', 'Marcos', 'Carlos', 'Pedro']
nomes.pop(1)

print(nomes)'''

##########################################################################################
# Como descobrir/encontrar o indice de um determinado elemento
# .index()

nomes = ['Caio', 'Marcos', 'Carlos', 'Pedro', 'Carlos']
print(nomes.index('Carlos'))

#print(nomes)