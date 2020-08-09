str = " *naber_Lan_benim*"
print(str)
a = str.strip("*")
print(a)

n = lambda a, b : a + b
print(n(4,5))

sırasız_liste = [('b', 3), ('a', 8), ('d', 12), ('c',1)]
print(sorted(sırasız_liste, key = lambda x : x[1]))

import numpy as np
a = np.array([1,2,3,40])
b = np.array([5,10,11,50])
print(a, b, a*b, sep='\n')

print("-"*50)
liste = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x : x*10, liste)))
print(list(filter(lambda x:x%2 ==0, liste)))
from functools import reduce
print(reduce(lambda a,b:a+b,liste))

print('-'*50)
x = 10
y = 0
w = 'a'
try:
    print(x/y)
except ZeroDivisionError:
    print('Sayı sıfıra bölünemez')
    print('0')

try:
    print(x+w)
except TypeError:
    print('{} + {} için : İnteger ile String toplamanaz'.format(x,w))

print(list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50]))))
from functools import reduce
A = ["Veri","Bilimi","Okulu"]
print(reduce(lambda a,b: a+b, list(map(lambda x: x[0], A))))