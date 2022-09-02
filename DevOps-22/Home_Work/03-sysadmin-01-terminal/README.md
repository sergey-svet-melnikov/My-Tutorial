## Домашнее задание к занятию "3.1. Работа в терминале, лекция 1"
### 1. Установите средство виртуализации Oracle VirtualBox.

* Версия 6.1.34 r150636 (Qt5.6.2) Windows
    
### 2. Установите средство автоматизации Hashicorp Vagrant.

* Vagrant 2.3.0

### 3. В вашем основном окружении подготовьте удобный для дальнейшей работы терминал.

* Windows Terminal в Windows

### 4. С помощью базового файла конфигурации запустите Ubuntu 20.04 в VirtualBox посредством Vagrant:

* Ubuntu - 20.04 развернута 

### 5. Ознакомьтесь с графическим интерфейсом VirtualBox, посмотрите как выглядит виртуальная машина, которую создал для вас Vagrant, какие аппаратные ресурсы ей выделены. Какие ресурсы выделены по-умолчанию?

* ОЗУ 1024 МБ
* CPU 2 Core от системного с загрузкой до 100% на каждое ядро
* Видео 4 МБ
* HDD vmdk динамический на 64 ГБ
* Сетевая Intel PRO / 1000 MT Desktop (8254OEM) в режиме NAT
* Назначена общая папка, совпадающая с папкой vagrant

### 6. Ознакомьтесь с возможностями конфигурации VirtualBox через Vagrantfile: документация. Как добавить оперативной памяти или ресурсов процессора виртуальной машине?

* https://www.vagrantup.com/docs/providers/virtualbox/configuration

### 7. Команда vagrant ssh из директории, в которой содержится Vagrantfile, позволит вам оказаться внутри виртуальной машины без каких-либо дополнительных настроек. Попрактикуйтесь в выполнении обсуждаемых команд в терминале Ubuntu.

* vagrant@vagrant:~$ uname -a 
Linux vagrant 5.4.0-110-generic #124-Ubuntu SMP Thu Apr 14 19:46:19 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

### 8. Ознакомиться с разделами man bash, почитать о настройках самого bash:

> Какой переменной можно задать длину журнала history, и на какой строчке manual это описывается?
 
* HISTSIZE, по умолчанию этоn файл ~/.bash_history (строка мануала по bash 843, если я корректно выставил позицию )

> что делает директива ignoreboth в bash?

* HISTCONTROL
              A  colon-separated  list of values controlling how commands are saved on the history list.  If the list
              of values includes ignorespace, lines which begin with a space character are not saved in  the  history
              list.  A value of ignoredups causes lines matching the previous history entry to not be saved.  A value
              of ignoreboth is shorthand for ignorespace and ignoredups.  A value of erasedups  causes  all  previous
              lines  matching  the  current  line to be removed from the history list before that line is saved.  Any
              value not in the above list is ignored.  If HISTCONTROL is unset, or does not include  a  valid  value,
              all  lines  read by the shell parser are saved on the history list, subject to the value of HISTIGNORE.
              The second and subsequent lines of a multi-line compound command are not tested, and are added  to  the
              history regardless of the value of HISTCONTROL.
>>>Не знаю как вам правильно описать что делает эта директива, надеюсь нашел верно, перевел в переводчике...

### 9. В каких сценариях использования применимы скобки {} и на какой строчке man bash это описано? 

* Показывет строку 174 мануала по bash (man bash):
  * RESERVED WORDS
        Reserved  words are words that have a special meaning to the shell.  The following words are recognized as re‐
        served when unquoted and either the first word of a simple command (see SHELL GRAMMAR below) or the third word
        of a case or for command:         ! case  coproc  do done elif else esac fi for function if in select then until while { } time [[ ]]

### 10. Основываясь на предыдущем вопросе, как создать однократным вызовом touch 100000 файлов?

* touch my_file_nomber_{1..100000} - ОК
* touch file{1..300000} - Ошибка "Слишком много аргументов" - превышено количество симфолов вводимых для 1 команды (длинна команды в строке превышена) 

### 11. В man bash поищите по /\\[\\[. Что делает конструкция [[ -d /tmp ]]

*  [[ expression ]]   Возвращает статус 0 или 1 в зависимости от оценки выражения условного выражения - нам еще не рассказывали как работать со скриптами и подобными сборками.

* Что делает конструкция [[ -d /tmp ]] - 
судя по описанию возвращает 0 или 1, если условие внутри скобок будет НЕ выполнено 
или ВЫПОЛНЕНО соответсвенно.

> ИСРПАВЛЕНИЕ ОТ 31 АВГУСТА 2022  
> Результатом команды будет ИСТИНА, так как каталог существует, по идее истина будет-(1),а  ложь-(0). А Если выходом донной конструкции является код ошибки (Error Code), то 0 - без ошибок (Истина, условие выполнено), а 1 - ложь, ошибка (Ложь, условие не выполнено)  
> 
> ~~[[ -d /tmp ]] возвращает логическое значение, а не физическую циру 0 или один, тем самым через echo ее вывести не можем, а если можем, то я не нашел как...~~    
>>  ИСПРАПВЛЕНИЕ ОТ 1 СЕНТЯБРЯ 2022  
>> ДОБАВИЛ ИСПРАВЛЕННЫЙ ОТВЕТ ПО МАТЕРИАЛАМ УРОКА ОТ 1 СЕНТЯБРЯ 2022  в ответ на ваш вопрос про echo $?     
>> vagrant@vagrant:~$ [[ -d /tmp ]] > /dev/null; echo $?  
>> 0
>>  


### 12. Основываясь на знаниях о просмотре текущих (например, PATH) и установке новых переменных; командах, которые мы рассматривали, добейтесь в выводе type -a bash в виртуальной машине наличия первым пунктом в списке: 

vagrant@vagrant:/$ mkdir /tmp/ttt  
vagrant@vagrant:/$ PATH=/tmp/ttt:$PATH  
vagrant@vagrant:/$ type -a bash  
bash is /usr/bin/bash  
bash is /bin/bash  
vagrant@vagrant:/$ cp /bin/bash /tmp/ttt/  
vagrant@vagrant:/$ type -a bash   
bash is /tmp/ttt/bash  
bash is /usr/bin/bash  
bash is /bin/bash  

### 13. Чем отличается планирование команд с помощью batch и at?

Судя по ману:
at запускает в определенное время команду (отложенный старт типа)
batch запускает компанду когда производительность (загруженность спадет ниже 1.5 - 1.5 чего?)

### 14. Завершите работу виртуальной машины чтобы не расходовать ресурсы компьютера и/или батарею ноутбука.

Выполнено! 