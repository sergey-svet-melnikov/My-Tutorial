## Домашнее задание к занятию "6.2. SQL"

        Введение
        Перед выполнением задания вы можете ознакомиться с дополнительными материалами. https://github.com/netology-code/virt-homeworks/blob/virt-11/additional/README.md

### 1. Обязательная задача 1

        Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, в который будут складываться данные БД и бэкапы.

        Приведите получившуюся команду или docker-compose манифест.



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
        Приведите:

        итоговый список БД после выполнения пунктов выше,
        описание таблиц (describe)
        SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
        список пользователей с правами над таблицами test_db

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
  
### 3.  Обязательная задача 3



### 4.  Задача 4 (*)

  