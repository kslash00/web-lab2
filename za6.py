"""
Задание 6.1
Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX Однако, в оборудовании Cisco
MAC-адреса используются в формате XXXX.XXXX.XXXX
Написать код, который преобразует MAC-адреса в формат cisco и добавляет их в новый
список result.
Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.
"""
"""
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []

for mac2 in mac:
    result.append(mac2.replace(":", "."))

print (result)
"""
"""
Задание 6.2
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
ips=input('Введите IP-адрес: ')
ip_list_str=ips.split(".")
i=0
ip_list =[]
while i<4:
    ip_list.append(int(ip_list_str[i]))
    i=i+1

if 1 <= ip_list[0] <= 223:
        print("unicast")
elif 224 <= ip_list[0] <= 239:
        print("multicast")
elif ips == "255.255.255.255":
        print("local broadcast")
elif ips == "0.0.0.0":
        print("unassigned")
else:
    print("unused")
"""
"""
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.
"""
"""
ips=input('Введите IP-адрес: ')
ip_list_str=ips.split(".")

prov=1
if len(ip_list_str) != 4:
    prov=0

for i in ip_list_str:
    if not i.isdigit() or int(i) < 0 or int(i) > 255 or prov==0:
        prov=0
        break

if prov==0:
    print("Неправильный IP-адрес")

else:
    i=0
    ip_list =[]
    while i<4:
        ip_list.append(int(ip_list_str[i]))
        i=i+1

    if 1 <= ip_list[0] <= 223:
        print("unicast")
    elif 224 <= ip_list[0] <= 239:
        print("multicast")
    elif ips == "255.255.255.255":
        print("local broadcast")
    elif ips == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
"""
"""
Задание 6.2b
Сделать копию скрипта задания 6.2a.
Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.
Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
"""
swich=1
while swich:
 ips=input('Введите IP-адрес: ')
 ip_list_str=ips.split(".")

 prov=1
 if len(ip_list_str) != 4:
    prov=0

 for i in ip_list_str:
    if not i.isdigit() or int(i) < 0 or int(i) > 255 or prov==0:
        prov=0
        break

 if prov==0:
    print("Неправильный IP-адрес")
 else:
    swich=0


i=0
ip_list =[]
while i<4:
    ip_list.append(int(ip_list_str[i]))
    i=i+1

if 1 <= ip_list[0] <= 223:
        print("unicast")
elif 224 <= ip_list[0] <= 239:
        print("multicast")
elif ips == "255.255.255.255":
        print("local broadcast")
elif ips == "0.0.0.0":
        print("unassigned")
else:
        print("unused")
"""
"""
Задание 6.3
В скрипте сделан генератор конфигурации для access-портов.
Сделать аналогичный генератор конфигурации для портов trunk.
В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ними делать (добавлять, удалять, перезаписывать).
Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка
указывает как воспринимать номера VLAN, которые идут дальше.
Пример значения и соответствующей команды:
* ['add', '10', '20'] - команда switchport trunk allowed vlan add 10,20
* ['del', '17'] - команда switchport trunk allowed vlan remove 17
* ['only', '11', '30'] - команда switchport trunk allowed vlan 11,30
Задача для портов 0/1, 0/2, 0/4, 0/5, 0/7:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only
Код не должен привязываться к конкретным номерам портов. То есть,
если в словаре trunk будут другие номера интерфейсов, код должен работать.
Для данных в словаре trunk_template вывод на
стандартный поток вывода должен быть таким:
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20
interface FastEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17
interface FastEthernet0/5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,21
interface FastEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30
"""

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {
    "0/1": ["add", "10", "20"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
    "0/5": ["add", "10", "21"],
    "0/7": ["only", "30"],
}
"""
for intf, vlan in access.items():
     print("interface FastEthernet" + intf)
     for command in access_template:
         if command.endswith("access vlan"):
             print(f" {command} {vlan}")
         else:
             print(f" {command}")
"""

for intf, vlan in trunk.items():
     print("interface FastEthernet" + intf)
     for command in trunk_template:
         if command.endswith("allowed vlan"):
             vlans=",".join(vlan[1:])
             if(vlan[0]=="add"):
                 print(f" {command} {vlan[0]} {vlans}")
             elif (vlan[0]=='only'):
                 print(f" {command} {vlans}")
             elif (vlan[0]=='del'):
                 print(f" {command} remove {vlans}")

         else:
             print(f" {command}")
