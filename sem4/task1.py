'''25'. Напишите программу, которая принимает на вход строку, и отслеживает,
сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
Порядок символов исходной строки не меняется.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2'''

list = (input('Введите строку: ')).split()
print(list)
dict = {}
for i in list:
    if i in dict:
        print(f'{i}_{dict[i]}', end=' ')
        dict[i] = dict[i] + 1
    else:
        print(i, end=' ')
        dict[i] = 1
#dict[i] = dict.get(i, 0) + 1