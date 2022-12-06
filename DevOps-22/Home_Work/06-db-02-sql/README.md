## Домашнее задание к занятию "6.2. SQL"

Введение
Перед выполнением задания вы можете ознакомиться с дополнительными материалами. https://github.com/netology-code/virt-homeworks/blob/virt-11/additional/README.md

### 1. Обязательная задача 1

Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, в который будут складываться данные БД и бэкапы.

Приведите получившуюся команду или docker-compose манифест.

ОТВЕТ:

```yaml
version: '3.6'

volumes:
  db: {}
  backup: {}

services:

  postgres:
    image: postgres:12
    container_name: psql
    ports:
      - "0.0.0.0:5432:5432"
    volumes:
      - db:/var/lib/postgresql/data
      - backup:/opt/backup
    environment:
      POSTGRES_USER: "test-admin-user"
      POSTGRES_PASSWORD: "netology"
      POSTGRES_DB: "db_test"
    restart: always
```

    vagrant@server1:~/docker-composer$ sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose   
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current 
                                     Dload  Upload   Total   Spent    Left  Speed   
    0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  
    100 11.6M  100 11.6M    0     0  5309k      0  0:00:02  0:00:02 --:--:-- 6738k  
        
    vagrant@server1:~/docker-composer$ sudo chmod +x /usr/local/bin/docker-compose  
        
    vagrant@server1:~/docker-composer$ docker-compose --version 
    docker-compose version 1.26.0, build d4451659   
    
    vagrant@server1:~/docker-composer$ sudo docker-compose up -d    
    Creating network "docker-composer_default" with the default driver  
    Creating volume "docker-composer_db" with default driver    
    Creating volume "docker-composer_backup" with default driver    
    Creating psql ... done      

    vagrant@server1:~/docker-composer$ sudo docker exec -it psql bash  

    root@7fb2bd53c232:/#  psql -h localhost -U test-admin-user db_test  
    psql (12.13 (Debian 12.13-1.pgdg110+1)) 
    Type "help" for help.   

    db_test=#   


### 2. Обязательная задача 2

        В БД из задачи 1:

        создайте пользователя test-admin-user и БД test_db
        в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)
        предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db
        создайте пользователя test-simple-user
        предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db
        Таблица orders:

        id (serial primary key)
        наименование (string)
        цена (integer)
        Таблица clients:
        
        id (serial primary key)
        фамилия (string)
        страна проживания (string, index)
        заказ (foreign key orders)

ОТВЕТ: 

```sql
CREATE USER "test-admin-user";
CREATE DATABASE db_test;
CREATE TABLE orders (
    id SERIAL,
    наименование VARCHAR,
    цена INTEGER,
    PRIMARY KEY (id)
);
CREATE TABLE clients (
    id SERIAL,
    фамилия VARCHAR,
    "страна проживания" VARCHAR,
    заказ INTEGER,
    PRIMARY KEY (id),
    CONSTRAINT fk_заказ
      FOREIGN KEY(заказ)
            REFERENCES orders(id)
);
CREATE INDEX ON clients("страна проживания");
GRANT ALL ON TABLE orders, clients TO "test-admin-user";
CREATE USER "test-simple-user" WITH PASSWORD 'netology';
GRANT CONNECT ON DATABASE db_test TO "test-simple-user";
GRANT USAGE ON SCHEMA public TO "test-simple-user";
GRANT SELECT, INSERT, UPDATE, DELETE ON orders, clients TO "test-simple-user";
```

Приведите:

итоговый список БД после выполнения пунктов выше,

    db_test=# \l
                                             List of databases
    Name      |      Owner      | Encoding |  Collate   |   Ctype    |            Access privileges
    -----------+-----------------+----------+------------+------------+-----------------------------------------
    db_test   | test-admin-user | UTF8     | en_US.utf8 | en_US.utf8 | =Tc/"test-admin-user"                  +
              |                 |          |            |            | "test-admin-user"=CTc/"test-admin-user"+
              |                 |          |            |            | "test-simple-user"=c/"test-admin-user"
    postgres  | test-admin-user | UTF8     | en_US.utf8 | en_US.utf8 |
    template0 | test-admin-user | UTF8     | en_US.utf8 | en_US.utf8 | =c/"test-admin-user"                   +
              |                 |          |            |            | "test-admin-user"=CTc/"test-admin-user"
    template1 | test-admin-user | UTF8     | en_US.utf8 | en_US.utf8 | =c/"test-admin-user"                   +    
              |                 |          |            |            | "test-admin-user"=CTc/"test-admin-user"
    (4 rows)

