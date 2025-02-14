# c = 5 * f - 32/9 de farenheit para celsius

farenheit = float(input('Digite o valor em farenheit: '))

#celsius = float(input('Digite o valor em celsius'))

celsius = 5 * ((farenheit - 32)/9)

print(f'A conversão de {farenheit}°F, é {celsius}°C')