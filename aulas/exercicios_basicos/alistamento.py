from  datetime import date
atual = date.today().year

ano_nasc = int(input('Ano de nascimento: '))
idade = atual - ano_nasc

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE.')

elif idade > 18:
    saldo = 18 + ano_nasc
    print(f'Você já tem {idade} e deveria ter se alistado em {saldo}, ou sejá, há {idade - 18} anos.')

elif idade < 18:
    saldo = ano_nasc + 18
    print(f'Você tem {idade} e deverá se alistar em {saldo}.')