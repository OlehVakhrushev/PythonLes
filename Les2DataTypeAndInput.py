# num = 5
# print(5)
# print(type(num))   # num

# num = 1.5
# print(num)
# print(type(num))   # float

# s = 'sun'
# print(type(s))   # str


# b = True
# b = False
# print(b)
# print(type(b)) # bool

# b = 4 <= 5
# print(b)
# print(type(b))

# n = 5
# print(n)
# n = float(n)
# print(n)

# n = 15.01
# n = int(n)
# print(n)

# s = '10'
# print(s)
# print(type(s))
# s = int(s)
# print(s)
# print(type(s))


# s = '12.3'
# print(s)
# print(type(s))
# s = float(s)
# print(s)
# print(type(s))

# num = 123
# print(type(num))
# num = str(num)
# print(type(num))


# print("Student #" + str(1))

# b = 0 > 1
# s = str(b)
# print(s)

# num = int(b)
# print(num)
# n = float(b)
# print(n)


# print(bool(1))
# print(bool(0))
# print(bool("hi"))
# print(bool(''))

# a = int(input("Enter fisrt number: "))
# print(a)
# b = int(input("Enter second number: "))
# print(b)
# s = a + b
# print(s)

# print(f"{a} + {b} = {s}")

# name = input("What is yuor name? ")
# print(f"Hello, {name}!")

# time = input("What is time of day now?")
# print(f"Good {time}, {name}!")

# people = int(input("enter number of people: "))
# perc_inc = int(input("enter percentage of growth: "))
# number_dec = int(input("Enter number of decrease:  "))
# people = int(people + people * perc_inc / 100 - number_dec)
# print(f"People in a year will be {people}")


# num = 123.64567
# print(int(num))
# num = int(num)
# print(num)
# print(round(num))
# print(round(num, 2))

# import math
# year = 1705
# century = math.ceil(year / 100)
# print(century)

# Домашнее задание № 2. Тема «Типы данных. Преобразование типов. Ввод данных».
# 1.     С помощью команды input введите трехзначное число и найдите сумму его цифр.
import math
number = int(input("Please enter your number: "))
sum = (number % 10) + ((number // 10) % 10) + number // 100
print(f"Sum of numbers is:, {sum}")

# 2.     С помощью команды input введите число сторон правильного многоугольника и найдите сумму его внутренних углов. Сумма углов n-угольника равна 180*(n-2).

num = int(input("Quantity of sides of the polygon: "))
sum = 180 * (num - 2)
print(f"Sum of inside corners is: {sum}")

# 3.     С помощью команды input запросите у пользователя количество миль (miles). Переведите это расстояние в километры и футы. 1 mile = 1.60934 km, 1 mile = 5280 feet.

mil = int(input("Enter your miles: "))
km =  mil * 1.60934
fit = mil * 5280
print(f"Converted in km: {km}")
print(f"Converted into feet: {fit}")

# 4.     С помощью команды input запросите у пользователя число градусов Фаренгейта (fahrenheit) и переведите это значение в градусы Цельсия (celsius). Для этого нужно от числа градусов Фаренгейта отнять 32, результат умножить на 5 и затем поделить на 9.

far = int(input("Enter fahrenheit here: "))
cel = int((far - 32) * 5 /9)
print(f"Converted in celsius: {cel} C")

# 5.     С помощью команды input запросите у пользователя число градусов Цельсия (celsius). Напишите программу перевода градусов Цельсия в градусы Фаренгейта (fahrenheit). Для этого нужно число градусов Цельсия умножить на 9, затем разделить на 5 и затем к результату прибавить 32.

cel = int(input("Enter celsius: "))
far = int((cel * 9) / 5) + 32
print(f"Converted in fahrenheit: {far} F")

# 6.     С помощью команды input запросите у пользователя стоимость заказа (price), процент чаевых (tip_percent) и процент налогов (tax_percent). Найдите общую стоимость заказа (total_price).

price = float(input("Enter your price: "))
tip_percent = float(input("Enter tip %: "))
tax_percent = float(input("Enter tax %: "))
total = price + (tip_percent * price / 100) + (tax_percent * price / 100)
print(f"Your total payment: {total}")

# 7.     С помощью команды input введите цену товара со скидкой и процент скидки. Найдите цену товара до скидки (полную цену товара), результат округлите до 2-х знаков после запятой. Например, товар со скидкой стоит 40 долларов при скидке 50%. Тогда цена товара без скидки составляет 80 долларов. Если товар стоит 40 долларов при скидке 10 процентов, его полная цена составляет $ 44.44.

price = float(input("Enter price: "))
discount = int(input("Enter % of dispount: "))
fprice = round((price / (100 - discount) * 100), 2)
print(f"Original price was: {fprice}")