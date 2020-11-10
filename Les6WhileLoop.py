 # 1,2,3,4,5,6....10

# x = 1
# while x <= 10:
#   print(x)
#   x += 1

# x = 10
# while x <= 100:
#   print(x)
#   x += 10

# x = 10
# while x >= 0:
#   print(x)
#   x -= 1


# 1+2+3....+100

# x = 1
# s = 0
# while x <= 100:
#   s += x
#   x += 1
# print(f"s = {s}")

# факториал числа 10! = 1*2*3....10
# n! = 1*2*3*4....10
# n = 15
# f = 1
# x = 1
# while x <= n:
#   f = f * x
#   x += 1
# print(f"{n}! = {f}")

# сумма чисел ввеленных с клавиатуры до тех пор, пока не будет введено "q"
# s = 0
# while True:
#   n = input("Enter number: ")
#   if n == "q":
#     break
#   else:
#     s = s + int(n)
# print(f"s = {s}")

# округлить число до ближ большего числа кратного 5

# 1 ===> 5
# 2 ===> 5


# x = int(input("Enter number: "))
# while x % 5 != 0:
#   x += 1
# print(x)


# 1-10
# for x in range(1, 11):
#   print(x)


# 2,4,6,8,10

# for x in range(2, 11, 2):
#   print(x)


# 10, 9 , 8, ....0

# for x in range(10, -1, -1):
#   print(x)

# "1, 2,4,5,6,7....n"

# n = int(input("Enter n: "))
# s = ""
# for i in range (1, n+1):
#   s += str(i) + " "
# print(s)
# print(len(s))

# 2 case:

# n = int(input("Enter n: "))
# s = ""
# for i in range(1, n+1):
#   if i < n:
#     s += str(i) + " "
#     print(s)
#   else:
#     s += str(i)



# print(s)
# print(len(s))

# for i in range(10):
#   if i % 2 == 0:
#     continue
#   else:
#     print(i)
#     if i == 7:
#       break

#  for i in range(10)
#   print(i)
#   if i > 10:
#     break
#   else:
#     print("Hello")

# "*
# **
# ***
# ****"

# n = int(input("Enter n: "))
# s = ""
# for i in range(1, n+1):
#   if i < n:
#     s += "*" * i + "\n"
#   else:
#     s += "+" * i
# print(s)

