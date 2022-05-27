"""
Задание 4.1
Используя подготовленную строку nat, получить новую строку, в которой в имени
интерфейса вместо FastEthernet написано GigabitEthernet.
Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.
"""
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
#nat2=nat[0:40]+'GigabitEthernet'+ nat[52:]
nat2=nat.replace('FastEthernet', 'GigabitEthernet')
#print(nat)
print(nat2)

"""
Задание 4.2
Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX
в формат XXXX.XXXX.XXXX
Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.
"""
mac = "AAAA:BBBB:CCCC"
mac=mac.replace(':', '.')
print(mac)

"""
Задание 4.3
Получить из строки config такой список VLANов:
['1', '3', '10', '20', '30', '100']
Записать итоговый список в переменную result.
(именно эта переменная будет проверяться в тесте)
Полученный список result вывести на стандартный поток вывода (stdout)
с помощью print.
Тут очень важный момент, что надо получить именно список (тип данных), а не,
например, строку, которая похожа на показанный список.
"""
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.split()
result = result[-1].split(',')
print(result)

"""
Задание 4.4
Список vlans это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.
Из списка vlans нужно получить новый список уникальных номеров VLANов,
отсортированный по возрастанию номеров. Для получения итогового
списка нельзя удалять конкретные vlanы вручную.
Записать итоговый список уникальных номеров VLANов в переменную result.
(именно эта переменная будет проверяться в тесте)
Полученный список result вывести на стандартный поток вывода (stdout)
с помощью print.
"""
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = sorted(set(vlans))
print(result)

"""
Задание 4.5
Из строк command1 и command2 получить список VLANов, которые есть
и в команде command1 и в команде command2 (пересечение).
В данном случае, результатом должен быть такой список: ['1', '3', '8']
Записать итоговый список в переменную result. (именно эта переменная будет
проверяться в тесте)
Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.
"""
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command11 = command1.split()
command11 = command11[-1].split(',')

command22 = command2.split()
command22 = command22[-1].split(',')

result = sorted(set(command11) & set(command22))
print(result)

"""
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.
"""
ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
ospf_route2=ospf_route.replace("[", "").replace("]", "").replace(",", "")
print(ospf_route2.split())
ospf_route2=ospf_route2.split()
print(template.format(ospf_route2[0], ospf_route2[1], ospf_route2[3], ospf_route2[4], ospf_route2[5]))

"""
Задание 4.7
Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'
Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.
"""
mac = "AAAA:BBBB:CCCC"
mac1 = str(bin(int(mac.replace(":", ""), 16)))[2:]
print(mac1)

"""
Задание 4.8
Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный
поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)
Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001
"""
ip = "192.168.3.1"

ip2=ip.split(".")

print("{:<10} {:<10} {:<10} {:<10}".format(ip2[0], ip2[1], ip2[2], ip2[3]))
print("{:08b}   {:08b}   {:08b}   {:08b}".format(int(ip2[0]), int(ip2[1]), int(ip2[2]), int(ip2[3])))