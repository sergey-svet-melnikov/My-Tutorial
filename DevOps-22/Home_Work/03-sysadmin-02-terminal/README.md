## Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"
### 1. Какого типа команда cd? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.

Команда cd внутреннего типа (команда интерпретатора, терминала), так же как и команды cp, mv, rmdir, mkdir и подобные, которые выполняются непосредственно в данной сессии терминал и оперируют с его состоянием.
Если команду сделать внешней, то теряется смысл - буде запускать дополнительный процесс, который должен управлять другим процессом - это не логично, проще менять состояние текущего процесса (терминала) без запуска других приложений (внешних команд).
    
### 2.  Какая альтернатива без pipe команде grep <some_string> <some_file> | wc -l? man grep поможет в ответе на этот вопрос. Ознакомьтесь с документом о других подобных некорректных вариантах использования pipe.

vagrant@vagrant:~$ cat 11.sh
if [[ -d /tmp ]]
then
    echo "каталог существует"

else
    echo "такого каталога нет"

fi
vagrant@vagrant:~$ grep echo 11.sh | wc -l
2
vagrant@vagrant:~$ grep echo 11.sh -c
2

 
### 3. Какой процесс с PID 1 является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?

vagrant@vagrant:~$ pstree -g  
systemd(1)─┬─ModemManager(670)─┬─{ModemManager}(670)    
            
### 4. Как будет выглядеть команда, которая перенаправит вывод stderr ls на другую сессию терминала?


vagrant@vagrant:~$ who  
vagrant  pts/0        2022-09-03 06:39 (10.0.2.2)  
vagrant  pts/1        2022-09-03 07:04 (10.0.2.2)  
vagrant@vagrant:~$ w  
 07:06:27 up 30 min,  2 users,  load average: 0.01, 0.02, 0.08  
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT  
vagrant  pts/0    10.0.2.2         06:39    1.00s  0.21s  0.02s w  
vagrant  pts/1    10.0.2.2         07:04    1:47   0.03s  0.03s -bash  
vagrant@vagrant:~$ ls /root 2>/dev/pts/1  


vagrant@vagrant:~$ who  
vagrant  pts/0        2022-09-03 06:39 (10.0.2.2)  
vagrant  pts/1        2022-09-03 07:04 (10.0.2.2)  
vagrant@vagrant:~$ w  
 07:06:49 up 30 min,  2 users,  load average: 0.01, 0.02, 0.08  
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT  
vagrant  pts/0    10.0.2.2         06:39   23.00s  0.19s  0.19s -bash  
vagrant  pts/1    10.0.2.2         07:04    0.00s  0.05s  0.01s w  
vagrant@vagrant:~$ ls: cannot open directory '/root': Permission denied  


### 5. Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.

 vagrant@vagrant:~$ ls  
11.sh  backup  
vagrant@vagrant:~$ cat 11.sh  
if [[ -d /tmp ]]  
then  
    echo "каталог существует"  
  
else  
    echo "такого каталога нет"  
  
fi  
vagrant@vagrant:~$ cat 11.sh > 22.sh  
vagrant@vagrant:~$ cat 22.sh  
if [[ -d /tmp ]]  
then  
    echo "каталог существует"  
  
else  
    echo "такого каталога нет"  
  
fi  

---

vagrant@vagrant:~$ ls  
11.sh  22.sh  backup  
vagrant@vagrant:~$ cat 0<22.sh >33.sh    
vagrant@vagrant:~$ cat 33.sh    
if [[ -d /tmp ]]  
then  
    echo "каталог существует"  
  
else  
    echo "такого каталога нет"  
  
fi  

  
### 6. Получится ли вывести находясь в графическом режиме данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?

Да, получится, если будет достаточно прав у pts для вывода на tty

root@vagrant:/home/vagrant# tty  
/dev/pts/0  
root@vagrant:/home/vagrant# echo Message From PTS0 to TTY1 > /dev/tty1  

![TTY1](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-02-terminal/VagrantTTY1.png)  


### 7. Выполните команду bash 5>&1. К чему она приведет? Что будет, если вы выполните echo netology > /proc/$$/fd/5? Почему так происходит?

