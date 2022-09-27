## Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"

### 1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?  

vagrant@vagrant:~$ ifconfig  


eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500   
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255  
        inet6 fe80::a00:27ff:fea2:6bfd  prefixlen 64  scopeid 0x20<link>  
        ether 08:00:27:a2:6b:fd  txqueuelen 1000  (Ethernet)  
        RX packets 44647  bytes 46911476 (46.9 MB)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 21277  bytes 1799541 (1.7 MB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536  
        inet 127.0.0.1  netmask 255.0.0.0  
        inet6 ::1  prefixlen 128  scopeid 0x10<host>  
        loop  txqueuelen 1000  (Local Loopback)  
        RX packets 440  bytes 30601 (30.6 KB)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 440  bytes 30601 (30.6 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

PS C:\> ipconfig  

Настройка протокола IP для Windows  


Неизвестный адаптер OpenVPN Wintun:  

   Состояние среды. . . . . . . . : Среда передачи недоступна.  
   DNS-суффикс подключения . . . . . :  

Адаптер Ethernet VirtualBox Host-Only Network:  

   DNS-суффикс подключения . . . . . :  
   IPv4-адрес. . . . . . . . . . . . : 10.0.0.10  
   Маска подсети . . . . . . . . . . : 255.0.0.0  
   Основной шлюз. . . . . . . . . :  

Неизвестный адаптер OpenVPN TAP-Windows6:  

   Состояние среды. . . . . . . . : Среда передачи недоступна.  
   DNS-суффикс подключения . . . . . :  

Адаптер Ethernet Подключение по локальной сети:  

   DNS-суффикс подключения . . . . . : beeline  
   IPv4-адрес. . . . . . . . . . . . : 95.29.   
   Маска подсети . . . . . . . . . . : 255.255.  
   Основной шлюз. . . . . . . . . : 95.29.  

### 2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?  

Link Layer Discovery Protocol (LLDP) — протокол канального уровня, позволяющий сетевому оборудованию оповещать оборудование, работающее в локальной сети, о своём существовании и передавать ему свои характеристики, а также получать от него аналогичные сведения. Описание протокола приводится в стандарте IEEE 802.1AB-2009[1], формально утверждённом в сентябре 2009 года. Протокол не зависит от производителей сетевого оборудования и является заменой аналогичных, но патентованных протоколов, таких как Cisco Discovery Protocol, Extreme Discovery Protocol, Foundry Discovery Protocol, Mikrotik Neighbor Discovery Protocol и Nortel Discovery Protocol (последний также известен как SONMP).  

vagrant@vagrant:~$ lldpctl  

LLDP neighbors:   

P.S. Соседей у меня нет.  

### 3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.  

VLAN (аббр. от англ. Virtual Local Area Network) — виртуальная локальная компьютерная сеть. Представляет собой группу хостов с общим набором требований которые взаимодействуют так, как если бы они были подключены к широковещательному домену независимо от их физического местонахождения. VLAN имеет те же свойства, что и физическая локальная сеть, но позволяет конечным членам группироваться вместе, даже если они не находятся в одной физической сети. Такая реорганизация может быть сделана на основе программного обеспечения вместо физического перемещения устройств.

vagrant@vagrant:~$ ifconfig  
dummy0: flags=195<UP,BROADCAST,RUNNING,NOARP>  mtu 1500  
        inet 10.0.10.1  netmask 255.255.255.0  broadcast 0.0.0.0  
        inet6 fe80::6c22:5ff:febf:e585  prefixlen 64  scopeid 0x20<link>  
        ether 6e:22:05:bf:e5:85  txqueuelen 1000  (Ethernet)  
        RX packets 0  bytes 0 (0.0 B)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 451  bytes 96832 (96.8 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

dummy1: flags=195<UP,BROADCAST,RUNNING,NOARP>  mtu 1500  
        inet 10.1.10.1  netmask 255.255.255.0  broadcast 0.0.0.0  
        inet6 fe80::e87d:8cff:feaa:9753  prefixlen 64  scopeid 0x20<link>  
        ether ea:7d:8c:aa:97:53  txqueuelen 1000  (Ethernet)  
        RX packets 0  bytes 0 (0.0 B)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 451  bytes 96832 (96.8 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500  
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255  
        inet6 fe80::a00:27ff:fea2:6bfd  prefixlen 64  scopeid 0x20<link>  
        ether 08:00:27:a2:6b:fd  txqueuelen 1000  (Ethernet)  
        RX packets 29444  bytes 33279901 (33.2 MB)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 8924  bytes 2673093 (2.6 MB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536  
        inet 127.0.0.1  netmask 255.0.0.0  
        inet6 ::1  prefixlen 128  scopeid 0x10<host>  
        loop  txqueuelen 1000  (Local Loopback)   
        RX packets 312  bytes 20462 (20.4 KB)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 312  bytes 20462 (20.4 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

vagrant@vagrant:~$ sudo vconfig add eth0 99  

Warning: vconfig is deprecated and might be removed in the future, please migrate to ip(route2) as soon as possible!    

vagrant@vagrant:~$ sudo ifconfig eth0.99 192.168.1.100 netmask 255.255.255.0 broadcast 192.168.1.255 up   
vagrant@vagrant:~$ ifconfig  
dummy0: flags=195<UP,BROADCAST,RUNNING,NOARP>  mtu 1500  
        inet 10.0.10.1  netmask 255.255.255.0  broadcast 0.0.0.0  
        inet6 fe80::6c22:5ff:febf:e585  prefixlen 64  scopeid 0x20<link>  
        ether 6e:22:05:bf:e5:85  txqueuelen 1000  (Ethernet)  
        RX packets 0  bytes 0 (0.0 B)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 453  bytes 97270 (97.2 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

dummy1: flags=195<UP,BROADCAST,RUNNING,NOARP>  mtu 1500   
        inet 10.1.10.1  netmask 255.255.255.0  broadcast 0.0.0.0  
        inet6 fe80::e87d:8cff:feaa:9753  prefixlen 64  scopeid 0x20<link>  
        ether ea:7d:8c:aa:97:53  txqueuelen 1000  (Ethernet)  
        RX packets 0  bytes 0 (0.0 B)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 453  bytes 97270 (97.2 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500  
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255  
        inet6 fe80::a00:27ff:fea2:6bfd  prefixlen 64  scopeid 0x20<link>  
        ether 08:00:27:a2:6b:fd  txqueuelen 1000  (Ethernet)  
        RX packets 29619  bytes 33292457 (33.2 MB)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 9051  bytes 2685348 (2.6 MB)   
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

eth0.99: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500  
        inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255  
        inet6 fe80::a00:27ff:fea2:6bfd  prefixlen 64  scopeid 0x20<link>  
        ether 08:00:27:a2:6b:fd  txqueuelen 1000  (Ethernet)  
        RX packets 0  bytes 0 (0.0 B)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 7  bytes 586 (586.0 B)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536  
        inet 127.0.0.1  netmask 255.0.0.0   
        inet6 ::1  prefixlen 128  scopeid 0x10<host>   
        loop  txqueuelen 1000  (Local Loopback)  
        RX packets 312  bytes 20462 (20.4 KB)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 312  bytes 20462 (20.4 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  


vagrant@vagrant:~$ ip -br link  
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>  
eth0             UP             08:00:27:a2:6b:fd <BROADCAST,MULTICAST,UP,LOWER_UP>  
dummy0           UNKNOWN        6e:22:05:bf:e5:85 <BROADCAST,NOARP,UP,LOWER_UP>  
dummy1           UNKNOWN        ea:7d:8c:aa:97:53 <BROADCAST,NOARP,UP,LOWER_UP>  
eth0.99@eth0     UP             08:00:27:a2:6b:fd <BROADCAST,MULTICAST,UP,LOWER_UP> 

Для netplan:

>vlans:
    vlan99:
      id: 99
      link: eth0
      addresses:
        - 192.168.1.100/24

### 4.  Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.  

 Объединения сетевых интерфейсов для отказоустойчивости и увеличения пропускной способности. Называется это в Linux - BONDING интерфейсов, в windows - Teaming интерфейсов.  

Типы агрегации (объединения) интерфейсов в Linux  

mode=0 (balance-rr)  
Этот режим используется по-умолчанию, если в настройках не указано другое. balance-rr обеспечивает балансировку нагрузки и отказоустойчивость. В данном режиме пакеты отправляются "по кругу" от первого интерфейса к последнему и сначала. Если выходит из строя один из интерфейсов, пакеты отправляются на остальные оставшиеся.При подключении портов к разным коммутаторам, требует их настройки.  

mode=1 (active-backup)  
При active-backup один интерфейс работает в активном режиме, остальные в ожидающем. Если активный падает, управление передается одному из ожидающих. Не требует поддержки данной функциональности от коммутатора.  

mode=2 (balance-xor)  
Передача пакетов распределяется между объединенными интерфейсами по формуле ((MAC-адрес источника) XOR (MAC-адрес получателя)) % число интерфейсов. Один и тот же интерфейс работает с определённым получателем. Режим даёт балансировку нагрузки и отказоустойчивость.  

mode=3 (broadcast)  
Происходит передача во все объединенные интерфейсы, обеспечивая отказоустойчивость.  

mode=4 (802.3ad)  
Это динамическое объединение портов. В данном режиме можно получить значительное увеличение пропускной способности как входящего так и исходящего трафика, используя все объединенные интерфейсы. Требует поддержки режима от коммутатора, а так же (иногда) дополнительную настройку коммутатора.  

mode=5 (balance-tlb)  
Адаптивная балансировка нагрузки. При balance-tlb входящий трафик получается только активным интерфейсом, исходящий - распределяется в зависимости от текущей загрузки каждого интерфейса. Обеспечивается отказоустойчивость и распределение нагрузки исходящего трафика. Не требует специальной поддержки коммутатора.  

mode=6 (balance-alb)  
Адаптивная балансировка нагрузки (более совершенная). Обеспечивает балансировку нагрузки как исходящего (TLB, transmit load balancing), так и входящего трафика (для IPv4 через ARP). Не требует специальной поддержки коммутатором, но требует возможности изменять MAC-адрес устройства.

>bonds:
    bond0:
      dhcp4: no
      interfaces:
              - dummy0
              - dummy1
      parameters:
        mode: 802.3ad
        mii-monitor-interval: 1



### 5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.  

* Сколько IP адресов в сети с маской /29   

vagrant@vagrant:~$ ipcalc 192.168.100.0/29  
***  
***  
***  
`Hosts`/Net: `6`                     Class C, Private Internet  

* Сколько /29 подсетей можно получить из сети с маской /24  

vagrant@vagrant:~$ ipcalc 192.168.0.1 255.255.255.0 255.255.255.248  
***  
***  
***  
Subnets after transition from /24 to /29  
***  
***  
***  
`Subnets:   32  `    
`Hosts:     192`  

* Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24     

vagrant@vagrant:~$ ipcalc 10.10.10.0 255.255.255.0 255.255.255.248  
Address:   10.10.10.0           00001010.00001010.00001010. 00000000  
Netmask:   255.255.255.0 = 24   11111111.11111111.11111111. 00000000  
Wildcard:  0.0.0.255            00000000.00000000.00000000. 11111111  
=>
Network:   10.10.10.0/24        00001010.00001010.00001010. 00000000   
HostMin:   10.10.10.1           00001010.00001010.00001010. 00000001  
HostMax:   10.10.10.254         00001010.00001010.00001010. 11111110  
Broadcast: 10.10.10.255         00001010.00001010.00001010. 11111111  
Hosts/Net: 254                   Class A, Private Internet  

Subnets after transition from /24 to /29  

Netmask:   255.255.255.248 = 29 11111111.11111111.11111111.11111 000  
Wildcard:  0.0.0.7              00000000.00000000.00000000.00000 111  

 1.  
Network:   10.10.10.0/29        00001010.00001010.00001010.00000 000  
HostMin:   10.10.10.1           00001010.00001010.00001010.00000 001  
HostMax:   10.10.10.6           00001010.00001010.00001010.00000 110  
Broadcast: 10.10.10.7           00001010.00001010.00001010.00000 111  
Hosts/Net: 6                     Class A, Private Internet  

2.
Network:   10.10.10.8/29        00001010.00001010.00001010.00001 000  
HostMin:   10.10.10.9           00001010.00001010.00001010.00001 001  
HostMax:   10.10.10.14          00001010.00001010.00001010.00001 110  
Broadcast: 10.10.10.15          00001010.00001010.00001010.00001 111  
Hosts/Net: 6                     Class A, Private Internet  

 3.
Network:   10.10.10.16/29       00001010.00001010.00001010.00010 000  
HostMin:   10.10.10.17          00001010.00001010.00001010.00010 001  
HostMax:   10.10.10.22          00001010.00001010.00001010.00010 110  
Broadcast: 10.10.10.23          00001010.00001010.00001010.00010 111  
Hosts/Net: 6                     Class A, Private Internet  
***
***
***
 32.
Network:   10.10.10.248/29      00001010.00001010.00001010.11111 000  
HostMin:   10.10.10.249         00001010.00001010.00001010.11111 001  
HostMax:   10.10.10.254         00001010.00001010.00001010.11111 110  
Broadcast: 10.10.10.255         00001010.00001010.00001010.11111 111  
Hosts/Net: 6                     Class A, Private Internet  

Subnets:   32  
Hosts:     192  


### 6. Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.

vagrant@vagrant:~$ ipcalc 100.64.0.0/26  
Address:   100.64.0.0           01100100.01000000.00000000.00 000000  
Netmask:   255.255.255.192 = 26 11111111.11111111.11111111.11 000000  
Wildcard:  0.0.0.63             00000000.00000000.00000000.00 111111  
=>  
Network:   100.64.0.0/26        01100100.01000000.00000000.00 000000  
HostMin:   100.64.0.1           01100100.01000000.00000000.00 000001  
HostMax:   100.64.0.62          01100100.01000000.00000000.00 111110  
Broadcast: 100.64.0.63          01100100.01000000.00000000.00 111111  
Hosts/Net: 62                    Class A


### 7.Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?

* Linux  
  
Просмотреть:  
  
vagrant@vagrant:~$ arp -a  
vagrant@vagrant:~$ arp -e  
  
Удалить все на localhost:     
  
vagrant@vagrant:~$ arp -d localhost  
  
Удалить один 10.10.10.10:    
  
vagrant@vagrant:~$ arp -d 10.10.10.10  

* Windows  
  
Просмотреть:    
  
PS C:\> route PRINT     
PS C:\> arp -a    

Удалить все:   

PS C:\> arp -d  

Удалить один 10.10.10.10:  

PS C:\> arp -d 10.10.10.10  

