def cadastro_carro(quantidade):
    carros = []

    for i in range(quantidade):
        carro = {
                'marca' : input('Marca do carro: '),
                'modelo' : input('Modelo do carro: '),
                'ano' : int(input('Ano do carro: ')),
                'placa' : input('Placa do carro: ')
}
        carros.append(carro)
        print(f'Carro inserido com sucesso: {carro}.')

    carros_cadastrados = '\n'.join(
        f"Marca: {carro['marca'].title()}, Modelo: {carro['modelo'].title()}, Ano: {carro['ano']}, Placa: {carro['placa']}"
        for carro in carros
        )
    return carros_cadastrados


try:
    quantidade_repeticoes = int(input('Insira a quantidade de cadastros: '))
    print(cadastro_carro(quantidade_repeticoes))
except ValueError:
    print('Valir inválido.')