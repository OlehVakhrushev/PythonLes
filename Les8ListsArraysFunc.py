# lst = []
# print(lst)
# print(len(lst))

# lst = [6, -1, 9, 4, 3]
# print(lst)
# print(lst[0])
# print(len(lst))
# print(lst[len(lst) -1])
# print(lst[-1])


# print(lst[0:2])
# print(lst[:3])
# print(lst[2:])
# print(lst[1:-1])
# print(lst[::2]) # прошлись по четным индексам
# print(lst[1::2])
# print(lst[::-1])

# arr = [10, 20, 30, 40, 50]

# for i in range (len(arr)):  # 0, 1, 2, 3, 4, 5
#   print(i, arr[i])

# print('-------')

# for el in arr:
#   print(el)

# print('-------')

# for i, el in enumerate(arr):
#   print(i, el)

# print('-------')

# print(sum(arr))
# print(min(arr))
# print(max(arr))
# print(sum(arr)/len(arr))

# arr = [10, -20, 30, 40, -50]
# s = 0
# for el in arr:
#   if el > 0:
#     s += el
# print

# s = 0
# for i, el in enumerate(arr):
#   if i % 2 == 0:
#     s += el
# print(s)


# кол-во пар элем с разными знаками
# count = 0
# for i in range(len(arr) - 1):
#   if arr[i] * arr[i+1] < 0:
#     count += 1
# print(count)

# заполнить масив от 0 до 9
# arr = list(range(10))
# print(arr)

# # 2,4,6,8, ....20
# arr = list(range(2, 21, 2))
# print(arr)

# # 10,9,8,7,.....0
# arr = list (range(10, -1, -1))
# # print(arr)

# s = "hello"
# arr = list(s)
# print(arr)

# num = 123456
# arr = list(str(num))
# for i in range(len(arr)):
#   arr[i] = int(arr[i])
# print(arr)

# s = "Roses are red and violets are blue"
# arr = s.split()
# print(arr)


# time = "12:15:10"
# arr = time.split(":")
# # print(arr)
# housr, minutes, seconds = time.split(":")
# print(housr, minutes, seconds)

# a = [1]
# b = [2]
# s = a + b
# print(s)
# p = a * 10
# print(p)

# [1,2.....n]
# def array(n):
#   return list(range(1, n+1))
# print(array(20))

# Колво чисел в массиве

# def count_nums(arr):
#   count = 0
#   for el in arr:
#     if type(el) == int or type(el) == float:
#       count += 1
#   return count

# print(count_nums([2, True, 'a', 3.14, -3, None, False]))


# вычислить кол-во строк в которых есть минимум 2 гласные
# def words(arr):
#   count_words = 0
#   for word in arr:
#     count = 0
#     for letter in word:
#       if letter in "AEUIOaeuio":
#         count += 1
#     if count >=2:
#       count_words += 1
#   return count_words

# print(words(["my", "apple", "banana", "in"]))

# возвратить"Obese".

# def index(weight, height):
#   bmi = weight / height ** 2
#   print(bmi)
#   if bmi <= 18.5:
#     return "Underweight"
#   elif bmi <= 25.0:
#     return "Normal"
#   elif bmi <= 30.0:
#     return "Overweight"
#   else:
#     return "Obese"
# print(index(95, 1.86))

# # 5. Напишите функцию planet_name, которая принимает n - номер планеты от Солнца и возвращает name - название планеты:
# # ·       n = 1: name = "Mercury"
# # ·       n = 2: name = "Venus"
# # ·       n = 3: name = "Earth"
# # ·       n = 4: name = "Mars"
# # ·       n = 5: name = "Jupiter"
# # ·       n = 6: name = "Saturn"
# # ·       n = 7: name = "Uranus"
# # ·       n = 8: name = "Neptune"

# def planet_name(n):
#   if n == 1:
#     return "Mercury"
#   elif n == 2:
#     return "Venus"
#   elif n == 3:
#     return "Earth"
#   elif n == 4:
#     return "Mars"
#   elif n == 5:
#     return "Jupiter"
#   elif n == 6:
#     return "Saturn"
#   elif n == 7:
#     return "Uranus"
#   elif n == 8:
#     return "Neptune"
#   else:
#     return "Wrong planet number"
# print(planet_name(5))

