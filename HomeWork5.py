# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число
# А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def main():
    a = int(input('a: '))
    b = int(input('b: '))
    print(f'{a}^{b} = {recursion(a, b)}')
def recursion(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * recursion(a, b - 1)


if __name__ == '__main__':
    main()


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4
# A = 2; B = 3 -> 8

def main():
    a = int(input('a: '))
    b = int(input('b: '))
    print(f'{a} + {b} = {recursion(a, b)}')


def recursion(a, b):
    if b !=0:
        return recursion(a,b-1)+1
    if b == 0:
        return a               \
            # + recursion(a, b - 1)


if __name__ == '__main__':
    main()