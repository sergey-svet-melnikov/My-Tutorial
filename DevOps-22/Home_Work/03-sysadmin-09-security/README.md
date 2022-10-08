## Домашнее задание к занятию "3.9. Элементы безопасности информационных систем"

### 1. Установите Bitwarden плагин для браузера. Зарегестрируйтесь и сохраните несколько паролей.

![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-09-security/bitwarden__PC_home.jpg)

### 2. Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.

![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-09-security/bitwarden_VIA_Google_Auth.jpg)

### 3. Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS.

vagrant@vagrant:~$ sudo apt update 

vagrant@vagrant:~$ sudo apt install apache2  

vagrant@vagrant:~$ sudo ufw app list  
Available applications:  
  Apache  
  Apache Full  
  Apache Secure  
  OpenSSH  
  
vagrant@vagrant:~$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.k

vagrant@vagrant:/$ sudo a2enmod ssl    

vagrant@vagrant:/$ sudo a2ensite default-ssl    

vagrant@vagrant:/etc/apache2/conf-available$ sudo a2enconf ssl-params  

vagrant@vagrant:/etc/apache2/sites-enabled$ sudo systemctl restart apache2  

![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-09-security/Apache_HTTPS.jpg)

### 4.  Проверьте на TLS уязвимости произвольный сайт в интернете (кроме сайтов МВД, ФСБ, МинОбр, НацБанк, РосКосмос, РосАтом, РосНАНО и любых госкомпаний, объектов КИИ, ВПК ... и тому подобное).



### 5. Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.



### 6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.



### 7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.



### 8*. Просканируйте хост scanme.nmap.org. Какие сервисы запущены?



### 9*.Установите и настройте фаервол ufw на web-сервер из задания 3. Откройте доступ снаружи только к портам 22,80,443

