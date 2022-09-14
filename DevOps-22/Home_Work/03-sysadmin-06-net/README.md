## Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"

### 1. Работа c HTTP через телнет.

* Подключитесь утилитой телнет к сайту stackoverflow.com telnet stackoverflow.com 80
* отправьте HTTP запрос

>GET /questions HTTP/1.0  
HOST: stackoverflow.com  
[press enter]  
[press enter]  

* В ответе укажите полученный HTTP код, что он означает?

>HTTP/1.1 301 Moved Permanently  
Server: Varnish  
Retry-After: 0  
Location: https://stackoverflow.com/questions  
Content-Length: 0  
Accept-Ranges: bytes  
Date: Wed, 14 Sep 2022 16:12:37 GMT  
Via: 1.1 varnish  
Connection: close  
X-Served-By: cache-bma1632-BMA  
X-Cache: HIT  
X-Cache-Hits: 0  
X-Timer: S1663171957.297951,VS0,VE0  
Strict-Transport-Security: max-age=300  
X-DNS-Prefetch-Control: off  

Мы запросили (GET) у сайта stackoverflow.com содержимое директории (/questions) по ротоколу HTTP (HTTP версии 1.0).
Сайт автоматом нам предлгает пользоваться протоколом HTTPS (HTTP версии 1.1).

А вообще ошибка "HTTP/1.1 301 Moved Permanently" звучит как премещено перманентно, т.е. нам предложила поискать страницу по адресу https://stackoverflow.com/questions и закрыли соединение! 

### 2. Повторите задание 1 в браузере, используя консоль разработчика F12.

* откройте вкладку Network
* отправьте запрос http://stackoverflow.com
* найдите первый ответ HTTP сервера, откройте вкладку Headers
* укажите в ответе полученный HTTP код.

Первый ответ - автоматический редирект 307

![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-06-net/First_answer.jpg)

* проверьте время загрузки страницы, какой запрос обрабатывался дольше всего? 
* приложите скриншот консоли браузера в ответ.

JS-скрипт грузился 344,5 мс из 386 мс, которые были затрачены на загрузку всей страницы.

![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-06-net/Long_request.jpg)

### 3. Какой IP адрес у вас в интернете?

2ip.ru, myip: 95.29.99.176

 wget -qO- eth0.me

 wget -qO- ipinfo.io/ip

 wget -qO- ipecho.net/plain

 wget -qO- icanhazip.com

 wget -qO- ipecho.net

 wget -qO- ident.me

 wget -qO- myip.gelma.net

### 4.  Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois

vagrant@vagrant:~$ whois 95.29.99.176  
% This is the RIPE Database query service.  
% The objects are in RPSL format.  
%  
% The RIPE Database is subject to Terms and Conditions.  
% See http://www.ripe.net/db/support/db-terms-conditions.pdf  
  
% Note: this output has been filtered.  
%       To receive output for a database update, use the "-B" flag.  
  
% Information related to '95.24.0.0 - 95.30.255.255'  
  
% Abuse contact for '95.24.0.0 - 95.30.255.255' is 'abuse-b2b@beeline.ru'  
   
inetnum:        95.24.0.0 - 95.30.255.255  
netname:        <span style="color:red">****BEELINE-BROADBAND  ****</span>
descr:          Dynamic IP Pool for broadband customers  
country:        RU  
admin-c:        CORB1-RIPE    
tech-c:         CORB1-RIPE  
status:         ASSIGNED PA  
mnt-by:         RU-CORBINA-MNT  
created:        2010-05-12T10:14:50Z  
last-modified:  2011-10-24T07:14:07Z  
source:         RIPE  
  
