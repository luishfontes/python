'''dados = {"nome": "Luís", "idade": 22, "telefone": "3333-2222"}

dados["nome"]
dados["idade"]
dados["telefone"]

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1213"

dados '''

contatos = {
    "luis@gmail.com": {"nome": "Luís", "idade": 22},
    "giovana@gmail.com": {"nome": "giovanna", "idade": 19},
    "aninha@gmail.com": {"nome": "aninha", "idade": 20},
    "torugo@gmail.com": {"nome": "torugo", "idade": 20, "extra": {"a": 1}}
}

telefone = contatos["luis@gmail.com"]["nome"]
print(telefone)

extra = contatos["torugo@gmail.com"]["extra"]["a"]
print(extra)

# Iterando o dicionario

for chave, valor in contatos.items():
    print(chave, valor)