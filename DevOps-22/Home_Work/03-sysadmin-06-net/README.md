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
Сайт автоматом нас переключил на протокол HTTPS (HTTP версии 1.1).

А вообще ошибка звучит как премещено перманентно, т.е. нам предложила поискать страницу по адресу https://stackoverflow.com/questions и закрыли соединение! 

### 2. Повторите задание 1 в браузере, используя консоль разработчика F12.

* откройте вкладку Network
* отправьте запрос http://stackoverflow.com
* найдите первый ответ HTTP сервера, откройте вкладку Headers
* укажите в ответе полученный HTTP код.

![]

* проверьте время загрузки страницы, какой запрос обрабатывался дольше всего? 
* приложите скриншот консоли браузера в ответ.

### 3.  
### 4. 
### 5. 