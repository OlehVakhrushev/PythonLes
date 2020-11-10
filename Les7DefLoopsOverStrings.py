# s = "world"
# for i in range(len(s)):
#    print(i, s[i])

# for i in range(len(s)-1, -1, -1):
#    print(i, s[i])

# for letter in s:
#   print(letter)


# s = "1 potato, 2 potato, 3 potatos, 4!"
# count = 0
# for el in s:
#   if el.isdigit():
#     count += 1
# print(count)

# count = 0
# for i in range(len(s)):
#   if s[i].isdigit():
#     count += 1
# print(count)


# rev = s[::-1]
# print(rev)

# t = ""
# for el in s:
#   t = el + "*" + t
# print(t)

# p = ""
# for i in range(len(s)-1, -1, -1):
#   p = p + s[i] + "*"
# print(p[:-1])


# s = "winter"
# for i, el in enumerate(s):
#   print(i, el)


# t = ""
# for i, el in enumerate(s):
#   if i % 2 == 0:
#     t += el.upper()
#   else:
#     t += el.lower()
# print(t)

# s = "May 9 is holiday"
# for el in s:
#   if el.isdigit():
#     print("Yes")
#     break
# else:
#   print("No")

# s = "May 9 is holiday"
# t = ""
# for el in s:
#   if el == "":
#     t += el
#   else:
#     t += el * 2
# print(t)

# def add(a, b):
#   return a + b
# print(add(3, 4))

# def greet(name="user"):
#   return f"Hello {name}!"
# print(greet("Larisa"))


# def say_hello(name):
#   return f"Hello boss!" if name == "John" else f"Hello {name}"
# print(say_hello("Ann"))
# print(say_hello("John"))



# def vowel_count(s):
#   s = s.lower()
#   count = 0
#   for el in s:
#     if el in "aeuio":
#       count += 1
#   return count

# print(vowel_count("I like Python"))

# def factorial(n):
#   f = 1
#   for i in range(1, n+1):
#     f *= i
#   return f

# print(factorial(7))

# Домашнее задание № 7. Тема Циклы. Работа со строками
# 1.     Посчитайте количество заглавных букв в строке.

# s = "Hello Oleg, how are you?"
# count = 0
# for el in s:
#   if el.isupper():
#     count += 1
# print(count)

# 2.     Посчитайте общее количество гласных в строке (в верхнем и нижнем регистре).

# s = "Hello Oleg, how are you?"
# count_up = 0
# count_lo = 0
# for el in s:
#   if el.isupper():
#     count_up += 1
#   elif el.islower():
#     count_lo += 1
# print(count_up, count_lo)

# 3.     Задайте строку с произвольным значением (например, "Python"). Получите строку, в которой все буквы будут разделены звездочками ("P*y*t*h*o*n").

# s = "Python"
# t = ""
# for el in s:
#   t = el + "*" + t
#   rev = t[::-1]
# print(rev)


# 4.     Вставьте пробелы после всех неалфавитных символов строки (путем создания новой строки). Например, s = "Bananas,2apples,sweets and 8plums". Получить "Bananas, 2 apples, sweets and 8 plums".

# s = "Bananas,2apples,sweets and 8plums"
# t = ""
# for el in s:
#   if el.isalpha():
#     t += el
#   else:
#     t = t + el + " "
# print(t)

# 5.     Задайте строку с произвольным значением (например, "summer"). Получите строку, в которой гласные буквы станут заглавными ("sUmmEr").

# s = "summer"
# t = ""
# for el in s:
#   if el in "aueoi":
#     t += el.upper()
#   else:
#     t += el
# print(t)

# 6.     Дана строка. Получить две новые строки: одну - из символов с четными индексами, другую - из символов с нечетными индексами. Например, s = "separate". Новые строки: "sprt", "eaae".

# s = "separate"
# even = ""
# odd = ""
# for i, el in enumerate(s):
#   if i % 2 == 0:
#     even += s[i]
#   else:
#     odd += s[i]
# print(even, odd)

# 7.     Ввести строку, включающую строчные и прописные буквы. Вывести ту же строку в одном регистре, который зависит от того, каких букв больше. При равном количестве преобразовать в нижний регистр. Например, вводится строка "HeLLo World", она должна быть преобразована в "hello world", потому что в исходной строке малых букв больше.

# s = "HeLLo World"
# count_up = 0
# count_lo = 0
# for el in s:
#   if el.isupper():
#     count_up += 1
#   elif el.islower():
#     count_lo += 1
# if count_lo > count_up:
#   s = s.lower()
# else:
#   s = s.upper()
# print(s)