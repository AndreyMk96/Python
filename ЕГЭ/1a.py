"""Задание №1А"""
N = 1000
a = [] #список элементов
max_mult = 0 #максимальное произведение
for i in range(N):
    a.append(int(input()))
for i in range(0, N-8):
    for j in range(i+8, N):
        if(a[i]*a[j]) > max_mult:
            max_mult = a[i] * a[j]
print(max_mult)

"""Тесты"""
""" 1) N = 10, a = [100,45,55,245,35,25,10,10,10,26] Ответ: 2600"""
""" 2) N = 15, a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] Ответ: 105"""
""" 3) N = 20, a = [1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1] Ответ: 42"""


