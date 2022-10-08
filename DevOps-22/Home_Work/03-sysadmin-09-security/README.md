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

vagrant@vagrant:~/testssl.sh$ ./testssl.sh -U --sneaky localhost  

###########################################################  
    testssl.sh       3.2rc2 from https://testssl.sh/dev/  
    (0ed2bf0 2022-10-07 16:48:06)  
  
      This program is free software. Distribution and  
             modification under GPLv2 permitted.   
      USAGE w/o ANY WARRANTY. USE IT AT YOUR OWN RISK!  
  
       Please file bugs @ https://testssl.sh/bugs/  

###########################################################  

 Using "OpenSSL 1.0.2-bad (1.0.2k-dev)" [~183 ciphers]  
 on vagrant:./bin/openssl.Linux.x86_64  
 (built: "Sep  1 14:03:44 2022", platform: "linux-x86_64")  
 

 Start 2022-10-08 14:49:25        -->> 127.0.0.1:443 (localhost) <<--  

 A record via:           /etc/hosts  
 rDNS (127.0.0.1):       --  
 Service detected:       HTTP  


 Testing vulnerabilities  
  
 Heartbleed (CVE-2014-0160)                not vulnerable (OK), no heartbeat extension  
 CCS (CVE-2014-0224)                       not vulnerable (OK)  
 Ticketbleed (CVE-2016-9244), experiment.  not vulnerable (OK), no session ticket extension  
 ROBOT                                     Server does not support any cipher suites that use RSA key transport  
 Secure Renegotiation (RFC 5746)           supported (OK)  
 Secure Client-Initiated Renegotiation     not vulnerable (OK)  
 CRIME, TLS (CVE-2012-4929)                not vulnerable (OK)  
 BREACH (CVE-2013-3587)                    potentially NOT ok, "gzip" HTTP compression detected. - only supplied "/" tested  
                                           Can be ignored for static pages or if no secrets in the page  
 POODLE, SSL (CVE-2014-3566)               not vulnerable (OK)  
 TLS_FALLBACK_SCSV (RFC 7507)              No fallback possible (OK), no protocol below TLS 1.2 offered  
 SWEET32 (CVE-2016-2183, CVE-2016-6329)    not vulnerable (OK)   
 FREAK (CVE-2015-0204)                     not vulnerable (OK)  
 DROWN (CVE-2016-0800, CVE-2016-0703)      not vulnerable on this host and port (OK)  
                                           make sure you don't use this certificate elsewhere with SSLv2 enabled services, see  
                                           https://search.censys.io/search?resource=hosts&virtual_hosts=INCLUDE&q=60C4194A352EC7067712B4FE10AFD077629A15E05BB44782769D9C8546662E0C   
 LOGJAM (CVE-2015-4000), experimental      common prime with 2048 bits detected: RFC3526/Oakley Group 14 (2048 bits),  
                                           but no DH EXPORT ciphers  
 BEAST (CVE-2011-3389)                     not vulnerable (OK), no SSL3 or TLS1  
 LUCKY13 (CVE-2013-0169), experimental     potentially VULNERABLE, uses cipher block chaining (CBC) ciphers with TLS. Check patches  
 Winshock (CVE-2014-6321), experimental    not vulnerable (OK)  
 RC4 (CVE-2013-2566, CVE-2015-2808)        no RC4 ciphers detected (OK)  


 Done 2022-10-08 14:50:13 [  64s] -->> 127.0.0.1:443 (localhost) <<--  

### 5. Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.

PS C:\Vagrant> ssh-keygen  
Generating public/private rsa key pair.  
Enter file in which to save the key (C:\Users\sam/.ssh/id_rsa): vagrant  
Enter passphrase (empty for no passphrase):  
Enter same passphrase again:  
Your identification has been saved in vagrant.  
Your public key has been saved in vagrant.pub.  
The key fingerprint is:  
SHA256:3PIYFyLifPfjjjsoh1v5XgLfZj2UJlJm2wAosDmu9Ss sam@samhome  
The key's randomart image is:  
+---[RSA 3072]----+  
|  ..   ..        |   
|   o. .  .       |   
|  + ... . *      |     
| . + . o * = .   |  
|  o o o S = =    |  
| o . . = X =     |  
|.   ..o.+ O o    |  
|  E ooo..B . .   |  
|   .o+ .=+o      |  
+----[SHA256]-----+  
  
