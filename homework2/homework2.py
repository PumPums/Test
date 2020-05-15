# PEP8
# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

var_list = input('Напишите что-нибудь\n')
changes_list = var_list.split()
el = 0

for i in range(int(len(changes_list) / 2)):
    changes_list[el], changes_list[el + 1] = changes_list[el + 1], changes_list[el]
    el += 2
print(changes_list)
