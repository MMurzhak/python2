'''Задача №17. Общее обсуждение
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 2, 3, 4, 1, 2, 3]
Output: 6
Примечание: Пользователь может вводить значения
списка или список задан изначально. '''

nums = [1, 2, 3, 4, 5, 1, 2, 3]
print(len(set(nums)))
# подсчитать кол-во чисел которые встречаються 1 раз
result = []

for i in set(nums):
    if nums.count(i) == 1:
        result.append(i)
print(result)

result1 = [i for i in set(nums) if nums.count(i) == 1]
print(result1)