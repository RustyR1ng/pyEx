# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line[1:].strip().replace(
        '[', '').replace(']', '').replace('via', '').replace(',', '').split()
    print('''
    Prefix              {}
    AD/Metric           {}
    Next-Hop            {}
    Last update         {}
    Outbound Interface  {}
    '''.format(*line))
