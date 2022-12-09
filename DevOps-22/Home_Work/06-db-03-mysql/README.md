# Домашнее задание к занятию "6.3. MySQL"

## Введение

Перед выполнением задания вы можете ознакомиться с 
[дополнительными материалами](https://github.com/netology-code/virt-homeworks/blob/virt-11/additional/README.md).

## Задача 1

Используя docker поднимите инстанс MySQL (версию 8). Данные БД сохраните в volume.

    vagrant@server1:~/docker-composer$ sudo docker pull mysql:8.0
    
    vagrant@server1:~/mysql$ sudo docker run --rm --name mysql-docker -e MYSQL_DATABASE=mydb -e MYSQL_ROOT_PASSWORD=netology -v /opt/backup:/opt/backup -v /var/lib/mysql:/var/lib/mysql -v /etc/mysql/conf.d:/etc/mysql/conf.d -p 3306:3306 -d mysq
    l:8.0
    3552f2b69cc33715ad007a89ce512c9bcf29b22c020dc9cf807bb5c54f926213
    
    vagrant@server1:~/mysql$ docker ps -a

    CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                    PORTS                                                  NAMES
    3552f2b69cc3   mysql:8.0     "docker-entrypoint.s…"   12 seconds ago   Up 9 seconds              0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   mysql-docker
    236924d69ca8   postgres:12   "docker-entrypoint.s…"   21 hours ago     Exited (0) 21 hours ago                                                          psql

   
Изучите [бэкап БД](https://github.com/netology-code/virt-homeworks/tree/virt-11/06-db-03-mysql/test_data) и 
восстановитесь из него.

    vagrant@server1:~/mysql$ ls
    test_dump.sql

    vagrant@server1:~/mysql$ sudo cp test_dump.sql /opt/backup/test.dump

    vagrant@server1:~/mysql$ sudo  docker exec -it mysql-docker bash

    bash-4.4# mysql -u root -p mydb < /opt/backup/test.dump
    Enter password:
    
Перейдите в управляющую консоль `mysql` внутри контейнера.

    bash-4.4# mysql -u root -p mydb
    Enter password:
    Reading table information for completion of table and column names
    You can turn off this feature to get a quicker startup with -A
    
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 10
    Server version: 8.0.31 MySQL Community Server - GPL
    
    Copyright (c) 2000, 2022, Oracle and/or its affiliates.
    
    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

Используя команду `\h` получите список управляющих команд.

    mysql> \h

    For information about MySQL products and services, visit:
    http://www.mysql.com/
    For developer information, including the MySQL Reference Manual, visit:
      http://dev.mysql.com/
    To buy MySQL Enterprise support, training, or other products, visit:
      https://shop.mysql.com/
    
    List of all MySQL commands:
    Note that all text commands must be first on line and end with ';'
    ?         (\?) Synonym for `help'.
    clear     (\c) Clear the current input statement.
    connect   (\r) Reconnect to the server. Optional arguments are db and host.
    delimiter (\d) Set statement delimiter.
    edit      (\e) Edit command with $EDITOR.
    ego       (\G) Send command to mysql server, display result vertically.
    exit      (\q) Exit mysql. Same as quit.
    go        (\g) Send command to mysql server.
    help      (\h) Display this help.
    nopager   (\n) Disable pager, print to stdout.
    notee     (\t) Don't write into outfile.
    pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
    print     (\p) Print current command.
    prompt    (\R) Change your mysql prompt.
    quit      (\q) Quit mysql.
    rehash    (\#) Rebuild completion hash.
    source    (\.) Execute an SQL script file. Takes a file name as an argument.
    status    (\s) Get status information from the server.
    system    (\!) Execute a system shell command.
    tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
    use       (\u) Use another database. Takes database name as argument.
    charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
    warnings  (\W) Show warnings after every statement.
    nowarning (\w) Don't show warnings after every statement.
    resetconnection(\x) Clean session context.
    query_attributes Sets string parameters (name1 value1 name2 value2 ...) for the next query to pick up.
    ssl_session_data_print Serializes the current SSL session data to stdout or file

    For server side help, type 'help contents'

Найдите команду для выдачи статуса БД и **приведите в ответе** из ее вывода версию сервера БД.

    mysql> \s
    --------------
    mysql  Ver 8.0.31 for Linux on x86_64 (MySQL Community Server - GPL)

    Connection id:          10
    Current database:       mydb
    Current user:           root@localhost
    SSL:                    Not in use
    Current pager:          stdout
    Using outfile:          ''
    Using delimiter:        ;
    Server version:         8.0.31 MySQL Community Server - GPL
    Protocol version:       10
    Connection:             Localhost via UNIX socket
    Server characterset:    utf8mb4
    Db     characterset:    utf8mb4
    Client characterset:    latin1
    Conn.  characterset:    latin1
    UNIX socket:            /var/run/mysqld/mysqld.sock
    Binary data as:         Hexadecimal
    Uptime:                 12 min 52 sec

    Threads: 2  Questions: 38  Slow queries: 0  Opens: 161  Flush tables: 3  Open tables: 79  Queries per second avg: 0.049
    --------------

Подключитесь к восстановленной БД и получите список таблиц из этой БД.

    mysql> use mydb
    Database changed
    
    mysql> show tables
    -> ;
    +----------------+
    | Tables_in_mydb |
    +----------------+
    | orders         |
    +----------------+
    1 row in set (0.01 sec)

**Приведите в ответе** количество записей с `price` > 300.

    mysql> select count(*) from orders where price >300;
    +----------+
    | count(*) |
    +----------+
    |        1 |
    +----------+
    1 row in set (0.00 sec)


В следующих заданиях мы будем продолжать работу с данным контейнером.

## Задача 2

Создайте пользователя test в БД c паролем test-pass, используя:
- плагин авторизации mysql_native_password
- срок истечения пароля - 180 дней 
- количество попыток авторизации - 3 
- максимальное количество запросов в час - 100
- аттрибуты пользователя:
- Фамилия "Pretty"
- Имя "James"


    mysql> CREATE USER 'test'@'localhost'  
    N_ATTEMPTS 3 PASSWORD_LOCK_TIME 2  
    ATTRIBUTE '{"first_name":    ->     IDENTIFIED WITH mysql_native_password BY 'test-pass'  
    ->     WITH MAX_CONNECTIONS_PER_HOUR 100  
    ->     PASSWORD EXPIRE INTERVAL 180 DAY  
    ->     FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2  
    ->     ATTRIBUTE '{"first_name":"James", "last_name":"Pretty"}';  
    Query OK, 0 rows affected (0.02 sec)  
  
Предоставьте привелегии пользователю `test` на операции SELECT базы `test_db`.

    mysql> GRANT SELECT ON mydb.* TO test@localhost;
    Query OK, 0 rows affected, 1 warning (0.01 sec)

    
Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES получите данные по пользователю `test` и 
**приведите в ответе к задаче**.

    mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES WHERE USER = 'test';
    +------+-----------+------------------------------------------------+
    | USER | HOST      | ATTRIBUTE                                      |
    +------+-----------+------------------------------------------------+
    | test | localhost | {"last_name": "Pretty", "first_name": "James"} |
    +------+-----------+------------------------------------------------+
    1 row in set (0.01 sec)

## Задача 3

Установите профилирование `SET profiling = 1`.
Изучите вывод профилирования команд `SHOW PROFILES;`.

Исследуйте, какой `engine` используется в таблице БД `test_db` и **приведите в ответе**.

    mysql> SELECT table_schema,table_name,engine FROM information_schema.tables WHERE table_schema = DATABASE();
    +--------------+------------+--------+
    | TABLE_SCHEMA | TABLE_NAME | ENGINE |
    +--------------+------------+--------+
    | mydb         | orders     | InnoDB |
    +--------------+------------+--------+
    1 row in set (0.01 sec)

Измените `engine` и **приведите время выполнения и запрос на изменения из профайлера в ответе**:
- на `MyISAM`
- на `InnoDB`


    mysql> SHOW PROFILES;
    Empty set, 1 warning (0.00 sec)

    mysql> SET profiling = 1;
    Query OK, 0 rows affected, 1 warning (0.00 sec)

    mysql> ALTER TABLE orders ENGINE = MyISAM;
    Query OK, 5 rows affected (0.04 sec)
    Records: 5  Duplicates: 0  Warnings: 0

    mysql> ALTER TABLE orders ENGINE = InnoDB;
    Query OK, 5 rows affected (0.05 sec)
    Records: 5  Duplicates: 0  Warnings: 0

    mysql> SHOW PROFILES;
    +----------+------------+------------------------------------+
    | Query_ID | Duration   | Query                              |
    +----------+------------+------------------------------------+
    |        1 | 0.04635875 | ALTER TABLE orders ENGINE = MyISAM |
    |        2 | 0.05535875 | ALTER TABLE orders ENGINE = InnoDB |
    +----------+------------+------------------------------------+
    2 rows in set, 1 warning (0.00 sec)

    mysql> SET profiling = 1;
    Query OK, 0 rows affected, 1 warning (0.00 sec)

    mysql> SHOW PROFILES;
    +----------+------------+------------------------------------+
    | Query_ID | Duration   | Query                              |
    +----------+------------+------------------------------------+
    |        1 | 0.04635875 | ALTER TABLE orders ENGINE = MyISAM |
    |        2 | 0.05535875 | ALTER TABLE orders ENGINE = InnoDB |
    |        3 | 0.00026300 | SET profiling = 1                  |
    +----------+------------+------------------------------------+
    3 rows in set, 1 warning (0.00 sec)
    

## Задача 4 

Изучите файл `my.cnf` в директории /etc/mysql.

Измените его согласно ТЗ (движок InnoDB):
- Скорость IO важнее сохранности данных
- Нужна компрессия таблиц для экономии места на диске
- Размер буффера с незакомиченными транзакциями 1 Мб
- Буффер кеширования 30% от ОЗУ
- Размер файла логов операций 100 Мб

Приведите в ответе измененный файл `my.cnf`.

    [mysqld]
    pid-file        = /var/run/mysqld/mysqld.pid
    socket          = /var/run/mysqld/mysqld.sock
    datadir         = /var/lib/mysql
    secure-file-priv= NULL
    
    !includedir /etc/mysql/conf.d/

    innodb_flush_log_at_trx_commit = 0
    innodb_file_per_table = ON
    innodb_log_buffer_size = 1M
    innodb_buffer_pool_size = 333M
    innodb_log_file_size = 100M

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---