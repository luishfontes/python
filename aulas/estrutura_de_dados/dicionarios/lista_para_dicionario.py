def pessoas(nome, idade):
    print(f'nome: {nome} e idade: {idade}')

lista_pessoas = [
    "Ana", 25,
    "Carlos", 30,
    "Maria", 22,
    "João", 28,
    "Luana", 35
]

dict_pessoas = {}

for i in range(0, len(lista_pessoas), 2):
    dict_pessoas[lista_pessoas[i]] = lista_pessoas[i+1]

print(dict_pessoas)

for nome, idade in dict_pessoas.items():
    pessoas(nome, idade)