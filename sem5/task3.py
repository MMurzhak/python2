'''35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)'''


def prost(k: int) -> str:    

    if k > 1:
        for i in range(2, int((k/2) + 1)):
            if (k % i) == 0:
                return ('ne prostoe')
    return ('prostoe')
k = int(input('Vvedite 4islo: '))
print(prost(k))