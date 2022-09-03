## Домашнее задание к занятию "3.3. Операционные системы, лекция 1"

### 1. Какой системный вызов делает команда cd? В прошлом ДЗ мы выяснили, что cd не является самостоятельной программой, это shell builtin, поэтому запустить strace непосредственно на cd не получится. Тем не менее, вы можете запустить strace на /bin/bash -c 'cd /tmp'. В этом случае вы увидите полный список системных вызовов, которые делает сам bash при старте. Вам нужно найти тот единственный, который относится именно к cd. Обратите внимание, что strace выдаёт результат своей работы в поток stderr, а не в stdout.

chdir("/tmp")

### 2.Попробуйте использовать команду file на объекты разных типов на файловой системе. Например:

file - оперделяет тип файла  

vagrant@vagrant:/$ file /dev/fd  
/dev/fd: symbolic link to /proc/self/fd  
vagrant@vagrant:/$ file ~/11.sh  
/home/vagrant/11.sh: UTF-8 Unicode text  
vagrant@vagrant:/$ file /sbin  
/sbin: symbolic link to usr/sbin  
vagrant@vagrant:/$ file ~/.viminfo  
/home/vagrant/.viminfo: ASCII text  

vagrant@vagrant:~$ strace file ~/11.sh  

openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3  

### 3.Предположим, приложение пишет лог в текстовый файл. Этот файл оказался удален (deleted в lsof), однако возможности сигналом сказать приложению переоткрыть файлы или просто перезапустить приложение – нет. Так как приложение продолжает писать в удаленный файл, место на диске постепенно заканчивается. Основываясь на знаниях о перенаправлении потоков предложите способ обнуления открытого удаленного файла (чтобы освободить место на файловой системе).



1. Найти в ps процесс работающий (пишущий) в файла
2. Посмотреть lsof информацию о процессе, увидеть каким дескриптором пользуется процесс пишуший в файл
3. Направить в дескриптор любое значение (или пустоту) через ">" , а не через ">>"

* Видим файл лога log_file:   
vagrant@vagrant:~$ cat log_file   
Log_DAta   
Log_DAta   
Log_DAta  
Log_DAta  
Log_DAta  
Log_DAta  
Log_DAta  
Log_DAta  
Log_DAta  
Log_DAta  

* Открываем файл на редактирование: 
vagrant@vagrant:~$ vi log_file  

* В другой сессии ищем процесс нашего vi или файла log_file (лучше по имени лога log_file) и Видим PID 5969 процесса, пишушщего в файл log_file

vagrant@vagrant:~$ ps -aux | grep log_file  
vagrant     5969  0.7  0.9  21840  9740 pts/1    S+   11:36   0:00 vi log_file  
vagrant     5971  0.0  0.0   6432   720 pts/0    S+   11:36   0:00 grep --color=auto log_file  
vagrant@vagrant:~$ ps -aux | grep vi
root         594  0.0  0.9 239288  9260 ?        Ssl  08:24   0:00 /usr/lib/accountsservice/accounts-daemon  
root        1251  0.0  0.2 292816  2984 ?        Sl   08:25   0:03 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-service.sh  
vagrant     5969  0.2  0.9  21840  9740 pts/1    S+   11:36   0:00 vi log_file  
vagrant     5973  0.0  0.0   6432   660 pts/0    S+   11:37   0:00 grep --color=auto vi  

* Удалим log_file

vagrant@vagrant:~$ rm log_file  
vagrant@vagrant:~$ ls  
11.sh  backup  log_file2  

* Ищем lsof номер дискриптора процесса, пишущего до сих пор в удаленный файл

vagrant@vagrant:~$ lsof -p 5969 | grep log_file  
vi      5969 vagrant    4u   REG  253,0    12288 1311799 /home/vagrant/.log_file.swp  

* Затем отправляем в поток файла пустоту

vagrant@vagrant:~$ echo /dev/nul > /proc/5969/fd/4  



### 4.Занимают ли зомби-процессы какие-то ресурсы в ОС (CPU, RAM, IO)?

ВИКИПЕДИЯ:
Процесс при завершении (как нормальном, так и в результате не обрабатываемого сигнала) освобождает все свои ресурсы и становится «зомби» — пустой записью в таблице процессов, хранящей статус завершения, предназначенный для чтения родительским процессом.

Зомби-процесс существует до тех пор, пока родительский процесс не прочитает его статус с помощью системного вызова wait(), в результате чего запись в таблице процессов будет освобождена.

При завершении процесса система уведомляет родительский процесс о завершении дочернего с помощью сигнала SIGCHLD, таким образом может быть удобно (но не обязательно) осуществлять вызов wait() в обработчике данного сигнала.

### 5.В iovisor BCC есть утилита opensnoop: 

>root@vagrant:~# dpkg -L bpfcc-tools | grep sbin/opensnoop  
/usr/sbin/opensnoop-bpfcc  
На какие файлы вы увидели вызовы группы open за первую секунду работы утилиты? Воспользуйтесь пакетом bpfcc-tools для Ubuntu 20.04. Дополнительные сведения по установке.  

1. Ставим пакет bpfcc-tools vagrant@vagrant:~$ sudo apt install bpfcc-tools  

2. Видимо при запуске sudo dpkg -L bpfcc-tools | grep sbin/opensnoop:  

vagrant@vagrant:~$ dpkg -L bpfcc-tools | grep sbin/opensnoop  
/usr/sbin/opensnoop-bpfcc  

3. Запускаем утилиту sudo /usr/sbin/opensnoop-bpfcc  

vagrant@vagrant:~$ sudo /usr/sbin/opensnoop-bpfcc  
PID    COMM               FD ERR PATH  
1251   vminfo              4   0 /var/run/utmp  
595    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services  
595    dbus-daemon        20   0 /usr/share/dbus-1/system-services  
595    dbus-daemon        -1   2 /lib/dbus-1/system-services  
595    dbus-daemon        20   0 /var/lib/snapd/dbus-1/system-services/  
356    systemd-udevd      14   0 /sys/fs/cgroup/unified/system.slice/systemd-udevd.service/cgroup.procs  
356    systemd-udevd      14   0 /sys/fs/cgroup/unified/system.slice/systemd-udevd.service/cgroup.threads  

### 6.Какой системный вызов использует uname -a? Приведите цитату из man по этому системному вызову, где описывается альтернативное местоположение в /proc, где можно узнать версию ядра и релиз ОС.

Делаем man uname - не видим там информации, однако видим второй раздел man по uname - uname(2).  
Ищем man 2 uname , внутри ищем по //proc/ и находим ответ:  

Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.  

### 7.Чем отличается последовательность команд через ; и через && в bash? Например:

>root@netology1:~# test -d /tmp/some_dir; echo Hi  
Hi  
root@netology1:~# test -d /tmp/some_dir && echo Hi  
root@netology1:~#  
Есть ли смысл использовать в bash &&, если применить set -e?  


### 8.Из каких опций состоит режим bash set -euxo pipefail и почему его хорошо было бы использовать в сценариях?

### 9.Используя -o stat для ps, определите, какой наиболее часто встречающийся статус у процессов в системе. В man ps ознакомьтесь (/PROCESS STATE CODES) что значат дополнительные к основной заглавной буквы статуса процессов. Его можно не учитывать при расчете (считать S, Ss или Ssl равнозначными).



