# letter = input("Введите букву")
# if  letter == 'a' or letter == 'e' or letter == 'i' or letter == 'u' or letter == 'o':
#     print("буква гласная")
# elif letter == 'y':
#     print('Буква может быть как гласная так и согласная')
# else:
#     print("буква согласная")
import math

# a=1
# b=3
# while (a!=5):
#     a+=1


# string = input("Введите числа через пробел:")
# list_of_strings = string.split()
# list_of_numbers = list(map(int, list_of_strings))
# print(sum(list_of_numbers[::3]))

# L = list(map(float, input("Введите числа через пробел:").split()))
# L[0], L[-1] = L[-1], L[0]
# L.append(sum(L))
# print(L)

# title = input("Введите название книги:")
# author = input("Введите фамилию автора:")
# year = int(input("Введите год издания:"))
#
# book = {'title': title,
#         'author': author,
#         'year': year}
#
# print(book)


# text = input("Введите текст:")
# c = list(set(text))
# print(c)

# text = input("Введите текст:")
# unique = list(set(text))
# print("Количество уникальных символов: ", len(unique))

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print (list_id_before==list_id_after)

# money = int(input("Введите сумму вклада:"))
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# deposit = []
# for key in per_cent:
#     deposit.append(per_cent[key]*money/100)
# max_deposit = max(deposit)
# print("Максимальная сумма, которую вы можете заработать:"+str(int(max_deposit)

# name=("Ivan")
# for i in name:
#     print (i)

# numbers_1 = list("5")
# # print(numbers_1)

# people = ['Ivan', 'Tom', 'Kate']
# if 'Kate' in people:
#   people.remove('Kate')
# print(people)

# people = ['Ivan', 'Tom', 'Kate']
# people_count= people.count('Tom')
# print(people_count)

# a = [5, 3, 1, 4, 2]
# print(sorted(a))

# people = ['Ivan', 'Tom', 'Kate']
# print(sorted(people))

# people = [['Ivan', 29], ['Tom', 27], ['Kate',32]]
# print(people[1][1])

# users = {1: 'Ivan', 2: 'Tom', 3: 'Kate'}
# key = 4
# if key in users:
#     user = users [key]
#     print(user)
# else :
#     print('элемент не найден')

# users = {1: 'Ivan', 2: 'Tom', 3: 'Kate'}
# for key in users.keys():
#     print(key)


# users_1 = {'Ivan', 'Tom', 'Kate'}
# users_2 = {'Sam', 'Bob', 'Tom'}
# users_3 = users_1.union(users_2)
# print(users_3)

# users_1 = {'Ivan', 'Tom', 'Kate'}
# users_2 = {'Sam', 'Bob', 'Tom'}
# users_3 = users_1.intersection(users_2)
# print(users_3)

# users_1 = {'Ivan', 'Tom', 'Kate'}
# users_2 = {'Sam', 'Bob', 'Tom'}
# users_3 = users_1.symmetric_difference(users_2)
# print(users_3)


# year = int (input("Введите год: "))
# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     if year % 4 == 0:
#         return  True
#     if year % 100 != 0:
#         return False
# print(year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

# N = int (input ("Введите число: "))
# '3' in str(N) and '7' in str(N)
# print('7' in str(N))
# print('3' in str(N))

# a = [1,2,3]
# b = [1,2,3]
# print(id(a))
# print(id(b))

# is_rainy = False # дождь будет

# if is_rainy:
#     print("Брать зонт")
# else:
#     print("Не брать зонт")

# is_rainy = True # дождь будет
# heavy_rain = False  # не сильный дождь
# if is_rainy:
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")

# dedlin = False
# t = 17
# if t>15 and not dedlin:
#     print("Идем гулять")
# else:
#     print("остаемся дома")

# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("После исключения")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")

# age = int(input("How old are you?"))
#
# if age > 100 or age <= 0:
#     raise ValueError("Тебе не может быть столько лет")
#
# print(f"Тебе {age} лет!")

# try:
#     string = str(input("Введите числа: "))
#
#     print(int(string))
# except ValueError as e:
#     print("Ошибка")
# else:
#     print("Всё ништяк")
# finally:
#     print("Выход из программы!")



