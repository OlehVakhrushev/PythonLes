# s = "programming language"
# print(len(s))
# print(s[0])
# print(s[-1])
# print(s[3:8])
# print(s[::-1])

# print(s.index(" "))
# print(s.rindex("g"))
# print(s.find("g"))
# print(s.rfind("g"))
# print(s.find("P"))


#  s = "sky"
# # print(s.isalpha())
# s = '7up'
# print(s.isalpha())

# s = "2020"
# print(s.isdigit())

# a = "2a"
# print(a.isdigit())

# s = 'october20'
# print(s.isalnum())
# s = 'october 20'
# print(s.isalnum())


# s = "PAVS"
# print(s.isupper())

# s = "Pavs"
# print(s.isupper())
# print(s.islower())
# print('pasv'.islower())

# s = "programming language"
# print(s.count("g"))  # 4
# print(s.count("b"))  # 0
# print(s.count("ram"))

# s = "Hello"
# # print(s.rjust(20))
# # print(s.ljust(20))
# num = 12
# num = str(num).rjust(5, "0")
# print(num)
# print(s.center(20, "*"))

# s = "my flOwers aRe beaUtiful"
# print(s.lower())
# st = s.lower()
# print(st)
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print(s.startswith("my"))
# print(s.endswith("beaUtiful"))

# print("a" in s)
# print("o" in "aeuio")
# print(not "n" in "aeuio")

# s = "my flOwers aRe beaUtiful"
# print(s.strip())
# print(s.lstrip(),"-")
# print(s.rstrip(),"-")

# s = "my flOwers aRe beaUtiful"
# s1 = s.replace(" ","")
# print(s1)
# s2 = s.replace("flOwers", "friends")
# print(s2)

# word = input("Enter word: ")
# width = int(input("Enter width of box: "))
# if width < len(word) + 2:
#   print("word to long for task")
# else:
#   print(width * "*")
#   print("*", word.center(width-2)+ "*")
#   print(width * "*")

# Домашнее задание № 5. Тема: Тернарный оператор. Функции работы со строками


# 1. Дана переменная num_of_day, хранящая номер дня недели. Присвоить переменой day значение “ Weekend”, если номер дня 6 или 7, и “Work day” в противном случае. Выполните это задание с использованием тернарного оператора.

# num_of_day = int(input("day of the week (from 1 to 7): "))
# if num_of_day == 6 or num_of_day == 7:
#   print("Weekend")
# else:
#   print("Work day")

# 2. Дано число n. Число является "счастливым", если оно делится на 9. Присвойте переменной is_lucky значение "Lucky number", если число делится на 9, и "Not a lucky number" в противном случае. Выполните это задание с использованием тернарного оператора.

# num = int(input("Enter yiur number: "))
# if num % 9 == 0:
#   print("Lucky number")
# else:
#   print("Not a lucky number")

# 3. Создайте переменную phrase и присвойте ей значение "My eyes are green too!" С помощью команды input спросите у пользователя "What is your favorite color? " Замените слово "green" в переменной phrase на любимый цвет пользователя и напечатайте полученную фразу.

# phrase = "My eyes are green too!"
# eyes = input("What is your favorite color? ")
# res = phrase.replace("green", eyes)
# print(res)


# 4. С помощью функции input введите first_name, middle_name, last_name. Выведите эти три слова в столбик, выравнивание по правому краю в строке с длиной, равной длине самого длинного из имен. Используйте функцию max для нахождения максимальной длины слов.
#       Ava
# Charlotte
#     Smith

# first = input("Enter your first name: ")
# mid = input("Enter your middle name: ")
# last = input("Enter your last name: ")
# long = max(len(first), len(mid), len(last))
# print(first.rjust(long))
# print(mid.rjust(long))
# print(last.rjust(long))


#  5. Создайте переменную s и присвойте ей значение произвольной строки. Удалите в этой строке все гласные буквы. Например, s = “We like Python”. Результат должен быть “W lk Pythn”.

# s = input("Enter your string: ")
# for i in "aeuioAEUIO":
#   s = s.replace(i, "")
# print(s)

# 6. С помощью команды input введите строку. Затем введите слово, которое надо заменить. Потом введите заменяющее слово. Выведите результат. Например, введены: строка "Have a good day", слово "good", слово "nice". Результат должен быть: "Have a nice day".

# string = "Have a nice day"
# print(string.replace("good", "nice"))

# 7. Задана строка. В начале и конце строки есть некоторое количество пробелов. Получить строку, в которой каждое слово написано в заглавной буквы, пробелы в начале строки удалены, а пробелы в конце строки заменены на такое же количество восклицательных знаков. Например, s = "   I like summer  ". Получить "s = "I Like Summer!!!"

# s = "   I like summer  "
# s = s.title().lstrip()
# len = len(s) - len(s.strip())
# print(s.strip() + "!"*len)