'''i = 0

while i < 10:
    print(i)
    if i >= 5:
        break
    i += 1'''

i = 0

while i < 10:
    print(i)
    if i % 2 == 1:
        i += 2
        continue
    i += 1