# # 6. Напишите функцию square_of_triangle, которая принимает три аргумента a, b, c (стороны треугольника) и возвращает площадь треугольника, если треугольник существует, или сообщение "The triangle does not exist", в противном случае. Площадь треугольника находится по формуле Герона: area = (p * (p - a) * (p - b) * (p - c)) ** 0.5, где p = (a + b + c) / 2

# def square_of_triangle(a, b, c):
#   p = (a + b + c) / 2
#   area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#   if area > 0:
#     return round(area)
#   else:
#     return "The triangle does not exist"
# print(square_of_triangle(3, 5, 6))

# # 7. Напишите функцию, которая принимает число n и возвращает количество делителей этого числа. Например, число 10 имеет 5 делителей : 1, 2, 5, 10. Число 12 имеет 6 делителей: 1, 2, 3, 4, 6, 12.

# def deliteli(n):
#   count = 0

#   for i in range (1, n+1):
#     if n % i == 0:
#       count += 1
#   return count
# print(deliteli(30))

# Домашнее задание № 9 Тема: Массивы (списки)
# 1.     Дан массив, содержащий числа. Найти сумму четных элементов массива.
# def SumOfEven(arr):
#   sumEven = 0
#   for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#       sumEven += arr[i]
#   return sumEven
# print(SumOfEven([8, -2, 9, 5, 6]))

# 2.     Найти произведение нечетных элементов массива.

# def MultOfOdd(arr):
#   odd = 1
#   for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#       odd = odd * arr[i]
#   return odd
# print(MultOfOdd([-3, 5, 8, 10, 40]))



# 3.     Найти среднее арифметическое элементов массива.

# def average(arr):
#   return sum(arr) / len(arr)
# print(average([3, 5, 8, 3, 7, -2]))

# 4.     Найти количество отрицательных элементов массива.

# def negative(arr):
#   sumNegative = 0
#   for i in range(len(arr)):
#     if arr[i] < 0:
#       sumNegative += arr[i]
#   return sumNegative
# print(negative([2, -5, -16, -1, 10]))

# 5.     Дан массив, содержащий слова. arr = ["apple", "appricot", "pineapple", "banana", "grape", "plum"]. Найдите количество слов длиной 5.

# def count5(arr):
#   count = 0
#   for el in arr:
#     if len(el) == 5:
#       count += 1
#   return count
# print(count5(["apple", "appricot", "pineapple", "banana", "grape", "plum"]))



# 6.     Дан массив, содержащий слова. arr = ["apple", "appricot", "pineapple", "banana", "grape", "orange"]. Найдите количество слов, которые начинаются с гласной буквы.

# def vowels(arr):
#   count = 0
#   for el in arr:
#     for i in el:
#       if el[0] in "aeuio":
#         count += 1
#         break
#   return count
# print(vowels(["apple", "appricot", "pineapple", "banana", "grape", "orange"]))

# 7.     Создайте массив, заполненный десятью нулями: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0].

# print([0] * 10)

# 8.   Создайте массив из 10 первых нечетных чисел: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19].

# print(list(range(1, 20, 2)))

# 9.   Создайте массив, содержащий десять чисел, являющихся степенями числа 2: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512].

# def two(n):
#   return [2 ** i for i in range(n)]
# print(two(10))

# 10.   Введите строку. Получите массив из слов строки, которые начинаются с гласной буквы.

# str = "Who create this test"
# arr = []
# for i, el in enumerate(str):
#   if el[0] in "uieao":
#     arr.append(el)
# print(arr)

# 11.   Задан массив arr, хранящий значение температуры в градусах Цельсия. arr = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]. Получите массив, содержащий значения температуры в градусах Фаренгейта.

# arr = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# arrF = []
# for el in arr:
#   far = el / 5 * 9 + 32
#   far = int(far)
#   arrF.append(far)
# print(arrF)

# 12.   Заполните массив 10 числами Фибоначчи. Первые два числа этой последовательности равны 0 и 1. А каждое следующее число, начиная с третьего, равно сумме двух предыдущих чисел: [0, 1, 1, 2, 3, 5, 8, 13, 21, 44] тут должно быть 34 или 44?

# arr = [0, 1]

# for i in range (1, 9):
#   fib = arr[-1] + arr[-2]
#   arr.append(fib)
# print(arr)