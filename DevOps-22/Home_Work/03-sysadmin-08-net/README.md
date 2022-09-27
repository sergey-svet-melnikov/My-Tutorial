## Домашнее задание к занятию "3.8. Компьютерные сети, лекция 3"

### 1. Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP

>telnet route-views.routeviews.org
Username: rviews
show ip route x.x.x.x/32
show bgp x.x.x.x/32
> 
> 
vagrant@vagrant:~$ telnet route-views.routeviews.org  
Trying 128.223.51.103...  
Connected to route-views.routeviews.org.  
Escape character is '^]'.  
C  
**********************************************************************  

                    RouteViews BGP Route Viewer  
                    route-views.routeviews.org  

 route views data is archived on http://archive.routeviews.org  

 This hardware is part of a grant by the NSF.  
 Please contact help@routeviews.org if you have questions, or  
 if you wish to contribute your view.  

 This router has views of full routing tables from several ASes.  
 The list of peers is located at http://www.routeviews.org/peers  
 in route-views.oregon-ix.net.txt  

 NOTE: The hardware was upgraded in August 2014.  If you are seeing  
 the error message, "no default Kerberos realm", you may want to  
 in Mac OS X add "default unset autologin" to your ~/.telnetrc  
  
 To login, use the username "rviews".  
  
 **********************************************************************  

User Access Verification  

Username: rviews    
route-views>  

route-views>show ip route 93.80.43.168      
Routing entry for 93.80.32.0/20    
  Known via "bgp 6447", distance 20, metric 0  
  Tag 6939, type external  
  Last update from 64.71.137.241 1w0d ago  
  Routing Descriptor Blocks:  
  * 64.71.137.241, from 64.71.137.241, 1w0d ago  
      Route metric is 0, traffic share count is 1  
      AS Hops 3  
      Route tag 6939  
      MPLS label: none  
route-views>  

