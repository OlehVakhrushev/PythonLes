# a = True
# b = False
# print(type(a))
# a = 5 > 4
# print(a)


# print("A" > "B")
# print("A" < "B")

# print("A" < "a")
# print(10 % 2 == 0)

# num = 11
# print(num % 2 != 0)


# print(num > 9 and num < 100)
# print(9 < num < 100)

# day = 7
# print(day == 6 or day == 7)
# print(5 < day < 8)
# print(day in [6, 7])

# letter = 'a'
# print(letter == 'a' or letter == 'o' or......)
# print(letter in "aeuio")
# print(letter in [a, e, i,....])
# print(not letter in "aeiou")

# if condition:
#   operator1
#   ....
#   operator
# [else:
#   operator..
#   operator..
#   ]



# a = 10
# if a > 0:
#   print("positive")

# a = 12
# if a % 2 == 0:
#   print("Even")
# else:
#   print("Odd")

# a = 12
# if a > 0:
#   print("positive")
# elif a == 0:
#   print("zero")
# else:
#   print("negative")


# answer = input("Are you OK? ")
# if answer == ["Yes", "yes", "y", "Y"]:
#   print("Cool")
# else:
#   print("Get better!")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operation: ")
# if op == "+":
#   res = a + b
# elif op == "-":
#   res = a - b
# elif op == "*":
#   res = a * b
# elif op == "/" or op == ":":
#   res = a / b
# elif op == "//":
#   res = a // b
# elif op == "%":
#   res = a % b
# elif op == "**":
#   res = a ** b
# else:
#   print("Wrong operation")
# print(f"{a} {op} {b} = {res}")

# name = input("Enter name: ")
# if name[0] in "aeuioAEUIO":
#   print(f"{name}, your name starts with vowel!")
# else:
#   print(f"{name}< your name starts with constant!")


# age = int(input("How old are you? "))
# if age < 0:
#   print("Wrong age")
# elif 0 <= age <= 10:
#   print("Drink milk!")
# elif age < 18:
#   print("drink coke!")
# elif age < 21:
#   print("Drink beer!")
# else:
#   print("Drink wisky!")


# тернарный оператор

# num = 8
# description = "Even" if num % 2 == 0 else "Odd"
# print(description)


# name = "John"
# greet = "Hello boss" if name == "Bob" else f"Hello {name}"
# print(greet)

# Домашнее задание № 4. Тема «Условный оператор if else».
# 1.    В переменную name введите имя. Определите, начинается ли имя с согласной буквы.

# name = input("Enter your name: ")
# if name[0] in "aeiuoyAEIUOY":
#   print(f"{name}, your name starts with vowel!")
# else:
#   print(f"{name}, your name starts with constant!")

# 2.    С помощью команды input введите имя пользователя name. Если имя содержит более 5 букв, напечатайте "Your name is long!". В противном случае напечатайте "Your name is short!"

# name = input("Enter your name: ")
# if len(name) > 5:
#   print("Yuor name is long!")
# else:
#   print("Your name is short!")

# 3.    С помощью команды input введите имя пользователя name и время time в часах от 0 до 24.
# ·       Если время от 0 до 6 (включительно), напечатайте "Good night, name";
# ·       если время от 7 до 11 (включительно), напечатайте "Good morning, name";
# ·       если время от 12 до 18 (включительно), напечатайте "Good day, name";
# ·       если время от 19 до 24 (включительно), напечатайте "Good night, name";
# ·       иначе напечатайте "Wrong time".

# name = input("Enter your name: ")
# time = int(input("Enter your time: "))
# if  0 <= time <= 6:
#   print(f"Good night, {name}.")
# elif 7 < time <= 11:
#   print(f"Good morning, {name}.")
# elif 12 < time <= 18:
#   print(f"Good day, {name}.")
# elif 19 < time <= 24:
#   print(f"Good night, {name}.")
# else:
#   print("Wrong time.")


# 4.    Введите цену товара price.
# ·       Если price >= 300, вы получаете скидку 30%;
# ·       иначе если price >= 200, вы получаете скидку 20%;
# ·       иначе если price >= 100, вы получаете скидку 10%;
# ·       если цена меньше 100, скидки нет. Найдите итоговую стоимость товара.

# price = int(input("Enter price: "))
# if price >= 300:
#   price1 = price * 0.7
#   print(f"Your price, {price1}")
# elif price >= 200:
#   price2 = price * 0.8
#   print(f"Your price, {price2}")
# elif price >= 100:
#   price3 = price * 0.9
#   print(f"Your price, {price3}")
# else:
#   price = price
#   print("Here is no discount ONLY for you!")

# 5.    Введите возраст человека age.
# ·       Если age<16 напечатайте "children";
# ·       иначе если age<50 напечатайте "young man";
# ·       иначе напечатайте "senior".

# age = int(input("Enter your age: "))
# if age < 16:
#   print("You are children")
# elif age < 50:
#   print("You are young man")
# else:
#   print("senior")

# 6.    В переменную current_color введите цвет сигнала светофора ('red','yellow','green'). Напечатайте следующий цвет сигнала светофора (смена цветов такая: 'red' ---> 'green', 'green' ---> 'yellow', 'yellow' ---> 'red').

# color = input("Enter color: ")
# if color == "red":
#   print("Next color is green!")
# elif color == "green":
#   print("Next color is yellow!")
# elif color == "yellow":
#   print("Next color is red!")
# else:
#   print("You entered invalid color.")