vagrant@vagrant:~$ pstree -p 647  
sshd(647)─┬─sshd(667)───sshd(778)───bash(780)───pstree(1324)    
vagrant@vagrant:~$ bash 5>&1    
vagrant@vagrant:~$ pstree -p 647    
sshd(647)─┬─sshd(667)───sshd(778)───bash(780)───bash(1399)───pstree(1348)    
vagrant@vagrant:~$ ls /dev/fd  
0  1  2  3  5  
vagrant@vagrant:~$ exit  
exit  
vagrant@vagrant:~$ pstree -p 647  
sshd(647)─┬─sshd(667)───sshd(778)───bash(780)───pstree(1360)  
vagrant@vagrant:~$ ls /dev/fd  
0  1  2  3  

* Мы находились в командном интерпретаторе bash (PID 780), выполнив "bash 5<&1" мы фактически создали форк bash (PID 1399)  
* А так же мы созадли файловый дескриптор "5" stdout'a , который соотносится c stdout'ом bash (PID1399)
* Выполнив команду echo netology > /proc/$$/fd/5 (находясь в форке bash PID1399, созданный командой "bash 5<&1"), мы передали stdout команыды echo в файловый дескриптор "5" своего же (self) процесса, а так как мы в нем же и находимся, то получили тот же результат, что если бы делали "echo netology", находясь тут же в bash PID1399

vagrant@vagrant:~$ ls /dev/fd  
0  1  2  3  5  
vagrant@vagrant:~$ ls /proc/self/fd  
0  1  2  3  5  
vagrant@vagrant:~$ pstree -p 647  
sshd(647)─┬─sshd(667)───sshd(778)───bash(780)───bash(1399)───pstree(1423)    
            
vagrant@vagrant:~$ echo netology-cool > /proc/$$/fd/5  
netology-cool  
vagrant@vagrant:~$ echo netology-cool > /dev/fd/5  
netology-cool   
vagrant@vagrant:~$ echo netology-cool  
netology-cool  

### 8. Получится ли в качестве входного потока для pipe использовать только stderr команды, не потеряв при этом отображение stdout на pty? Напоминаем: по умолчанию через pipe передается только stdout команды слева от | на stdin команды справа. Это можно сделать, поменяв стандартные потоки местами через промежуточный новый дескриптор, который вы научились создавать в предыдущем вопросе.

vagrant@vagrant:~$ ls -l /root 33>&2 2>&1 1>&33 | grep /root  
ls: cannot open directory '/root': Permission denied  

### 9.  Что выведет команда cat /proc/$$/environ? Как еще можно получить аналогичный по содержанию вывод?

* Выводит переменные окружения

env  

export  

printenv  

### 10. Используя man, опишите что доступно по адресам /proc/<PID>/cmdline, /proc/<PID>/exe

*  /proc/[PID]/cmdline - список всех параметров (аргументов) комаандной строки, с которыми был запущен процесс с номером PID]  
*  /proc/[PID]/exe - путь к запускаемому файлу процесса c с номером PID  

### 11. Узнайте, какую наиболее старшую версию набора инструкций SSE поддерживает ваш процессор с помощью /proc/cpuin

vagrant@vagrant:/proc$ cat cpuinfo | grep sse  

flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx lm constant_tsc rep_good nopl cpuid tsc_known_freq pni monitor ssse3 cx16 sse4_1 x2apic hypervisor lahf_lm pti  

### 12. При открытии нового окна терминала и vagrant ssh создается новая сессия и выделяется pty. Это можно подтвердить командой tty, которая упоминалась в лекции 3.2. Однако:

vagrant@netology1:~$ ssh localhost 'tty'
not a tty  

*

### 13. Бывает, что есть необходимость переместить запущенный процесс из одной сессии в другую. Попробуйте сделать это, воспользовавшись reptyr. Например, так можно перенести в screen процесс, который вы запустили по ошибке в обычной SSH-сессии.

*

### 14. sudo echo string > /root/new_file не даст выполнить перенаправление под обычным пользователем, так как перенаправлением занимается процесс shell'а, который запущен без sudo под вашим пользователем. Для решения данной проблемы можно использовать конструкцию echo string | sudo tee /root/new_file. Узнайте что делает команда tee и почему в отличие от sudo echo команда с sudo tee будет работать. 

*