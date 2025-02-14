#Para alterar a lista original, uso o .sort()
#Para não alterar, uso o sorted()

numeros = [1, 22, 34, 6, 81, 3, 23, 543, 5345, 12]
#nomes.sort(reverse=True)
# .sort() ordena e .sort(reverse=True) para ordem reversa. mas muda a lista original

numeros_ordenado = sorted(numeros, reverse=False) #Só por true que faz a ordem reversa.
print(numeros_ordenado)
# sorted() ele retorna uma lista nova em ordem, não afeta a original

print(numeros)