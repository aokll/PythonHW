# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list = []
s = {}

print("минимальное значение диапазона")
min = int(input())
print("максимальное значение диапазона")
max = int(input())
print("Введите размер массива")
l = int(input())


import random

for i in range(l):
    list.append(random.randint(-1000,1000))

for i in range(len(list)):
    if list[i]>min and list[i]<max:
        s[i] = list[i]

print("Вывод всех значений", end=' ')
print(list)
print("Вывод индексов и значений попавших в диапазон", end=' ')
print(s)
   



