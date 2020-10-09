# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

templates = {"access": {"template": access_template, "quiz": "Введите номер VLAN:"},
             "trunk": {"template": trunk_template, "quiz": "Введите разрешенные VLANы:"}}
workMode = input("Введите режим работы интерфейса (access/trunk):")
typeI = input("Введите тип и номер интерфейса:")
vlanNum = input(templates[workMode]["quiz"])
template = templates[workMode]["template"]
out = '''interface {}
{}'''.format(typeI, '\n'.join(template).format(vlanNum))
print(out)