C:\Vagrant>scp.exe -P 2222 vagrant.pub vagrant@127.0.0.1:~/.ssh/authorized_keys  
vagrant@127.0.0.1's password:  
vagrant.pub                                   100%  566   283.0KB/s   00:00  

PS C:\Vagrant> ssh -p 2222 -i vagrant vagrant@127.0.0.1  
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-110-generic x86_64)  
  
 * Documentation:  https://help.ubuntu.com  
 * Management:     https://landscape.canonical.com  
 * Support:        https://ubuntu.com/advantage  

  System information as of Sat 08 Oct 2022 03:07:53 PM UTC  

  System load:  0.04               Processes:             122  
  Usage of /:   12.2% of 30.63GB   Users logged in:       1  
  Memory usage: 21%                IPv4 address for eth0: 10.0.2.15  
  Swap usage:   0%  


This system is built by the Bento project by Chef Software  
More information can be found at https://github.com/chef/bento  
Last login: Sat Oct  8 14:08:12 2022 from 10.0.2.2  
vagrant@vagrant:~$  

### 6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.

vagrant.* => => vag.*  

PS C:\users\sam\.ssh> ls  

  Каталог: C:\users\sam\.ssh  

Mode                 LastWriteTime         Length Name  
----                 -------------         ------ ----  
-a----        08.10.2022     20:31             86 config  
-a----        08.10.2022     20:05            271 known_hosts  
-a----        08.10.2022     20:29           2602 vag  
-a----        08.10.2022     20:29            566 vag.pub  

PS C:\users\sam\.ssh> type config  
Host vag  
  User vagrant  
  HostName 127.0.0.1  
  Port 2222  
  IdentityFile ~/.ssh/vag    

PS C:\users\sam\.ssh> ssh vag  
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-110-generic x86_64)  

 * Documentation:  https://help.ubuntu.com  
 * Management:     https://landscape.canonical.com  
 * Support:        https://ubuntu.com/advantage  
 
  System information as of Sat 08 Oct 2022 03:32:11 PM UTC  

  System load:  0.12               Processes:             123  
  Usage of /:   12.2% of 30.63GB   Users logged in:       1  
  Memory usage: 21%                IPv4 address for eth0: 10.0.2.15  
  Swap usage:   0%  


This system is built by the Bento project by Chef Software  
More information can be found at https://github.com/chef/bento  
Last login: Sat Oct  8 15:30:25 2022 from 10.0.2.2  
 
### 7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.

![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-09-security/tcpdump.jpg)

### 8*. Просканируйте хост scanme.nmap.org. Какие сервисы запущены?

vagrant@vagrant:~$ nmap localhost  
Starting Nmap 7.80 ( https://nmap.org ) at 2022-10-08 16:23 UTC  
Nmap scan report for localhost (127.0.0.1)  
Host is up (0.00062s latency).  
Not shown: 997 closed ports  
PORT    STATE SERVICE  
22/tcp  open  ssh  
80/tcp  open  http  
443/tcp open  https  

vagrant@vagrant:~$ nmap scanme.nmap.org  
Starting Nmap 7.80 ( https://nmap.org ) at 2022-10-08 16:23 UTC  
Nmap scan report for scanme.nmap.org (45.33.32.156)  
Host is up (0.21s latency).  
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f  
Not shown: 996 filtered ports  
PORT      STATE SERVICE   
22/tcp    open  ssh  
80/tcp    open  http  
9929/tcp  open  nping-echo
31337/tcp open  Elite   


Все открытые порты описаны выше... что тут добавить! 