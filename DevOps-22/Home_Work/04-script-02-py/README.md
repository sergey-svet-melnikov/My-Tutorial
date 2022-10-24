## Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

### 1. Есть скрипт:

    #!/usr/bin/env python3
    a = 1
    b = '2'
    c = a + b

* "Какое значение будет присвоено переменной c?"    
      
Ответ: Будет ошибка - разные типы переменных (int(a) и str(b))  


* Как получить для переменной c значение 12?  

Ответ: Переопределить переменную "а" в тип "str": c = str(a) + b  

* Как получить для переменной c значение 3?

Ответ: Переопределить переменную "b" в тип "int": c = a + int(b)

### 2. Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?


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


ОТВЕТ:

В скрипет лишняя переменная типа Boolean (is_changed), а так же прерывание цикла поиска файлов псле первого найденного файла (break), убираем их и получаем результат.
P.S. Так же скрипт адаптирован под выполнение на локальной системе, где выполняется задание.

    #python3

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



### 4.  Обязательная задача 4


