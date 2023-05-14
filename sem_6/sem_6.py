# Урок 6. Повторение списков
#
# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#

def form_progress(first, diff, n):
 n_item = first + n*diff
 return n_item
def input_data(text):
 num = int(input(text + ": "))
 return num

first_elem = input_data('first elem')
difference = input_data('diff')
n = input_data('n elem')
list_progress =[]
i = first_elem
for i in range (n):
 #elem = form_progress(first_elem, difference, n)
 list_progress.append(form_progress(first_elem, difference, i))

print(list_progress)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума)
#
# После загрузки задания, вы можете проверить себя самостоятельно с помощью эталонного решения
#  до 02 мая
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
 if min_number <= list_1[i] <= max_number:
  print(i)