route-views>show bgp 93.80.43.168  
BGP routing table entry for 93.80.32.0/20, version 2429445139  
Paths: (23 available, best #15, table default)  
  Not advertised to any peer  
  Refresh Epoch 1  
  3333 1103 3216 8402  
    193.0.0.56 from 193.0.0.56 (193.0.0.56)  
      Origin incomplete, localpref 100, valid, external  
      Community: 3216:2001 3216:4459 8402:1203 65000:52254 65000:65049  
      path 7FE11BF37170 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  4901 6079 3257 1273 3216 8402  
    162.250.137.254 from 162.250.137.254 (162.250.137.254)  
      Origin incomplete, localpref 100, valid, external  
      Community: 65000:10100 65000:10300 65000:10400  
      path 7FE18920B4C8 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  3267 3216 8402  
    194.85.40.15 from 194.85.40.15 (185.141.126.1)  
      Origin incomplete, metric 0, localpref 100, valid, external  
      path 7FE18A2A9688 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  8283 3216 8402  
    94.142.247.3 from 94.142.247.3 (94.142.247.3)  
      Origin incomplete, metric 0, localpref 100, valid, external  
      Community: 3216:2001 3216:4459 8283:1 8283:101 8402:1203 65000:52254 65000:65049  
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x18  
 --More--  

### 2. Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.  

vagrant@vagrant:~$ sudo ip link add dummy0 type dummy    
vagrant@vagrant:~$ sudo ip link add dummy1 type dummy    

vagrant@vagrant:~$  sudo ip link set dummy0 up  
vagrant@vagrant:~$  sudo ip link set dummy1 up  

vagrant@vagrant:~$ sudo ip addr add 10.0.10.1/24 dev dummy0  
vagrant@vagrant:~$ sudo ip addr add 10.1.10.1/24 dev dummy1  
vagrant@vagrant:~$ ifconfig  
dummy0: flags=195<UP,BROADCAST,RUNNING,NOARP>  mtu 1500  
        inet 10.0.10.1  netmask 255.255.255.0  broadcast 0.0.0.0  
        inet6 fe80::dc50:b5ff:fef3:78f6  prefixlen 64  scopeid 0x20<link>  
        ether de:50:b5:f3:78:f6  txqueuelen 1000  (Ethernet)  
        RX packets 0  bytes 0 (0.0 B)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 8  bytes 1007 (1.0 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

dummy1: flags=195<UP,BROADCAST,RUNNING,NOARP>  mtu 1500  
        inet 10.1.10.1  netmask 255.255.255.0  broadcast 0.0.0.0  
        inet6 fe80::d4b7:35ff:fe1f:c465  prefixlen 64  scopeid 0x20<link>  
        ether d6:b7:35:1f:c4:65  txqueuelen 1000  (Ethernet)  
        RX packets 0  bytes 0 (0.0 B)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 8  bytes 1007 (1.0 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500  
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255  
        inet6 fe80::a00:27ff:fea2:6bfd  prefixlen 64  scopeid 0x20<link>  
        ether 08:00:27:a2:6b:fd  txqueuelen 1000  (Ethernet)  
        RX packets 56569  bytes 60286188 (60.2 MB)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 28812  bytes 2445836 (2.4 MB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536  
        inet 127.0.0.1  netmask 255.0.0.0  
        inet6 ::1  prefixlen 128  scopeid 0x10<host>  
        loop  txqueuelen 1000  (Local Loopback)  
        RX packets 558  bytes 41677 (41.6 KB)  
        RX errors 0  dropped 0  overruns 0  frame 0  
        TX packets 558  bytes 41677 (41.6 KB)  
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0  

vagrant@vagrant:~$ ip route
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100
8.8.3.0/24 via 10.0.10.1 dev dummy0
8.8.4.0/24 via 10.1.10.1 dev dummy1
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15
10.0.2.2 dev eth0 proto dhcp scope link src 10.0.2.15 metric 100
10.0.10.0/24 dev dummy0 proto kernel scope link src 10.0.10.1
10.1.10.0/24 dev dummy1 proto kernel scope link src 10.1.10.1

### 3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.  

vagrant@vagrant:~$ sudo netstat -talpn  
Active Internet connections (servers and established)  
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name  
tcp        0      0 127.0.0.1:8125          0.0.0.0:*               LISTEN      607/netdata  
tcp        0      0 0.0.0.0:19999           0.0.0.0:*               LISTEN      607/netdata  
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      583/systemd-resolve  
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      659/sshd: /usr/sbin  
tcp        0      0 10.0.2.15:22            10.0.2.2:50827          ESTABLISHED 1170/sshd: vagrant  
tcp        0      0 10.0.2.15:19999         10.0.2.2:65336          ESTABLISHED 607/netdata  
tcp6       0      0 :::9100                 :::*                    LISTEN      1415/node_exporter  
tcp6       0      0 :::22                   :::*                    LISTEN      659/sshd: /usr/sbin

vagrant@vagrant:~$ sudo ss -tap  
State  Recv-Q Send-Q   Local Address:Port     Peer Address:Port  Process  
LISTEN 0      4096         127.0.0.1:8125          0.0.0.0:*      users:(("netdata",pid=607,fd=20))  
LISTEN 0      4096           0.0.0.0:19999         0.0.0.0:*      users:(("netdata",pid=607,fd=4))  
LISTEN 0      4096     127.0.0.53%lo:domain        0.0.0.0:*      users:(("systemd-resolve",pid=583,fd=13))  
LISTEN 0      128            0.0.0.0:ssh           0.0.0.0:*      users:(("sshd",pid=659,fd=3))  
ESTAB  0      0            10.0.2.15:ssh          10.0.2.2:50827  users:(("sshd",pid=1195,fd=4),("sshd",pid=1170,fd=4))  
ESTAB  0      0            10.0.2.15:19999        10.0.2.2:65336  users:(("netdata",pid=607,fd=26))  
LISTEN 0      4096                 *:9100                *:*      users:(("node_exporter",pid=1415,fd=3))  
LISTEN 0      128               [::]:ssh              [::]:*      users:(("sshd",pid=659,fd=4))    

vagrant@vagrant:~$ sudo ss -tapn  
State  Recv-Q  Send-Q   Local Address:Port    Peer Address:Port  Process  
LISTEN 0       4096         127.0.0.1:8125         0.0.0.0:*      users:(("netdata",pid=607,fd=20))  
LISTEN 0       4096           0.0.0.0:19999        0.0.0.0:*      users:(("netdata",pid=607,fd=4))  
LISTEN 0       4096     127.0.0.53%lo:53           0.0.0.0:*      users:(("systemd-resolve",pid=583,fd=13))  
LISTEN 0       128            0.0.0.0:22           0.0.0.0:*      users:(("sshd",pid=659,fd=3))  
ESTAB  0       0            10.0.2.15:22          10.0.2.2:50827  users:(("sshd",pid=1195,fd=4),("sshd",pid=1170,fd=4))  
ESTAB  0       0            10.0.2.15:19999       10.0.2.2:65336  users:(("netdata",pid=607,fd=26))  
LISTEN 0       4096                 *:9100               *:*      users:(("node_exporter",pid=1415,fd=3))  
LISTEN 0       128               [::]:22              [::]:*      users:(("sshd",pid=659,fd=4))  

vagrant@vagrant:~$ sudo lsof -i -P | grep TCP  
systemd-r  583 systemd-resolve   13u  IPv4  20469      0t0  TCP localhost:53 (LISTEN)  
netdata    607         netdata    4u  IPv4  25892      0t0  TCP *:19999 (LISTEN)  
netdata    607         netdata   20u  IPv4  27265      0t0  TCP localhost:8125 (LISTEN)  
netdata    607         netdata   26u  IPv4  41025      0t0  TCP vagrant:19999->_gateway:65336 (ESTABLISHED)  
sshd       659            root    3u  IPv4  23854      0t0  TCP *:22 (LISTEN)  
sshd       659            root    4u  IPv6  23906      0t0  TCP *:22 (LISTEN)  
sshd      1170            root    4u  IPv4  27692      0t0  TCP vagrant:22->_gateway:50827 (ESTABLISHED)  
sshd      1195         vagrant    4u  IPv4  27692      0t0  TCP vagrant:22->_gateway:50827 (ESTABLISHED)  
node_expo 1415            root    3u  IPv6  29304      0t0  TCP *:9100 (LISTEN)  
 
19999 - HTTP (netdata web monitoring)
22 - SSH
53 - DNS 
9100 - JetDirect (HP Print Services - из wiki)

### 4.  Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

vagrant@vagrant:~$ sudo netstat -ualpn
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
udp        0      0 127.0.0.1:8125          0.0.0.0:*                           607/netdata
udp        0      0 127.0.0.53:53           0.0.0.0:*                           583/systemd-resolve
udp        0      0 10.0.2.15:68            0.0.0.0:*                           581/systemd-network

vagrant@vagrant:~$ sudo ss -ulp
State    Recv-Q   Send-Q      Local Address:Port       Peer Address:Port   Process
UNCONN   0        0               127.0.0.1:8125            0.0.0.0:*       users:(("netdata",pid=607,fd=19))
UNCONN   0        0           127.0.0.53%lo:domain          0.0.0.0:*       users:(("systemd-resolve",pid=583,fd=12))
UNCONN   0        0          10.0.2.15%eth0:bootpc          0.0.0.0:*       users:(("systemd-network",pid=581,fd=19))

vagrant@vagrant:~$ sudo ss -ulpn
State    Recv-Q   Send-Q      Local Address:Port       Peer Address:Port   Process
UNCONN   0        0               127.0.0.1:8125            0.0.0.0:*       users:(("netdata",pid=607,fd=19))
UNCONN   0        0           127.0.0.53%lo:53              0.0.0.0:*       users:(("systemd-resolve",pid=583,fd=12))
UNCONN   0        0          10.0.2.15%eth0:68              0.0.0.0:*       users:(("systemd-network",pid=581,fd=19))

vagrant@vagrant:~$ sudo lsof -i -P | grep UDP
systemd-n  581 systemd-network   19u  IPv4  20444      0t0  UDP vagrant:68
systemd-r  583 systemd-resolve   12u  IPv4  20468      0t0  UDP localhost:53
netdata    607         netdata   19u  IPv4  27264      0t0  UDP localhost:8125

53 - DNS
68 - Bootstrap Protocol Client
8125 - приложение netdata web monitoring

### 5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.

