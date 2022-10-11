"""
Задание 9.1
Создать функцию generate_access_config, которая генерирует конфигурацию
для access-портов.
Функция ожидает такие аргументы:
- словарь с соответствием интерфейс-VLAN такого вида:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/16': 17}
- шаблон конфигурации access-портов в виде списка команд (список access_mode_template)
Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_mode_template. В конце строк в списке не должно быть
символа перевода строки.
"""
"""
access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}


def generate_access_config(intf_vlan_mapping, access_template):
    ##intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
    ##    {'FastEthernet0/12':10,
    ##     'FastEthernet0/14':11,
    ##     'FastEthernet0/16':17}
    ##access_template - список команд для порта в режиме access
    ##Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    config=[]
    for intf, vlan in intf_vlan_mapping.items():
        config.append(f"interface {intf}")
        for template in access_template:
            if template.find("access vlan") != -1:
                config.append(f"{template} {vlan}")
            else:
                config.append(template)
    return config

print(generate_access_config(access_config, access_mode_template))
"""
"""
Задание 9.1a
Сделать копию функции generate_access_config из задания 9.1.
Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли
настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд
   port-security (находятся в списке port_security_template)
Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_mode_template и шаблона port_security_template,
если он был передан.
В конце строк в списке не должно быть символа перевода строки.
Проверить работу функции на примере словаря access_config, с генерацией конфигурации
port-security и без.
Пример вызова функции:
print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    ##intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
    ##    {'FastEthernet0/12':10,
    ##     'FastEthernet0/14':11,
    ##     'FastEthernet0/16':17}
    ##access_template - список команд для порта в режиме access
    ##Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    config=[]
    for intf, vlan in intf_vlan_mapping.items():
        config.append(f"interface {intf}")
        for template in access_template:
            if template.find("access vlan") != -1:
                config.append(f"{template} {vlan}")
            else:
                config.append(template)
        if psecurity:
            config.extend(psecurity)
    return config

print(generate_access_config(access_config, access_mode_template, port_security_template))
"""
"""
Задание 9.2
Создать функцию generate_trunk_config, которая генерирует
конфигурацию для trunk-портов.
У функции должны быть такие параметры:
- intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы
  такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
  списка команд (список trunk_mode_template)
Функция должна возвращать список команд с конфигурацией на основе указанных портов
и шаблона trunk_mode_template. В конце строк в списке не должно быть символа
перевода строки.
Пример итогового списка (перевод строки после каждого элемента сделан
для удобства чтения):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    ##intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы
    ## такого вида:
    ##{'FastEthernet0/1': [10, 20],
    ## 'FastEthernet0/2': [11, 30],
    ## 'FastEthernet0/4': [17]}
    ##trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
    ##списка команд (список trunk_mode_template)
    ##Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    config=[]
    for intf, vlan in intf_vlan_mapping.items():
        config.append(f"interface {intf}")
        for template in trunk_template:
            if template.find("allowed vlan") != -1:
                vlans=str(vlan).replace("[", "").replace("]", "")
                config.append(f"{template} {vlans}")
            else:
                config.append(template)
    return config

print(generate_trunk_config(trunk_config, trunk_mode_template))
"""
"""
Задание 9.2a
Сделать копию функции generate_trunk_config из задания 9.2
Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе
Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.
Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    config_dict={}
    
    for intf, vlan in intf_vlan_mapping.items():
        config=[]
        ##config.append(f"interface {intf}")
        for template in trunk_template:
            if template.find("allowed vlan") != -1:
                vlans=str(vlan).replace("[", "").replace("]", "")
                config.append(f"{template} {vlans}")
            else:
                config.append(template)
        config_dict[intf]=config
    return  config_dict

print(generate_trunk_config(trunk_config, trunk_mode_template))
"""
"""
Задание 9.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}
* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}
У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict= {}
    s=''
    with open(config_filename, 'r') as file:
        for line in file:
            if line.find("interface") != -1:
                intf=line.split()[1]
            elif line.find("access vlan") != -1:
                access_dict[intf] = line.split()[-1]
            elif line.find("allowed vlan") != -1:
                trunk_dict[intf] = line.split()[-1]
    return access_dict, trunk_dict 
           


name="C:/Users/karin/STUDY/2k_2c/Veb_rasr/config_sw11.txt"
print(get_int_vlan_map(name))
"""
"""
Задание 9.3a
Сделать копию функции get_int_vlan_map из задания 9.3.
Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto
То есть, порт находится в VLAN 1
В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }
У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw2.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict= {}
    s=''
    with open(config_filename, 'r') as file:
        for line in file:
            if line.find("interface") != -1:
                intf=line.split()[1]
            elif line.find("access vlan") != -1:
                access_dict[intf] = line.split()[-1]
            elif line.find("allowed vlan") != -1:
                trunk_dict[intf] = line.split()[-1]
            elif line.find("duplex auto") != -1:
                access_dict[intf] = 1
    return access_dict, trunk_dict 
           


name="C:/Users/karin/STUDY/2k_2c/Veb_rasr/config_sw2.txt"
print(get_int_vlan_map(name))
"""
"""
Задание 9.4
Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.
Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(file_name):
    conf_dict = {}
    with open(file_name) as file:
        for line in file:
            line = line.rstrip()
            if line and not (line.startswith("!") or ignore_command(line, ignore)):
                if line[0].isalnum():
                    section = line
                    conf_dict[section] = []
                else:
                    conf_dict[section].append(line.strip())
    return conf_dict

name="C:/Users/karin/STUDY/2k_2c/Veb_rasr/config_sw11.txt"
convert_config_to_dict(name)