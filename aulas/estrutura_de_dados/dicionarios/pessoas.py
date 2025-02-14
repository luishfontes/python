pessoas = [{"nome": "Luís", "idade": 22}, 
           {"nome": "Pedro", "idade": 25},
           {"nome": "João", "idade": 18},
           {"nome": "Caio", "idade": 19},
           {"nome": "Lucas", "idade": 24},
           {"nome": "Miguel", "idade": 31},
]

'''pessoa = [pessoa['nome'] for pessoa in pessoas]
print(pessoa)'''
'''
for pessoa in pessoas:
    print(pessoa['nome'], pessoa['idade'])'''

nomes = ', '.join(pessoa['nome'] for pessoa in pessoas)

print(nomes)