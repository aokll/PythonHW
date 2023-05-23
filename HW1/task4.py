# Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой между
# дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input())
m = int(input())

k = int(input())

import sys

for el in range(0,n):
    if k == m*el:
         print(f"{n} {m} {k} -> yes")
         sys.exit() 

for el in range(0,m):
    if k == n*el:
         print(f"{n} {m} {k} -> yes")
         sys.exit() 

print(f"{n} {m} {k} -> no")