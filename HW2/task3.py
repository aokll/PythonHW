# ; Задача 14: Требуется вывести все целые степени двойки 
# ; (т.е. числа вида 2k), не превосходящие числа N.
# # 10 -> 1 2 4 8
import sys
n = int(input())
x = 0
r = range(0,n)

for i in r:
    x = 2**i
    if x > n:
        sys.exit()
    print(x,end=' ')
    





