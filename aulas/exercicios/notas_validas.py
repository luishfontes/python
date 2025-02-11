#Escreva um programa que recebe notas de um aluno (0-10).
#Caso a nota digitada esteja fora deste intervalo, peça para o prof digitar novamente.

while True:
    nota = float(input('Insira uma nota: '))
    if nota >= 0 and nota <= 10:
        print(f'Nota armazenada com sucesso {nota}')
        break

    print('Nota inválida, digite novamente.') 