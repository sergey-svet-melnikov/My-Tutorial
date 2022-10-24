# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательная задача 1

Есть скрипт:
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:
| Вопрос  | Ответ |
| ------------- |--|
| Какое значение будет присвоено переменной `c`?  | Ошибка - разные типы |
| Как получить для переменной `c` значение 12?  | c = str(a) + b |
| Как получить для переменной `c` значение 3?  | c = a + int(b) |

## Обязательная задача 2
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:
```python
#python3
#1-2.py

import os

bash_command = ['cd /Git/devops-netology/', 'git status']
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print('File', prepare_result, 'is modyfied and located at: ', os.getcwd())
```

### Вывод скрипта при запуске при тестировании:
```
PS C:\Git\devops-netology> python3 C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-02-py\1-2.py
File README.md is modyfied and located at:  C:\Git\devops-netology
File test1 is modyfied and located at:  C:\Git\devops-netology

```

## Обязательная задача 3
1. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:
```python
#python3
#1-3.py

import os
import sys

path = os.getcwd()
if len(sys.argv) > 1:
    path = sys.argv[1]
bash_command = [f'cd '+path, 'git status 2>&1']
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('not a git') != -1:
        print('Текущий или указанный каталог: ', path, '- не являтся репозиторием!')
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print('File', prepare_result, 'is modyfied and located at: ', path)
```

### Вывод скрипта при запуске при тестировании:
```
PS C:\Git> python3 C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-02-py\1-3.py
Текущий или указанный каталог:  C:\Git - не являтся репозиторием!
PS C:\Git> python3 C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-02-py\1-3.py c:\temp
Текущий или указанный каталог:  c:\temp - не являтся репозиторием!
PS C:\Git> python3 C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-02-py\1-3.py C:\Git\devops-netology 
File README.md is modyfied and located at:  C:\Git\devops-netology
File test1 is modyfied and located at:  C:\Git\devops-netology

```

## Обязательная задача 4
1. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:
```python
???
```

### Вывод скрипта при запуске при тестировании:
```
???
```

## 2. Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?


    #python3

    import os

    bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()
    is_change = False
    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(prepare_result)
            break


ОТВЕТ:

В скрипет лишняя переменная типа Boolean (is_changed), а так же прерывание цикла поиска файлов псле первого найденного файла (break), убираем их и получаем результат.
P.S. Так же скрипт адаптирован под выполнение на локальной системе, где выполняется задание.

    #python3
    #1-2.py
    import os

    bash_command = ["cd /Git/devops-netology/", "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()
    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print('File', prepare_result, 'is modyfied and located at: ', os.getcwd())

РЕЗУЛЬТАТА ВЫВОДА РАБОТЫ СКРИПТА с проверкой:  

PS C:\Git\devops-netology> git status  
On branch fix  

Changes not staged for commit:  
  (use "git add <file>..." to update what will be committed)  
  (use "git restore <file>..." to discard changes in working directory)  
        modified:   README.md  
        modified:   test1  

no changes added to commit (use "git add" and/or "git commit -a")  

PS C:\Git\devops-netology> python3 C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-02-py\1-2.py
File README.md is modyfied and located at:  C:\Git\devops-netology
File test1 is modyfied and located at:  C:\Git\devops-netology
  

### 3. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

    #python3

    import os
    import sys

    path = os.getcwd()
    if len(sys.argv) > 1:
        path = sys.argv[1]
    bash_command = [f'cd '+path, 'git status 2>&1']
    result_os = os.popen(' && '.join(bash_command)).read()
    for result in result_os.split('\n'):
        if result.find('not a git') != -1:
            print('Текущий или указанный каталог: ', path, '- не являтся репозиторием!')
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print('File', prepare_result, 'is modyfied and located at: ', path)


ВЫВОД:  

PS C:\Git> python3 C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-02-py\1-3.py        
Текущий или указанный каталог:  C:\Git - не являтся репозиторием!  
PS C:\Git> python3 C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-02-py\1-3.py C:\temp  
Текущий или указанный каталог:  C:\temp - не являтся репозиторием!  
PS C:\Git> python3 C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-02-py\1-3.py C:\Git\devops-netology\  
File README.md is modyfied and located at:  C:\Git\devops-netology\  
File test1 is modyfied and located at:  C:\Git\devops-netology\  

### 4.  Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.

    #python3
    #1-4.py

    import time
    import socket

    site = {'drive.google.com':'1.1.1.1', 'mail.google.com':'2.2.2.2', 'google.com':'3.3.3.3'}
    while 1 == 1 :
    for address in site :
        ip = socket.gethostbyname(address)
        if ip != site[address] :
          print('[ERROR] ' + str(address) + ' IP mismatch: ' + site[address] + ' ' + ip)
          site[address] = ip
        else :
            print(str(address) + ' ' + ip)
        time.sleep(3)

ВЫВОД:   

    #python3
    #1-4.py

    import time
    import socket

    site = {'drive.google.com':'1.1.1.1', 'mail.google.com':'2.2.2.2', 'google.com':'3.3.3.3'}
    while 1 == 1 :
    for address in site :
        ip = socket.gethostbyname(address)
        if ip != site[address] :
          print('[ERROR] ' + str(address) + ' IP mismatch: ' + site[address] + ' ' + ip)
          site[address] = ip
        else :
            print(str(address) + ' ' + ip)
        time.sleep(3)