# # def are_both_odd(A, B):
# A = int(input("Введите число А: "))
# B = int(input("Введите число B: "))
# if A % 2 == 1 and B % 2 == 1:
#     print('Числа А и B нечетные')
# else:
#     print('упс')



# a = int(input("Введите число a: "))
# if a == 10:
#     print('a равно 10')
# elif a < 10:
#     print('a меньше 10')
# else:
#     print('a больше 10')

# month = int(input("Введите номер месяца: "))
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# # elif month in [12, 1, 2]:
# else:
#     print("Зима")

# def get_wind_class(speed):
# speed = int (input("Введите класс ветра: "))
# if speed in [1]:
#     print("weak")
# elif speed in [2]:
#     print("moderate")
# elif speed in [3]:
#     print("strong")
# else:
#     print ("hurricane")

# def get_wind_class(speed): #объявление функции
#     speed = int (input("speed: "))
#     if 1 <= speed <= 4: #только аргумент
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return"strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(3)) #мы просим программу напечатать то, что в скобках

# user_database = {'user': 'password'}
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False

# A = int(input('Введите первое число: '))
# B = int(input('Введите второе число: '))
# C = int(input('Введите третье число: '))
#
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')

# A = int(input('Введите число\n'))
#
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print("Число не принадлежит интервалу")
# else:
#     print("Число принадлежит интервалу")

# A = int (input("Ведите двухзначное число: "))
# first_digit = A // 10
# second_digit = A % 10
#
# print((first_digit == 5) or (second_digit == 5))

# list_ = [int(input("Введите числа: "))]
#
# print(len(list_) == len(set(list_)))

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# print(len(list_) == len(set(list_)))

# num = int(input("введите восьмизначное число: "))
#
# print(str(num) == str(num)[::-1])

# print(list(range(5)))

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5
#
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# P = 1   # заводим переменную-счетчик, в которой мы будем считать произведение, подумайте чему она должна быть равна
# N = 5
# for i in range(1, N+1):
#     print("Текущее число: ", i)
#     # P= P * i
#     P*= i       # умножение и присваивание
#     print("Значение произведения после умножения: ", P)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: произведение равно = ", P)

# n=5
# for i in range (1, n+1):
#     print("*" * i)

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
#
# # заводим цикл while, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n)

# S = 0  # заводим переменную-счетчик
# n = 1   # текущее натуральное число
#
# # заводим цикл while, который будет работать, пока реультат не превысит 1000
# while S<1000:  # делай пока ... (Можно так: n**2<1000)
#     S = n**2
#     n += 1  #  увеличиваем переменную-счетчик
#     print("Ещё считаю...")
#
# print("Конец программы")
# print("Количество чисел: ", n)

# n = 1
# while True:
#    if n ** 2 >= 1000:
#        print("Последнее число", n - 1)
#        break
#    n += 1


# N = 2
# M = 3
# # заполнили матрицу последовательными числами
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
#
#
# for i in range(N):  # цикл, отвечающий за строки
#     for j in range(M):  # цикл, отвечающий за столбцы
#         print(matrix[i][j], end=" ")
#     print()


# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
# for row in random_matrix:  # здесь мы целиком берем каждую строку
#    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#    max_index = 0
#    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#    max_value = row[max_index]  # для максимального значения тоже самое
#    for index_col in range(len(row)):
#        if row[index_col] < min_value:
#            min_value = row[index_col]
#            min_index = index_col
#        if row[index_col] > max_value:
#            max_value = row[index_col]
#            max_index = index_col
#    min_value_rows.append(min_value)
#    min_index_rows.append(min_index)
#    max_value_rows.append(max_value)
#    max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")


# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")


# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i in range(len(list_)):
#     if list_[i] < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)


# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# # for i in range(len(list_)):
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", value)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)


# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
#
# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")


# name = str("Lena")
# age = 40
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут %(name)s. Мне %(age)d лет." % {"name": name, "age": age})
# print(f"Меня зовут {name}. Мне {age} лет.")
# print(f" Мне {age + 10} лет.")

# n = int(input("Введите число: "))
# while True:
#     if n % 3 == 0:
#          n = n // 3
#          if n == 1:
#               break
#     else:
#          break


# n = int(input("Введите число: \n"))
#
# while True:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = (n * 3 + 1) // 2
#     print(n)
#
#     if n == 1:
#         print("Done")
#         break


