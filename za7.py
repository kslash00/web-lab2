"""
Задание 7.1
Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
file = open('C:/Users/karin/STUDY/2k_2c/Veb_rasr/ospf.txt', 'r')
for line in file:
    line_format = line.replace("[", "").replace("]", "").replace(",", "")
    line_format = line_format.split()
    print("Prefix             {}".format(line_format[1]))
    print("AD/Metric          {}".format(line_format[2]))
    print("Next-Hop           {}".format(line_format[4]))
    print("Last update        {}".format(line_format[5]))
    print("Outbound Interface {}".format(line_format[6]))
file.close()
"""
"""
Задание 7.2
Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt.
Имя файла передается как аргумент скрипту.
Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.
Вывод должен быть без пустых строк.
Ограничение: Все задания надо выполнять используя только пройденные темы.
Пример вывода:
$ python task_7_2.py config_sw1.txt
Current configuration : 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
 duplex auto
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
interface Ethernet0/2
 duplex auto
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
...
"""
"""
name_file='C:/Users/karin/STUDY/2k_2c/Veb_rasr/config_sw1.txt' 
with open(name_file, 'r') as file:
    for line in file:
        if(line[0]!="!"):
            print(line.rstrip())
"""
"""
Задание 7.2a
Сделать копию скрипта задания 7.2.
Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.
При этом скрипт также не должен выводить строки, которые начинаются на !.
Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
ignore = ["duplex", "alias", "configuration"]

name_file='C:/Users/karin/STUDY/2k_2c/Veb_rasr/config_sw1.txt' 
with open(name_file, 'r') as file:
    for line in file:
        if(line[0]!="!"):
            if line.find(ignore[0])==-1:
                if line.find(ignore[1])==-1:
                    if line.find(ignore[2])==-1:
                                        print(line.rstrip())
"""
"""
Задание 7.2b
Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл
Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
from sys import argv

ignore = ["duplex", "alias", "configuration"]

src_file = "C:/Users/karin/STUDY/2k_2c/Veb_rasr/config_sw1.txt"
dst_file = "C:/Users/karin/STUDY/2k_2c/Veb_rasr/config_sw1_72.txt"

with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        for line in src:
         if(line[0]!="!"):
            if line.find(ignore[0])==-1:
                if line.find(ignore[1])==-1:
                    if line.find(ignore[2])==-1:
                          dst.write(line)
"""
"""
Задание 7.3
Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
name_file='C:/Users/karin/STUDY/2k_2c/Veb_rasr/CAM_table.txt' 
with open(name_file, 'r') as file:
    for line in file:
        line_list=line.split()
        if line_list and line_list[0].isdigit():
            print("{:<9} {:<20} {:<}".format(line_list[0], line_list[1], line_list[3]))
"""
"""
Задание 7.3a
Сделать копию скрипта задания 7.3.
Переделать скрипт: Отсортировать вывод по номеру VLAN
В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9
Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.
Подсказка: Для сортировки удобно сначала создать список списков такого типа,
а потом сортировать.
[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]
Сортировка должна быть по первому элементу (vlan), а если первый элемент одинаковый,
то по второму. Так работает по умолчанию функция sorted и метод sort, если сортировать
список списков выше.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
name_file='C:/Users/karin/STUDY/2k_2c/Veb_rasr/CAM_table.txt' 

list_save=[]

with open(name_file, 'r') as file:
    for line in file:
        line_list=line.split()
        if line_list and line_list[0].isdigit():
            vlan, mac, intf = line_list[0], line_list[1], line_list[3]
            list_save.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(list_save):
    print(f"{vlan:<9}{mac:20}{intf}")
"""
"""
Задание 7.3b
Сделать копию скрипта задания 7.3a.
Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.
Пример работы скрипта:
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

name_file='C:/Users/karin/STUDY/2k_2c/Veb_rasr/CAM_table.txt' 

list_save=[]

with open(name_file, 'r') as file:
    for line in file:
        line_list=line.split()
        if line_list and line_list[0].isdigit():
            vlan, mac, intf = line_list[0], line_list[1], line_list[3]
            list_save.append([int(vlan), mac, intf])

number=input('Enter VLAN number: ')


for vlan, mac, intf in sorted(list_save):
    if int(number) == vlan:
        print(f"{vlan:<9}{mac:20}{intf}")