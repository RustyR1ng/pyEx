# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input("IP:")
ip_copy = ip
for i in range(4):
    try:
        if i == 3:
            num = int(ip_copy)
        elif i < 3 and ip_copy.find('.') != -1:
            num = int(ip_copy[:ip_copy.find('.')])
        else:
            num = -1
        if num < 0 or num > 255:
            print('Неправильный IP-адрес')
            break
    except BaseException:
        print('Неправильный IP-адрес')
        break
    ip_copy = ip_copy[ip_copy.find('.')+1:] if i < 3 else ip_copy
else:
    if ip == "0.0.0.0":
        print("unassigned")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif int(ip[:ip.find('.')]) >= 1 and int(ip[:ip.find('.')]) <= 223:
        print("unicast")
    elif int(ip[:ip.find('.')]) >= 224 and int(ip[:ip.find('.')]) <= 239:
        print("multicast")
    else:
        print("unused")
