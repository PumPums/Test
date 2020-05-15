# PEP8
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']

while True:
    number_str = input('Введите номер месяца\n')
    if number_str.isdigit():
        number_str = int(number_str)
        break

while True:
    number = number_str
    if number in number_list:
        number = int(number)
        break

dict1 = {}

for a, b in zip(number_list, seasons_list):
    dict1[a] = b

answer = dict1.get(number)
print(answer)