описание таблиц (describe)

    db_test=# \d+ clients
                                                           Table "public.clients"
      Column       |       Type        | Collation | Nullable |               Default               | Storage  | Stats target | Description
    -------------------+-------------------+-----------+----------+-------------------------------------+----------+--------------+-------------
    id                | integer           |           | not null | nextval('clients_id_seq'::regclass) | plain    |
    фамилия           | character varying |           |          |                                     | extended |
    страна проживания | character varying |           |          |                                     | extended |
    заказ             | integer           |           |          |                                     | plain    |
    
    Indexes:
        "clients_pkey" PRIMARY KEY, btree (id)
        "clients_страна проживания_idx" btree ("страна проживания")
        Foreign-key constraints:
        "fk_заказ" FOREIGN KEY ("заказ") REFERENCES orders(id)
    Access method: heap

    db_test=# \d+ orders
                                                        Table "public.orders"
    Column    |       Type        | Collation | Nullable |              Default               | Storage  | Stats target
    | Description
    --------------+-------------------+-----------+----------+------------------------------------+----------+--------------+-------------
    id           | integer           |           | not null | nextval('orders_id_seq'::regclass) | plain    |
    наименование | character varying |           |          |                                    | extended |
    цена         | integer           |           |          |                                    | plain    |
    
    Indexes:
        "orders_pkey" PRIMARY KEY, btree (id)
    Referenced by:
        TABLE "clients" CONSTRAINT "fk_заказ" FOREIGN KEY ("заказ") REFERENCES orders(id)
    Access method: heap

SQL-запрос для выдачи списка пользователей с правами над таблицами test_db

    SELECT 
        grantee, table_name, privilege_type 
    FROM 
        information_schema.table_privileges 
    WHERE 
        grantee in ('test-admin-user','test-simple-user')
        and table_name in ('clients','orders')  
    order by 
        1,2,3;


список пользователей с правами над таблицами test_db


    db_test=# SELECT
        grantee, table_name, privilege_type
    FROM
        information_schema.table_privileges
    WHERE
        grantee in ('test-admin-user','test-simple-user')
        and table_name in ('clients','orders')
    order by
        1,2,3;
        grantee      | table_name | privilege_type
    ------------------+------------+----------------
    test-admin-user  | clients    | DELETE
    test-admin-user  | clients    | INSERT
    test-admin-user  | clients    | REFERENCES
    test-admin-user  | clients    | SELECT
    test-admin-user  | clients    | TRIGGER
    test-admin-user  | clients    | TRUNCATE
    test-admin-user  | clients    | UPDATE
    test-admin-user  | orders     | DELETE
    test-admin-user  | orders     | INSERT
    test-admin-user  | orders     | REFERENCES
    test-admin-user  | orders     | SELECT
    test-admin-user  | orders     | TRIGGER
    test-admin-user  | orders     | TRUNCATE
    test-admin-user  | orders     | UPDATE
    test-simple-user | clients    | DELETE
    test-simple-user | clients    | INSERT
    test-simple-user | clients    | SELECT
    test-simple-user | clients    | UPDATE
    test-simple-user | orders     | DELETE
    test-simple-user | orders     | INSERT
    test-simple-user | orders     | SELECT
    test-simple-user | orders     | UPDATE
    (22 rows)
  
### 3.  Обязательная задача 3

Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:

Таблица orders  

Наименование	цена  
Шоколад	10  
Принтер	3000  
Книга	500  
Монитор	7000  
Гитара	4000  

Таблица clients  

ФИО	Страна проживания  
Иванов Иван Иванович	USA  
Петров Петр Петрович	Canada  
Иоганн Себастьян Бах	Japan  
Ронни Джеймс Дио	Russia  
Ritchie Blackmore	Russia  

