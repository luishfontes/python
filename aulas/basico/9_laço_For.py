#for i in range(0, 102, 2):
#    print(i)

#Dessa forma eu posso fazer a mesma coisa de exibir tudo par, só que mais simples!!

# print(list(range(0, 100, 3)))

k = 0

for i in range(0, 100):
    for j in range(0, 100):
        print(f'i = {i} j = {j}')
        k += 1

print(k)