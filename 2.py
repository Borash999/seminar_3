# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите количество элементов массива: '))
array = []
i = 0
while n>i:
    array.append(int(input('Введите элемент массива: ')))
    i += 1
x = int(input('Введите некоторое число: '))  
m = array[0]
for el in array:
    if abs(x-m)>abs(x-el):
        m=el

print(m)

# import random  
# N = int(input("Введите количество элементов в массиве "))
# list = [random.randint(1, 20) for i in range(N)]
# print(list)
# x = int(input("Введите искомое число "))
# index_element = 0
# min_element = abs(x - list[0])
# for i in range(1, N):
#     buffer_element = abs(x -list[i])
#     if buffer_element < min_element:
#         min_element = buffer_element
#         index_element = i

# print("Самый близкий по величине элемент к заданному числу " , list[index_element])      