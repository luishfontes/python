casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = float(input('Digite em quantos anos deseja pagar: '))

prestacao = casa/(anos * 12)
minimo = salario * 30/100

print(f'Para pagar uma casa de R${casa} em {anos} anos, a prestação será de {prestacao}')

if prestacao <= minimo:
    print(f'O valor da prestação é: {prestacao}, o emprestimo pode ser concedido')
else:
    print('Sinto muito, mas você não tem direito ao emprestimo.')
