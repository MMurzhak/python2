'''Задача №19. Общее обсуждение
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.'''

nums = [1, 2, 3, 4, 5]

# Решение 1
#sdvig = int(input())
#for i in range(sdvig + 1):
#    nums.append(nums.pop(0))
#print(nums)

# Решение 2
#sdvig = int(input())
#for _ in range(sdvig):
#    nums.insert(0, nums.pop(len(nums) - 1))
#print(nums)

sdvig = int(input()) % len(nums)
#for _ in range(sdvig):
#    nums.insert(0, nums.pop(len(nums) - 1))
#print(nums)

nums1 = nums[-sdvig::] + nums[:-sdvig:]
print(nums1)