# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
ignore = ["duplex", "alias", "Current configuration"]

reading_file = argv[1]
writing_file = argv[2]

with open(reading_file, 'r') as r_file, open(writing_file, 'a') as w_file:
    for line in r_file.readlines():
        for word in ignore:
            if line.find(word) != -1:
                break
        else:
            w_file.write(line)
