import random
a = [random.randint(1, 100) for i in range(10)]
#randint - возвращает случ. целое число в указанном диапазоне
#создается массив из 10 символов, каждый из которых нах-ся в диапазоне от 1 до 100

"""Функция, которая сортирует массив методом вставки"""
def Insertion_sort(mas):
    for i in range(len(mas)): #цикл по индексу
        v, j = mas[i], i
        while (mas[j-1] > v) and (j > 0):
            mas[j] = mas[j-1]
            j = j - 1
        mas[j] = v
    return mas

print('Исходный массив',a)
print('Метод вставки:',Insertion_sort(a))

#с помощью встроенных функций языка
print('Сортировка с помощью sorted',sorted(a))
a.sort()
print('Сортировка с помощью метода sort', a)
