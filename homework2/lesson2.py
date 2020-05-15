# PEP8
var_str = 'строка'
a = len(var_str) # количество символов в строке
print(a)

b = var_str.isdigit() # другие в методичке
print(b)

c = var_str[-1]
d = var_str[len(var_str) - 1]
print(d)
print(c)

# var_str[start:step:stop]
e = var_str[0:3]
print(e)
f = var_str[0:3:2]
print(f)

g = var_str
h = var_str[:]
print(g)
print(h)

var_list = [1, 'kot', 'b', 't', 'd', ['l', 1, 2]]
i = var_list[5]
print(i)

a = [] # пустой список

j = list('hello')
print(j)

k = '-.'.join(['h', 'e', 'l', 'l', 'o'])
print(k)

l = 'h-.e-.l-.l-.o'.split('-.')
print(l)

var_list2 = [1, 2, 3, 4, ]
m = var_list2.append(55)
print(m)

n = var_list.append(var_list2)
print(n)

var_list3 = [1, 2, 3, [1, 2, 4, [1, 2, 5]]]
o = var_list3[-1][-1]
print(o)

var_tuple = (1, 2, 3, 4, 5, [1, 2, 3])  # turple нельзя изменять, но занимает меньше оперативной памяти и более безопасный код

p = var_tuple[-1].append('hello')
print(var_tuple)

var_set = {1, 2, 8, 3, 4, 5, 'g', 0, True, '', None} # разделяет уникальные значения true = 1 false = 0
q = var_set
print(q)

for itm in var_tuple:
    print(itm)

for itm2 in var_set:
    print(itm2)

var_list4 = [(1, 2), (3, 4), (5, 6)]

for r, s in var_list4[::-1]:
    print(r)
    print(r, s)

var_dict = {'KEY': 12345, 'KEY2':'bit', 0:'world', False: 1111, 'KEY': 444444}
t = var_dict['KEY']
u = var_dict['KEY2']
print(t)
print(u)

var_dict['KEY3'] = 213121
print(var_dict)

for key in var_dict.items():
    print(key)

for key2, value in var_dict.items():
    print(key2, value)
