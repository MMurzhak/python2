'''Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
'''

slovar = {1: 3, 2: 5}
print(list(slovar.values()))

list_of_dicts = [{"V": "S001"},
                 {"V": "S002"},
                 {"VI": "S001"},
                 {"VI": "S005"},
                 {"VII": "S005"},
                 {"V": "S009"},
                 {"VIII": "S007"}]
#uniq_el = set()
#for i in list_of_dicts:
#    element = list(i.values())[0]
#    print(element)
#    uniq_el.add(element)
#print(uniq_el)

uniq_el = set()
for i in list_of_dicts:
    for key in i:
        element = i[key]
        uniq_el.add(element)
    print(uniq_el)
    
uniq_el1 = set(list(i.values())[0] for i in list_of_dicts)
print(uniq_el1)