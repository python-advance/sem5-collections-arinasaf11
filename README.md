# Инвариантная самостоятельная работа
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

# Вариативная самостоятельная работа

4.3. Создание программы, позволяющей выполнять основные операции (объединение, пересечение, вычитание) над множествами (количество элементов в множестве и их элементы вводятся вручную).

```python
"""Функция создает заданное количество множеств, элементы которого вводятся с клавиатуры"""
def create_sets():
  n = int(input('Введите количество множеств: '))
  lst = []
  for i in range(n):
      el = input('Введите множество через запятую и нажмите enter: ')
      el = el.split(",")
      #split - разбивает строку на части, используя разделитель, и возвращает эти части списками
      lst.append(set(el))
  return lst #получился список из множеств

"""Функция возвращает множество, являющееся результатом одной из операций, выбранной пользователем"""
def set_functions(n, lst):
      main_set = set()
      if n == 1:
        for i in lst:
              main_set.update(i) #Метод update() принимает один аргумент — множество, и добавляет все его элементы к исходному множеству. 
      elif n == 2:
        x=0
        for i in lst:
          if x == 0: #один раз в main_set добавляется первое множество из lst, а потом оно будет изменятся
            main_set.update(i)
            x += 1
          else:
            main_set.intersection_update(i) #intersection_update - оставляет во множестве main_set пересечение множеств main_set и i-м
      elif choice == 3:
        x = 0
        for i in lst:
          if x == 0: 
            main_set.update(i)
            x += 1
          else:
            main_set.difference_update(i)#difference_update - удаляет из множества main_set все элементы, присутствующие в i-м
      return main_set
          
        
print("Что вы хотите сделать со множествами?\n1-объединение множеств\n2-пересечение множеств\n3-вычитание множеств")
choice = int(input('Введите номер нужной операции\n'))
print(set_functions(choice, create_sets()))
```

Результат:
![объединение](https://github.com/python-advance/sem5-collections-arinasaf11/blob/master/VSR/1.3/union.jpg?raw=true)

![пересечение](https://github.com/python-advance/sem5-collections-arinasaf11/blob/master/VSR/1.3/intersection.jpg?raw=true)

![вычитание](https://github.com/python-advance/sem5-collections-arinasaf11/blob/master/VSR/1.3/difference.jpg?raw=true)