# В клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги. Узнайте число фазанов и число кроликов.
# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")


# def print_ladder (n):
#     for i in range (1, n+1):
#         if n<=5:
#             print("*" * i)
#         else:
#             break


# some_var = None
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))



# some_var = (2,)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))


# a = '' # пустая строка
# b = a or 1
# print(b)


# print( 1 and "hello" and [False])


# print([] or 3.14 or False)
# # 3.14


# print(0 or '' or False)
# # False

# a = None
# if a is None:
#     b = 1
# else:
#     b = a
# print (b)


# a = "foo"
# b = "bar"
#
# print(1 and a or b)


# a = ""
# b = "bar"
#
# print(1 and a or b)


# a=1
# b=0
# if a and b:
# # пусть a и b - переменные, которые мы хотим проверитьif ??? : # проверка истинности обеих переменных
#     print("Обе переменные истинные")
#     print(a,b)


# a=5
# b=1
# # пусть a и b - переменные, которые мы хотим проверить
# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b) # печать одной переменной, той, которая является истинной
# else:
#     a and b is None
#     print("Обе переменные ложные")


# a = int(input("Введите число: "))
# if type(a) == int:
#     if 100 <= a <= 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print("Число удовлетворяет условиям")


# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print("Число удовлетворяет условиям")


# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print("Число удовлетворяет условиям")

#
# L = list(map(int, input().split()))
#
# print(all(L))


# squares = [i**2 for i in range(1,11)]
# print (squares)

#
# squares = [i**2 for i in range(1,11) if i % 2 == 1]
# print(squares)
# # [1, 9, 25, 49, 81]


# list_tuples = [(i, i**2) for i in range(1,11)]
# print(list_tuples)


# M = [[i+j for j in range(5)] for i in range(5)]
# print (M)


# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(T)


# L = [input("число") for i in range(5)]
# print(i)

# L = [int(input(""))%2 == 0  for i in range(5)]
# print(L)

# L = [int(input()) % 2 == 0 for i in range(5)]
# print( any(L))


# L = input()
# any([L]) and not all([L])
# print()


# L = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1
# print(L)
# print(M)
# N = [ ]

# for i in range(10):
#     N.append(L[i] * M[i])
#     print(N)

# for a in zip(L,M):
#     print(a)

# for a, b in zip(L,M):
#     print('a =', a, 'b =', b)


# L = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]
# for a, b in zip (L,M):
#     N= a * b
# N = [a*b for a,b in zip(L,M)]
# print(N)


# text = input()
# first = text[0]  # сохраняем первый символ
# count = 0  # заводим счетчик
# result = ''  # и результирующую строку
#
# for c in text:
#     if c == first:  # если символ совпадает с сохраненным,
#         count += 1  # то увеличиваем счетчик
#     else:
#         result += first + str(count)  # иначе - записываем в результат
#         first = c  # и обновляем сохраненный символ с его счетчиком
#         count = 1
#
# result += first + str(count)  # и добавляем в результат последний символ
# print(result)


# all_tickets = int(input("Введите количество билетов: "))
# ages = []
# for i in range(0, all_tickets):
#     input_value = int(input(f"Введите возраст участника №{i+1}:\n"))
#     ages.append(input_value)
#     def prise(age):
#         if age < 18:
#             return 0
#         elif 18 <= age <= 25:
#             return 990
#         else:
#             return 1390
#     full_prise = sum(map(prise, ages))
# discount_prise = int(full_prise*0.9)
# if all_tickets > 3:
#     print("Стоимость всех билетов со скидкой: ", discount_prise, "руб.")
# else:
#     print("Стоимость всех билетов: ", full_prise, "руб.")


# def print_2_add_2():
#    result = 2 + 2
#    print(result)
#
# print_2_add_2()


# def hello_world():
#     print("Hello World")
#
# hello_world()
# hello_world()


# def func(num):
#     print(num**2)
# func(2)
# func(3)
# func(4)


# # функция, которая возводит любое число в степень n
# def pow_func(base, n=2):
#    print(base ** n)
#
# pow_func(3)  # 9
# pow_func(5, 3)  # 125


# def num(a, n):
#    if a % n == 0:
#        print(f"Число {n} является делителем числа {a}")
#    else:
#        print(f"Число {n} не является делителем числа {a}")
# num(5,2)
# num(4,2)


