# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый 
# ребенок, если известно, что Петя и Сережа сделали одинаковое количество
# журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

s = int(input())

k = ((2/3)*s)

p = c = (s - k)/2

print(f"k = {round((2/3)*s,2)}, p = {round((s - (2/3)*s)/2,2)}, c = {round((s - (2/3)*s)/2,2)}")