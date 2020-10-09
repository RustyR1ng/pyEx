# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = input('VLAN: ')

with open('CAM_table.txt', 'r') as r_file:
    lines = []
    vlans = []
    for line in r_file.readlines()[6:]:
        line = line.split()
        lines.append(line)

for i in range(len(lines)):
    for j in range(len(lines)-1):
        if int(lines[j][0]) > int(lines[j+1][0]):
            temp = lines[j][0]
            lines[j][0] = lines[j+1][0]
            lines[j+1][0] = temp
for line in lines:
    if(line[0] == vlan):
        print("{0:6}{1:17}{3:}".format(*line))
