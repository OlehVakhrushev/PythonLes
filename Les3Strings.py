# s = "CROCODILE"
# print(type(s))
# print(len(s))

# print(s[0])
# print(s[8])
# print(s[len (s)-1])
# print(s[-1])

# print(s[1:4])  # 1-3
# print(s[3:6])
# print(s[0:-1])
# print(s[:-1])  # s[0: -1]

# print(s[1:-1])
# print(s[5:])
# print(s[:])
# print(s[0:8:2])
# print(s[::2])
# print(s[::-1]) # reverse

# concatenation
# a = "my"
# b = "home"
# s = a + b
# s1 = b + a
# print(s, s1)
# s2 = a + "\n" + b
# print(s2)

# умножение строки на число

# s = "Hello!"
# print((s + " ") * 5)

# print("*" * 20)


# x = -12
# print(abs(x))

# x1 = 10
# x2 = 14
# dist = abs(x1 - x2)
# print(dist)

# x = 12.656456
# print(int(x))
# print(round(x))
# print(round(x, 2))

# a = 12
# b = 15
# c = 7
# maximum = max(a, b, c)
# minimum = min(a, b, c)
# print(maximum, minimum)


# s = "CROCODILE"
# print(s.count("O"))

# print(s.index("O"))
# print(s.rindex("O"))
# print(s.index("a")) # Error

# print(s.find("O")) # 2
# print(s.rfind("O") # 4
# print(s.find("a")) # -1

# monkey ---> m----y

# word = input("Enter word: ")
# count_dash = len(word) - 2
# code = word[0] + "-" * count_dash + word[-1]
# print(code)


# time = "12:15:10"
# hour = int(time[:2])
# print(hour)
# minutes = int(time[3:5])
# print(minutes)
# seconds = int(time[-2:])
# print(seconds)
# total = hour*3600 + minutes*60 + seconds
# print(total)

# r1 = int(input("Enter resilt of 1 sportsman: "))
# r2 = int(input("Enter resilt of 2 sportsman: "))
# r3 = int(input("Enter resilt of 3 sportsman: "))
# res = min(r1, r2, r3)
# print(res)

# s = "warm evening"
# i = s.index(" ")
# print(i)
# first = s[:i]
# print(first)
# second = s[i+1:]
# print(second)
# new_s = second + " " + first
# print(new_s)

# Домашнее задание № 3. Тема «Строки. Получение части строки. Умножение строки на число. Поиск индекса подстроки в строке».


# 1. С помощью команды input введите в переменную name значение вашего имени. Напечатайте длину имени, первую букву имени, последнюю букву имени. Результат работы программы должен быть такой:
# What is your name? > Andrew
# Andrew, your  name has 6 letters
# Andrew,  your name starts with letter ”A”
# Andrew< your name ends with letter ”w”

# name = input("What is your name? ")
# print(f"{name}, your name has {len(name)} letters")
# print(f"{name}, your name starts with letter '{name[0]}'")
# print(f"{name}, yuor name ends with letter '{name[-1]}'")

# 2. С помощью команды input в переменную name введите имя. Напечатайте приветствие, перевернув имя. Например, name = "Alice", надо напечатать "Hello, ecilA!"

# name = input("Enter name: ")
# print(f"Hello, {name[::-1]}! ")

# 3. Дана строка, содержащая 10 цифр, например, s = "1234567890". С помощью операции конкатенации и операции выделения части строки получить строку в формате телефонного номера: "(+123) 456-7890".

# s = "1234567890"
# print("(" + s[:3] + ") " + s[3:6] + "-" +s[6:])



# 4. Ввести строку name, содержащую имя и фамилию, разделенные пробелом. Преобразуйте эту строку в формат адреса электронной почты. Например name = "Alice Moon" преобразовать в "Alice.Moon@company.com".

# name = "Oleg Vakhrushev"
# i = name.index(" ")
# print(i)
# first = name[:i]
# second = name[i+1:]
# print(f"{first}.{second}@company.com")

# 5. Введите слово. Заключите слово в рамку из звездочек. Например, если введено слово "summer", вывести:
# image.png
# image.pn

# word = input("Enter word:")
# length = len(word)+2
# print("*" * length + "\n" + "*" + word + "*" + "\n" + "*" * length)