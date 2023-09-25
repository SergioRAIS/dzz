import random
zelen = int(input("Введите количество кустов: "))
ber = list(random.randint(0, 10) for i in range(zelen))
result = []
i = 0
sum = 0

print(ber)

while (i < zelen):
    if (i == zelen - 1):
        sum = ber[i] + ber[i - 1] + ber[0]
    else:
        sum = ber[i] + ber[i - 1] + ber[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f"Макс число ягод : {result[-1]}")