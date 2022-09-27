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



### 3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.

### 4.  Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

### 5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.

