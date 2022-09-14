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
<span style="color:red">descr:          RU-CORBINA-BROADBAND-POOL2  ****</span>
<span style="color:red">****origin:         AS8402****</span>  
mnt-by:         RU-CORBINA-MNT  
created:        2011-09-16T23:52:08Z  
last-modified:  2011-09-16T23:52:08Z  
source:         RIPE # Filtered  
  
% This query was served by the RIPE Database Query Service version 1.103 (WAGYU)  
  

### 5. 