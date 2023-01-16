# letter = input("Введите букву")
# if  letter == 'a' or letter == 'e' or letter == 'i' or letter == 'u' or letter == 'o':
#     print("буква гласная")
# elif letter == 'y':
#     print('Буква может быть как гласная так и согласная')
# else:
#     print("буква согласная")

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
# print("deposit")
# print("Максимальная сумма, которую вы можете заработать:" + str(max_deposit))

print("Hello")