role:           CORBINA TELECOM Network Operations    
address:        <span style="color:red">****PAO Vimpelcom - CORBINA TELECOM/Internet Network Operations****</span>    
address:        111250 Russia Moscow Krasnokazarmennaya, 12  
phone:          +7 495 755 5648  
fax-no:         +7 495 787 1990  
remarks:        -----------------------------------------------------------  
remarks:        Feel free to contact Corbina Telecom NOC to  
remarks:        resolve networking problems related to Corbina  
remarks:        -----------------------------------------------------------  
remarks:        User support, general questions: support@corbina.net  
remarks:        Routing, peering, security: corbina-noc@beeline.ru  
remarks:        Report spam and abuse: abuse@beeline.ru   
remarks:        Mail and news: postmaster@corbina.net  
remarks:        DNS: hostmaster@corbina.net  
remarks:        Engineering Support ES@beeline.ru  
remarks:        -----------------------------------------------------------  
admin-c:        SVNT1-RIPE  
tech-c:         SVNT2-RIPE  
nic-hdl:        CORB1-RIPE  
mnt-by:         RU-CORBINA-MNT  
abuse-mailbox:  abuse-b2b@beeline.ru  
created:        1970-01-01T00:00:00Z  
last-modified:  2022-05-11T13:21:44Z  
source:         RIPE # Filtered  
  
% Information related to '95.29.99.0/24AS8402'  

route:          95.29.99.0/24  
<span style="color:red">****descr:          RU-CORBINA-BROADBAND-POOL2****</span>   
<span style="color:red">****origin:         AS8402****</span>    
mnt-by:         RU-CORBINA-MNT   
created:        2011-09-16T23:52:08Z  
last-modified:  2011-09-16T23:52:08Z  
source:         RIPE # Filtered  
  
% This query was served by the RIPE Database Query Service version 1.103 (WAGYU)  
  

### 5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute

Мой вагрант не показывает сведения при трассировке дальше самого себя.

Но команда, которой можно посмотреть и сети и AS можно смотреть traceroute -An 8.8.8.8 

### 6. Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?

                                             My traceroute  [v0.93]
vagrant (10.0.2.15)                                                                            2022-09-14T19:18:55+0000
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                                                               Packets               Pings
 Host                                                                        Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. _gateway                                                                  0.0%    50    0.2   0.3   0.1   0.5   0.1
 2. bras252.perm.corbina.net                                                  0.0%    50    4.9   6.5   1.9  11.6   3.0
 3. bras252.perm.corbina.net                                                  0.0%    50    6.7   6.6   1.6  11.8   2.9
 4. 10.2.247.244                                                              0.0%    50    1.3   2.7   1.3  40.2   5.5
 5. 79.104.24.193                                                             0.0%    50    2.0   2.2   1.5   3.7   0.3
 6. pe03.KK12.Moscow.gldn.net                                                 0.0%    50   23.0  23.3  22.8  24.5   0.3
 7. 72.14.213.116                                                             0.0%    49   31.3  30.8  30.3  33.6   0.7
 8. 108.170.250.34                                                            0.0%    49   32.6  31.7  31.2  33.9   0.5
 9. 142.251.49.24                                                             0.0%    49   35.9  36.3  35.8  37.5   0.4
10. 172.253.65.82                                                             0.0%    49   36.2  38.8  35.0  83.9   9.2
11. 142.250.233.27                                                            0.0%    49   36.1  36.3  35.7  39.2   0.5
12. (waiting for reply)
13. (waiting for reply)
14. (waiting for reply)
15. (waiting for reply)
16. (waiting for reply)
17. (waiting for reply)
18. (waiting for reply)
19. (waiting for reply)
20. (waiting for reply)
21. dns.google                                                                0.0%    49   42.8  42.8  42.5  45.8   0.6

Наиудший: 
10. 172.253.65.82                                                             0.0%    49   36.2  38.8  35.0  83.9   9.2

### 7.Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой dig

vagrant@vagrant:~$ dig dns.google  

; <<>> DiG 9.16.1-Ubuntu <<>> dns.google  
;; global options: +cmd  
;; Got answer:  
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56170  
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1  
  
;; OPT PSEUDOSECTION:  
; EDNS: version: 0, flags:; udp: 65494  
;; QUESTION SECTION:  
;dns.google.                    IN      A  
  
;; ANSWER SECTION:  
dns.google.             742     IN      A       8.8.8.8  
dns.google.             742     IN      A       8.8.4.4  
  
;; Query time: 32 msec  
;; SERVER: 127.0.0.53#53(127.0.0.53)  
;; WHEN: Wed Sep 14 19:21:50 UTC 2022   
;; MSG SIZE  rcvd: 71  

Серверы, отвечающие за dns.google:  

dns.google.             742     IN      A       8.8.8.8  
dns.google.             742     IN      A       8.8.4.4  

### 8.