# def reverse_stair(n):
#    for i in range(n,0,-1):
#       print("*" * i)
#
# reverse_stair(10)


# def pow_func(base, n=2):
#    print(base ** n)
# # pow_func(3)
# print(pow_func(3))
# # 9
# # None


# def pow_func(base, n=2):
#     result = base ** n
#     return result
#
# # print(pow_func(3))
# # # 9
# outside_result = pow_func(3)
# print(outside_result)
# # 9


# def num(a):
#     count = 0
#     print(a)


# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    print(count)
# get_multipliers(5)  # 2
# get_multipliers(4)  # 3


# def check_palindrome(str_):
#    str_ = str_.lower()
#    str_ = str_.replace(" ", "")
#
#    if str_ == str_[::-1]:
#        print(True)
#    else:
#        print(False)
#
# check_palindrome("test")  # False
# check_palindrome("Кит на море не романтик")  # True


# def my_func(a, b):
#     print(a+b)
# my_func(1, 2)

# def my_func (a, b):
#     result = a + b
#     return result
# c = my_func(1, 2)
# print(c)


# def local():
#    x = 5  # локальная переменная
#    print(x)
#
# x = 10
# local()
# print(x)

# 5
# 10


# def local():
#   print(x)  # так как x нет в локальной области видимости, мы берем её из глобальной области
#
# x = 10
# local()
# print(x)


# x = 3
# def function():
#     print(x)
#     return x
#
# print(function())


# x = 3
#
# def func():
#    global x
#    print(x)
#    x = 5
#    x += 5
#    return x
# func()
# print(func())


# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()  # Hello


# def get_mul_func(m):
#    nonlocal_m = m
#
#    def local_mul(n):
#       return n * nonlocal_m
#
#    return local_mul
#
#
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# two_mul(5)  # 5 * 2
# print(two_mul(5))


# def func(a, b, c):
#    print('a =', a)
#    print('b =', b)
#    print('c =', c)
#
# func(1, 2, 3)
# # a = 1
# # b = 2
# # c = 3
#
# func(3, 2, 1)
# # a = 3
# # b = 2
# # c = 1
#
# func(a=1, b=2, c=3)
# # a = 1
# # b = 2
# # c = 3
#
# func(c=3, b=2, a=1)
# # a = 1
# # b = 2
# # c = 3


# print(1)
# print(1, 2)
# print(1, 2, 3)


# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def my_func(*args, **kwargs):
#    print(type(args))
#    print(type(kwargs))
#
# my_func()
# # <class 'tuple'>
# # <class 'dict'>


# def adder(*nums):
#    sum_ = 0
#    for n in nums:
#       sum_ += n
#
#    return sum_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))  # 6


# def mul(*nums):
#    pr_ = 1
#    for n in nums:
#       pr_ *= n
#
#    return pr_
#
#
# print(mul())
# print(mul(1))
# print(mul(1, 2))
# print(mul(1, 2, 3))


# def incorrect_func(name_arg=[]):
#    # name_arg является локальной переменной
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# incorrect_func()
# print('-----')
# incorrect_func()


# # установим аргумент name_arg пустым а внутри функции будем проверять его
# def correct_func(name_arg=None):
#    if name_arg is None:
#        name_arg = []
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# correct_func()
# print('-----')
# correct_func()
# print('-----')
# correct_func([123])
# print('-----')
# correct_func(name_arg=[123])


# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#        return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# rec_fibb(10)  # 55
# print(rec_fibb(10))


# def rec_sum(n):
#    if n == 1:  # терминальный случай
#        return 1
#    return n + rec_sum(n - 1)  # рекурсивный вызов


# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# reverse_str('test')  # tset
# print(reverse_str('test'))


# def sum_digit(N):
#     if N<10:
#         return N
#     else:
#         return N % 10 + sum_digit(N//10)
# sum_digit(123)
# print(sum_digit(123))


# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step



# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)


# # для примера возьмём строку
# str_ = "my tst"
# str_iter = iter(str_)
#
# print(type(str_))  # строка
# print(type(str_iter))  # итератор строки
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))


# def twice_func(inside_func):
#     """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
#     inside_func()
#     inside_func()
#
# def hello():
#     print("Hello")
#
# twice_func(hello)


