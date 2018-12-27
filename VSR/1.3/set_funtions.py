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
