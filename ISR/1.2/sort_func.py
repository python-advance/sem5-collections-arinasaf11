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
