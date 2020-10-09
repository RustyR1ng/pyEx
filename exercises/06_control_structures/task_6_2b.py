# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_right = False
while ip_right != True:
    ip = input("IP:")
    ip_copy = ip
    try:
        for i in range(4):
            if i == 3:
                num = int(ip_copy)
            elif i < 3 and ip_copy.find('.') != -1:
                num = int(ip_copy[:ip_copy.find('.')])
            else:
                num = -1
            if num < 0 or num > 255:
                error = 1/0
            ip_copy = ip_copy[ip_copy.find('.')+1:] if i < 3 else ip_copy
    except BaseException:
        print('Неправильный IP-адрес')
    else:
        ip_right = True
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