# n = int(input("Enter number of levels: "))
# s = ""
# for i in range(1, 2*n, 2):
#   s = s + ("*" * i).center(2*n-1) + "\n"
# print(s)


 # 1.     Постройте строку “1 monkey 2 monkeys ... 10 monkeys”.

 # m = " monkeys "
 # st = ""
 # for i in range(2, 11):
 #   st += str(i) + m
 # print("1" + m.replace(m[-2], "")+ st)

 # 2.     Составьте строку, которая "отсчитывает" секунды до старта ракеты: "10 seconds...9 seconds...8 seconds...7 seconds...6 seconds...5 seconds...4 seconds...3 seconds...2 seconds...1 second"

 # m = " seconds... "
 # st = ""
 # for i in range(10, 1, -1):
 #   st += str(i) + m
 # print(st + "1" + m[:7])

 # 3.     Возведите число n в степень k, не используя операцию возведения в степень (n, k ввести с помощью input). Для того чтобы возвести число n в степень k, его необходимо k раз умножить на само себя.

 # n = int(input("Enter the number: "))
 # k = int(input("Enter the times: "))
 # s = 1
 # for i in range(k):
 #   s = s * n
 # print(s)

 # 4.     В первый день тренировок спортсмен пробежал 5 км. В каждый последующий день он пробегал на 5% больше, чем в предыдущий день. Напечатайте, сколько километров спортсмен пробегает ежедневно в течение 10 дней.

 # n = 5
 # for k in range(1, 11):
 #   n = n + (n * 0.05)
 #   print(n)

 # 5.     Ученик к моменту начала обучения не знает ни одного английского слова. В первый день занятий он выучил 5 английских слов. В каждый последующий день он выучивал на 2 слова больше, чем в предыдущий. Через сколько дней ученик будет знать не менее n английских слов?

 # day0 = 0
 # day1 = 5
 # day2 = 7.....

 # n = int(input(" Enter quantity of words: "))
 # total = 5
 # # n = 10
 # k = 5
 # days = 1
 # while total < n:
 #   k += 2
 #   total += k
 #   days += 1
 # print(days)


 # 6.     Получите строку, содержащую лесенку. Число «ступенек» ввести командой input.
 # #
 #  #
 #   #
 #    #

 # step = int(input("Enter quantity of steps: "))
 # s = ""
 # for i in range(1, step+1):
 #   s = s + "#" + " " * i + "#" + "\n"
 # print(s)

 # 7.     Нарисуйте ромб. Ширину (нечетное число, в данном примере это 7) ввести командой input. Используйте выравнивание строки по центру.
 #     *
 #    ***
 #   *****
 #  *******
 #   *****
 #    ***
 #     *


 # n = int(input("Enter the width of the rhombus: "))
 # sides = n
 # shape = "*" * n

 # while n > 1:
 #   n -= 2
 #   nextLine = ("*" * n).center(sides)
 #   shape = nextLine + "\n" + shape + "\n" + nextLine

 # print(shape)

 # 1.     Постройте строку “1 monkey 2 monkeys ... 10 monkeys”.

 # m = " monkeys "
 # st = ""
 # for i in range(2, 11):
 #   st += str(i) + m
 # print("1" + m.replace(m[-2], "")+ st)

 # 2.     Составьте строку, которая "отсчитывает" секунды до старта ракеты: "10 seconds...9 seconds...8 seconds...7 seconds...6 seconds...5 seconds...4 seconds...3 seconds...2 seconds...1 second"

 # m = " seconds... "
 # st = ""
 # for i in range(10, 1, -1):
 #   st += str(i) + m
 # print(st + "1" + m[:7])

 # 3.     Возведите число n в степень k, не используя операцию возведения в степень (n, k ввести с помощью input). Для того чтобы возвести число n в степень k, его необходимо k раз умножить на само себя.

 # n = int(input("Enter the number: "))
 # k = int(input("Enter the times: "))
 # s = 1
 # for i in range(k):
 #   s = s * n
 # print(s)

 # 4.     В первый день тренировок спортсмен пробежал 5 км. В каждый последующий день он пробегал на 5% больше, чем в предыдущий день. Напечатайте, сколько километров спортсмен пробегает ежедневно в течение 10 дней.

 # n = 5
 # for k in range(1, 11):
 #   n = n + (n * 0.05)
 #   print(n)

 # 5.     Ученик к моменту начала обучения не знает ни одного английского слова. В первый день занятий он выучил 5 английских слов. В каждый последующий день он выучивал на 2 слова больше, чем в предыдущий. Через сколько дней ученик будет знать не менее n английских слов?

 # day0 = 0
 # day1 = 5
 # day2 = 7.....

 # n = int(input(" Enter quantity of words: "))
 # total = 5
 # # n = 10
 # k = 5
 # days = 1
 # while total < n:
 #   k += 2
 #   total += k
 #   days += 1
 # print(days)


 # 6.     Получите строку, содержащую лесенку. Число «ступенек» ввести командой input.
 # #
 #  #
 #   #
 #    #

 # step = int(input("Enter quantity of steps: "))
 # s = ""
 # for i in range(1, step+1):
 #   s = s + "#" + " " * i + "#" + "\n"
 # print(s)

 # 7.     Нарисуйте ромб. Ширину (нечетное число, в данном примере это 7) ввести командой input. Используйте выравнивание строки по центру.
 #     *
 #    ***
 #   *****
 #  *******
 #   *****
 #    ***
 #     *


 # n = int(input("Enter the width of the rhombus: "))
 # sides = n
 # shape = "*" * n

 # while n > 1:
 #   n -= 2
 #   nextLine = ("*" * n).center(sides)
 #   shape = nextLine + "\n" + shape + "\n" + nextLine

 # print(shape)



