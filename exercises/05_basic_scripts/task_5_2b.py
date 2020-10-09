# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ip = argv[1]
ipNetwork = ip[:ip.find('/')].split('.')
ipMask = ip[ip.find('/'):]
ipBin = "{0:08b}{1:08b}{2:08b}{3:08b}".format(
    int(ipNetwork[0]), int(ipNetwork[1]), int(ipNetwork[2]), int(ipNetwork[3]))[:int(ipMask[1:])]+"0"*(32-int(ipMask[1:]))
ipBin = (ipBin[:8]+' '+ipBin[8:16]+' ' +
         ipBin[16:24]+' '+ipBin[24:]).split()

network = '''{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'''.format(int(ipBin[0], 2), int(ipBin[1], 2), int(ipBin[2], 2), int(ipBin[3], 2))
maskBin = '1' * int(ipMask[1:])+'0' * (32-int(ipMask[1:]))
maskBin = (maskBin[:8]+' '+maskBin[8:16]+' ' +
           maskBin[16:24]+' '+maskBin[24:]).split()

mask = '''{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'''.format(int(maskBin[0], 2), int(maskBin[1], 2), int(maskBin[2], 2), int(maskBin[3], 2))

out = f"Network:\n{network}\nMask:\n{ipMask}\n{mask}"
print(out)