# def make_adder(x):
#    def adder(n):
#        return x + n # захват переменной "x" из nonlocal области
#    return adder  # возвращение функции в качестве результата
# add_5 = make_adder(5)
# print(add_5(10))  # 15
# print(add_5(100))  # 105


# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
#
# print(my_function())
# # Я - оборачиваемая функция!
# # 0
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())
# # Я буду выполнен до основного вызова!
# # Я - оборачиваемая функция!
# # Я буду выполнен после основного вызова!
# # 0

#
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")


# def my_decorator(fn):
#    def wrapper():
#        fn()
#    return wrapper  # возвращается задекорированная функция, которая заменяет исходную
#
# # выведем незадекорированную функцию
# def my_function():
#    pass
# print(my_function)  # <function my_function at 0x7f938401ba60>
#
# # выведем задекорированную функцию
# @my_decorator
# def my_function():
#    pass
# print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>


# декоратор, в котором встроенная функция умеет принимать аргументы
# def do_it_twice(func):
#    def wrapper(*args, **kwargs):
#        func(*args, **kwargs)
#        func(*args, **kwargs)
#    return wrapper
#
# @do_it_twice
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Oo!!!


# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper

#
# def counter(func):
#    count = 0
#    def wrapper(*args, **kwargs):
#        nonlocal count
#        func(*args, **kwargs)
#        count += 1
#        print(f"Функция {func} была вызвана {count} раз")
#    return wrapper
#
# @counter
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз
#
# say_word("Ooo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз


# def f(n):
#    return n * 123456789
# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper


# def linear_solve(a, b):
#     return b/a
# # 2*x = 9
# print(linear_solve(2, 9))


# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
# # 2*x = 9
# print(linear_solve(2,9))


# my_list = [i for i in range (1,11)]
# print(my_list)


# def D(a,b,c):
#     return b**2 - 4*a*c
#
#     def quadratic_solve(a, b, c):
#         if D(a, b, c) < 0:
#             return "Нет вещественных корней"
#         elif D(a, b, c) == 0:
#             return -b / (2 * a)
#         else:
#             return (-b - D(a, b, c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)
#
# L = list(map(float, input().split()))
# print(quadratic_solve(L[0], L[1], L[2]))


# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])


# def mirror(a, res=0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a // 10, res * 10 + a % 10)
#
# print(mirror(106))


# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)
# print(equal(23,5))


# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение


# def e():
#     n = 1
#
#     while True:
#         yield (1 + 1 / n) ** n
#         n += 1


# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
#
# @is_auth
# def from_db():
#     print("some data from database")
#
# from_db()
#
# @is_auth
# def change_profile():
#     print("Profile has been changed")


# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)

# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()


# def map_(func, some_list):
#     # some_list объект, над которым будет производиться преобразование
#     # func функция, которая должна выполняться над каждым объектом
#     outp = []
#     for i in range(len(some_list)):
#         outp.append(func(some_list[i]))
#     return outp
#
#
# print(list(map(pow_, a_list)))  # [1, 4, 9]
#
# for i in map(pow_, a_list):
#    pass


# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))


# def filter(func, cont):
#     outp = []
#     for x in cont: # проходим циклом по итерируемому объекту
#         if func(x): # проверяем условие для каждого элемента
#             outp.append(x) # если True, добавляем в новый список
#     return outp


# Из заданного списка вывести только положительные элементы
# def positive(x):
#     return x > 0  # функция возвращает только True или False
#
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))   # [1, 2]


# Из заданного списка вывести только четные элементы
# def even(x):
#     return x % 2 == 0 # функция возвращает только True или False
#
# result = filter(even, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))   # [-2, 0, 2]


# # map + filter
# some_list = [i - 10 for i in range(20)]
# def pow2(x): return x**2
# def positive(x): return x > 0
#
# print(some_list)
# print(list(map(pow2, filter(positive, some_list))))


# map(func, list1)  # итератор, но никаких вычислений не будет произведено
# list(map(...))  # только здесь появляется объект
#
# [func(i) for i in list1]  # сразу готовый объект
#
#
# [func(i) for i in list1] == list(map(func, list1))  # результат один и тот же


# list(map(lambda x: x ** 2, range(1, 11)))


#
# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
#
# # Чтобы отсортировать его по ключам, нужно сделать так:
# print(dict(sorted(d.items())))
# # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}
# sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря


# # (вес, рост)
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
# sorted(data, key = lambda x: x[0] / x[1] ** 2)
# print(min(data, key=lambda x: x[0] / x[1] ** 2)) # отбор по ключу


# myFile = open('namefile.txt', 'w')
# myFile.write('tttt\n')
# print('zzzz', file=myFile)


# myFile = open('hello.txt', 'r')
# file=myFile.read()
# print(file)
# myFile.close()


# myFile = open('filename.txt', 'w', encoding='utf8')
# myFile.write('елочка')


# myFile = open('snowtree.txt', 'r', encoding="utf8")
# file= myFile.read()
# print(file)
# # print(myFile.read())
# myFile.close()


# with open('snowtree.txt', encoding='utf8') as myFile:
#     print(myFile.read())


# with open('snowtree.txt', encoding='utf8') as myFile:
#     a=myFile.readline()
#     print(a)


# подсчитать количество слов
# file = open('...txt')
# data =file.read()
# words = data.split()  - разбить на слова
# print(len(words)) - подсчитать и показать количество слов
# file.close()


# создать из словаря JSON  объект:
#
# data = {
#     "name": "Ivan",
#     "age": 26,
#     "city": "Saratov"
# }
# with open('data_file.json', 'w') as f:
#     json.dump(data, f)

#
# def changeText(text):
#     """
#     Функция принимает строку с текстом.
#     Убирает все знаки препинания и возвращает
#     список, состоящий из слов текста.
#     """
#
#
# for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
#     text = text.replace(i, '')
#
# return text.split()
#
#
# def mostCommon(text, length=0):
#     """
#     Функция принимает список и ограничение по длине.
#     Возвращает самый часто встречающийся элемент.
#     Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
#     """
#
#
# most_common = []
# qty_most_common = 0
#
# for item in text:
#     if len(item) > length:
#         qty = text.count(item)
#         if qty > qty_most_common:
#             qty_most_common = qty
#             most_common = [item]
#         elif qty == qty_most_common:
#             most_common.append(item)
#
# return list(set(most_common))
#
#
# def mostLength(text):
#     """
#     Функция принимает список.
#     Возвращает самый длинный элемент.
#     Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
#     """
#
#
# most_length = []
# qty_most_length = 0
# alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for item in text:
#     for char in item:
#         if char not in alphabet:
#             charEn = False
#         else:
#             charEn = True
#
#     if charEn:
#         qty = len(item)
#         if qty > qty_most_length:
#             qty_most_length = qty
#             most_length = [item]
#         elif qty == qty_most_length:
#             most_length.append(item)
#
# return list(set(most_length))
#
# nameFile = input('Название файла: ')
#
# with open(nameFile, encoding='utf8') as f:
#     fileText = f.read()
#
# fileText = changeText(fileText)
# print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
# print(f'Список самых длинных английских слов: {mostLength(fileText)}')

# input(int("Введите число: "))
# N = int(num)
# SELECT num FROM N WHERE num > 3 AND num
#  < 100;


# class User:
#     pass
#
# peter = User()
# peter.name = "Peter Robertson"
#
# julia = User()
# julia.name = "Julia Donaldson"
#
# print(peter.name)
# print(julia.name)
#
# peter.email = "peterrobertson@mail.com"
# print(peter.email)
# print('\n')


# class User:
#     number_of_fingers = 5
#     number_of_eyes = 2
#
# lancelot = User()
# print(lancelot.number_of_fingers)


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
# julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")
#
# print(peter.name)
# print(julia.email)


# class Product:
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
# eggs = Product("eggs", "food", 5)
# print(eggs.is_available())


# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
# events = [
#     {
#        "timestamp": 1554583508000,
#         "type": "itemViewEvent",
#         "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#      },
#      {
#        "timestamp": 1555296337000,
#        "type": "itemViewEvent",
#        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#        "timestamp": 1549461608000,
#        "type": "itemBuyEvent",
#        "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#      },
#      ]
# for event in events:
#          event_obj = Event(timestamp=event.get("timestamp"),
#              event_type=event.get("type"),
#              session_id=event.get("session_id"))
#          print(event_obj.timestamp)


# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
# events = [
#         {
#             "timestamp": 1554583508000,
#             "type": "itemViewEvent",
#             "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#         },
#         {
#             "timestamp": 1555296337000,
#             "type": "itemViewEvent",
#             "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#         },
#         {
#             "timestamp": 1549461608000,
#             "type": "itemBuyEvent",
#             "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#         },
#     ]
#
# for event in events:
#     event_obj = Event()
#     event_obj.init_from_dict(event)
#     print(event_obj.timestamp)


# import datetime
#
#
# class Product:
#     max_quantity = 100000
#
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
#
# class Food(Product):
#     is_critical = True
#     needs_to_be_refreshed = True
#     refresh_frequency = datetime.timedelta(days=1)
#
#
# eggs = Food(name="eggs", category="food", quantity_in_stock=5)
# print(eggs.max_quantity)
# print(eggs.is_available())


# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
#     def show_description(self):
#         print("This is generic event.")
#
#
# class ItemViewEvent(Event):
#     type = "itemViewEvent"
#
#     def __init__(self, timestamp=0, session_id="", number_of_views=0):
#         self.timestamp = timestamp
#         self.session_id = session_id
#         self.number_of_views = number_of_views
#
#     def show_description(self):
#         print("This event means someone has browsed an item.")
#
#
# if __name__ == "__main__":
#     test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
#     test_view_event.show_description()
#     print(test_view_event.type)


# class Rectangle:
#     def __init__(self, x, y, width, heigth):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.heigth = heigth
#
#     def __str__(self):
#         return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.heigth}.'
#
#
# rect_1 = Rectangle(5, 10, 50, 100)
# print(rect_1)


# class Rectangle:
#     def __init__(self, x, y, width, heigth):
#         self.x=x
#         self.y=y
#         self.width=width
#         self.heigth=heigth
#
#     def __str__(self):
#         return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.heigth}.'
#     def get_area(self):
#         return self.width * self.heigth
#
# rect_1=Rectangle(5,10,50,100)
# print(rect_1)
# print(rect_1.get_area())


# class Customers:
#     def __init__(self, first_name, second_name, city, balance):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.balance = balance
#         self.city = city
#
#     def __str__(self):
#         return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''
#
#
# customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
# print(customer_1)


# class Customers:
#     def __init__(self, first_name,second_name,city, balance):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.balance = balance
#         self.city=city
#
#     def __str__(self):
#         return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''
#
#     def get_guest(self):
#         return f'{self.first_name} {self.second_name},г. {self.city}'
#
#
# costomer_1 = Customers('Иван','Петров','Москва',50)
# costomer_2 = Customers('Владимир','Зайцев','Кострома',50)
# costomer_3 = Customers('Олеся','Янина','Новосибирск',50)
#
# guest_list=[costomer_1,costomer_2,costomer_3]
#
#
# for guest in guest_list:
#     print(guest.get_guest())


# n=10000
# one=n**2
# two=n*math.log2(n)
# print(one/two)


# def p(n):
#     if n == 0:
#         return
#     else:
#         p(n-1)
#         print(n)
# p(5)


# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент — открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит, возвращаем True, иначе — False
#     return len(stack) == 0
# print(par_checker('(5+6)*(7+8)/(4+3)'))


# pars = {")": "(", "]": "["}


# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0


# N_max = int(input("Определите размер очереди:"))

# queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")
#
#
#
#
# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head
#
#
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №1 добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
# def show(): # выводим приоритетную задачу
#     print("Задача №1 в приоритете" % (queue[head]))
# def do(): # выполняем приоритетную задачу
#     global head
#     print("Задача №1 выполнена" % (queue[head]))
#     queue[head] = 0 # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max # и циклично перемещаем указатель


# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#             if self.left_child is None:
#                 self.left_child = BinaryTree(next_value)
#             else:
#                 new_child = BinaryTree(next_value)
#                 new_child.left_child = self.left_child
#                 self.left_child = new_child
#             return self
#
#     def insert_right(self, next_value):
#             if self.right_child is None:
#                 self.right_child = BinaryTree(next_value)
#             else:
#                 new_child = BinaryTree(next_value)
#                 new_child.right_child = self.right_child
#                 self.right_child = new_child
#             return self
# создаём корень и его потомков /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
#         def pre_order(self):
#             print(self.value) # процедура обработки
#
#             if self.left_child is not None: # если левый потомок существует
#                 self.left_child.pre_order() # рекурсивно вызываем функцию
#
#             if self.right_child is not None: # если правый потомок существует
#                 self.right_child.pre_order() # рекурсивно вызываем функцию
#             node_root.pre_order()
# def post_order(self):
#     if self.left_child is not None: # если левый потомок существует
#         self.left_child.post_order() # рекурсивно вызываем функцию
#
#     if self.right_child is not None: # если правый потомок существует
#         self.right_child.post_order() # рекурсивно вызываем функцию
#     print(self.value) # процедура обработки


# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R


# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL)


# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))


# def count(array, element):
#     count = 0
#     for a in array:
#         if a == element:
#             count += 1
#     return count


# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находим середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))


# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698


# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# count=0
# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count+=1
#         if array[j] < array[idx_min]:
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]
#
#
# print(array)
# print(count)


# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):
#     for j in range(len(array) - i - 1):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)


# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count=0
# for i in range(1, len(array)):
#
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         array[idx] = array[idx-1]
#         count += 1
#         idx -= 1
#     array[idx] = x
# print(count)


# def merge_sort(L):  # "разделяй"
#     if len(L) < 2:  # если кусок массива меньше 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
#
# def merge(left, right):  # "властвуй"
#     result = []  # результирующий массив
#     i, j = 0, 0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result


# def qsort(array, left, right):
#     middle = (left + right) // 2
#
#     p = array[middle]
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)


# import random
#
#
# def qsort_random(array, left, right):
#     p = random.choice(array[left:right + 1])
#     i, j = left, right
#     while i <= j:
#         count=0
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             count += 1
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort_random(array, left, j)
#     if right > i:
#         qsort_random(array, i, right)


# array = [int(x) for x in input("Введите числа от 1 до 999 в любом порядке, через пробел: ").split()]
#
# def merge_sort(array):  # "разделяй"
#
#
#     if len(array) < 2:  # если кусок массива равен 2,
#         return array[:]  # выход из рекурсии
#     else:
#         middle = len(array) // 2  # ищем середину
#         left = merge_sort(array[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(array[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
#
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result
#
# print(merge_sort(array))
#
#
# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# while True:
#     try:
#         element = int(input("Введите число от 1 до 999: "))
#         if element < 0 or element > 999:
#             raise Exception
#         break
#     except ValueError:
#         print("Нужно ввести число!")
#     except Exception:
#         print("Неправильный диапазон!")
#
#
# print(binary_search(array, element, 0,  len(array)))


# import requests
#
# r = requests.get(
#     'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
# print(r.content)


# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# print(r.status_code)  # узнаем статус полученного ответа


# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ
# print(r.content)


# import requests
# import json  # импортируем необходимую библиотеку
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50], '\n')


# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# print(r.content)


# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
#
# print(type(d))
# print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений


# import requests
#
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
# print(r.content)  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет


# import requests
# import json
#
# data = {'key': 'value'}
#
# r = requests.post('https://httpbin.org/post', json=json.dumps(
#     data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
# print(r.content)


# import requests
# import json
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
#
# r = json.loads(r.content)
#
# print(r[0])

# import telebot
#
# TOKEN = "6001190744:AAEWW8iibHDc_FWayhc9H7EZWnKAYxTgIo0"
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(content_types=["voice"])
# def repeat(message:telebot.types.Message):
#     bot.send_message(message.chat.id, "Какой смешной у тебя голос!")
# # bot.polling(none_stop=True)
#
# # Обрабатываются все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass
#
# @bot.message_handler(commands=['start', 'help'])
# def repeat(message: telebot.types.Message):
#     bot.reply_to(message, f"Салют, {message.chat.username}")
#
# bot.polling(none_stop=True)


# import requests  # импортируем наш знакомый модуль
# import lxml.html
# from lxml import etree
#
# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python
#
# # tree = lxml.html.document_fromstring(html)
# # title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.
# #
# # print(title)  # выводим полученный заголовок страницы
#
#
#
# # from lxml import etree
#
# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.
#
# ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
#
# # создаём цикл? в котором будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
#     time = li.find('time')
#     print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием


# import lxml.html
#
# html = ''' <html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>
# '''
#
# tree = lxml.html.document_fromstring(html)
#
# text = tree.xpath('/html/body/tag1/tag2/text()')
#
# print(text)

