'''33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
[1, 2, 3, 1, 2, 1, 5, 4, 5] -> [1, 2, 3, 1, 2, 1, 1, 4, 1]'''

list = [1, 2, 3, 1, 2, 1, 5, 4, 5]
print(list)

min = int(min(list))
max = int(max(list))
for i in range (len(list)): 
    if list[i] == max:
        list[i] = min
print(list)