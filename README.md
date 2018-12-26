# Инвариантная СР
4.1. Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.

```python
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
```
![результат](https://github.com/python-advance/sem5-collections-arinasaf11/blob/master/ISR/1.1/Screenshot_1.jpg?raw=true)

4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).

```python
import random
a = [random.randint(-50, 50) for i in range(10)]
#randint - возвращает случ. целое число в указанном диапазоне
#создается массив из 10 символов, каждый из которых нах-ся в диапазоне от -50 до 50
lst1, lst2 = [], []
for i in a:
    if i < 0:
        lst1.append(i)
    else:
        lst2.append(i)
        
print('Исходный список:',a)
print('Два списка из отрицательных и положительных чисел:')
print(lst1)
print(lst2)
```

![результат](https://github.com/python-advance/sem5-collections-arinasaf11/blob/master/ISR/1.2/sort_func.jpg?raw=true)
