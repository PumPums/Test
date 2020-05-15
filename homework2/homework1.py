# PEP8

#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.

lorem_list = list('Contrary to popular belief, Lorem Ipsum is not simply random text.')
lorem_list.append(1023542)
lorem_list.insert(3, 3.23523)
lorem_list.insert(10, True)
lorem_list.insert(20, None)
lorem_list.insert(40, [1, 3, 3, 'e'])
lorem_list.insert(50, (3, 5, True, 'l'))
lorem_list.reverse()
print(lorem_list)

for i in lorem_list:
    print(f'{i} is {type(i)}')
