# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    result_access = dict()
    result_trunk = dict()
    mode = ''
    with open(config_filename, 'r') as file:
        temp = list()
        for line in file:
            if line.find('interface') != -1:
                temp.append(line[10:].rstrip())
                while line.find('!') == -1:
                    line = file.readline().strip()
                    temp.append(line)
            print(temp)

    return result_access, result_trunk


print(get_int_vlan_map(
    "C:/Users/R1/Desktop/09_functions/config_sw1.txt"))