Используя SQL синтаксис:  

вычислите количество записей для каждой таблицы  
приведите в ответе:  
запросы  
результаты их выполнения.  
  
ОТВЕТ:  

    db_test=# INSERT INTO orders VALUES (1, 'Шоколад', 10), (2, 'Принтер', 3000), (3, 'Книга', 500), (4, 'Монитор', 7000), (5, 'Гитара', 4000);
    .INSERT 0 5

    db_test=# SELECT * FROM orders;
    id | наименование | цена
    ----+--------------+------
    1 | Шоколад      |   10
    2 | Принтер      | 3000
    3 | Книга        |  500
    4 | Монитор      | 7000
    5 | Гитара       | 4000
    (5 rows)

 
    db_test=# SELECT count(1) FROM orders;
    count
    -------
         5
    (1 row)

    db_test=# SELECT * FROM clients;
     id |       фамилия        | страна проживания | заказ
    ----+----------------------+-------------------+-------
     1 | Иванов Иван Иванович | USA               |
    2 | Петров Петр Петрович | Canada            |
    3 | Иоганн Себастьян Бах | Japan             |
    4 | Ронни Джеймс Дио     | Russia            |
    5 | Ritchie Blackmore    | Russia            |
    (5 rows)

    db_test=# SELECT count(1) FROM clients;
    count
    -------
         5
    (1 row)

### 4.  Обязательная задача 4 

Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.  

Используя foreign keys свяжите записи из таблиц, согласно таблице:  

ФИО	Заказ  
Иванов Иван Иванович	Книга  
Петров Петр Петрович	Монитор  
Иоганн Себастьян Бах	Гитара  
Приведите SQL-запросы для выполнения данных операций.  

Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса.  

Подсказка - используйте директиву UPDATE.  

ОТВЕТ:

    db_test=# UPDATE clients SET "заказ" = (SELECT id FROM orders WHERE "наименование"='Книга') WHERE "фамилия"='Иванов Иван Иванович';
    UPDATE 1
    db_test=# UPDATE clients SET "заказ" = (SELECT id FROM orders WHERE "наименование"='Монитор') WHERE "фамилия"='Петров Петр Петрович';
    UPDATE 1
    db_test=# UPDATE clients SET "заказ" = (SELECT id FROM orders WHERE "наименование"='Гитара') WHERE "фамилия"='Иоганн Себастьян Бах';
    UPDATE 1
    db_test=# SELECT a.* FROM clients a JOIN orders b ON a.заказ = b.id;
     id |       фамилия        | страна проживания | заказ
    ----+----------------------+-------------------+-------
      1 | Иванов Иван Иванович | USA               |     3
      2 | Петров Петр Петрович | Canada            |     4
      3 | Иоганн Себастьян Бах | Japan             |     5
    (3 rows)

### 5.  Обязательная задача 5

Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 (используя директиву EXPLAIN).  

Приведите получившийся результат и объясните что значат полученные значения.  

    db_test=# EXPLAIN SELECT a.* FROM clients a JOIN orders b ON a.заказ = b.id;
                                   QUERY PLAN
    ------------------------------------------------------------------------
    Hash Join  (cost=37.00..57.24 rows=810 width=72)
    Hash Cond: (a."заказ" = b.id)
    ->  Seq Scan on clients a  (cost=0.00..18.10 rows=810 width=72)
    ->  Hash  (cost=22.00..22.00 rows=1200 width=4)
             ->  Seq Scan on orders b  (cost=0.00..22.00 rows=1200 width=4)
    (5 rows)

    На сколько могу понимать было сделано следующее:
    1. Прочитана вся таблимца clients
    2. Прочитана вся таблица orders
    3. Создан кеш по id таблицы orders
    4. Для строк таблицы clients, по стобку заказ будет проверенно есть ли соотвествие поля id из кэша таблицы orders, при наличии такого соотвествия будет выданы соотвествующие строки.
    5. В описании плана запроса с EXPLAIN выдана информация о том, сколько времени потратится на поиск строк первой и последней, на сколько могу понять, сколько будет строк, какова будет длинна строк.

### 6.  Обязательная задача 6

