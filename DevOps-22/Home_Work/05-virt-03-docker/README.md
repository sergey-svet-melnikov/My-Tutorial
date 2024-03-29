## Домашнее задание к занятию "3. Введение. Экосистема. Архитектура. Жизненный цикл Docker контейнера"

### 1. Обязательная задача 1

    Сценарий выполения задачи:

    создайте свой репозиторий на https://hub.docker.com;
    выберете любой образ, который содержит веб-сервер Nginx;
    создайте свой fork образа;
    реализуйте функциональность: запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:
    
    <html>
    <head>
    Hey, Netology
    </head>
    <body>
    <h1>I’m DevOps Engineer!</h1>
    </body>
    </html>
    
    Опубликуйте созданный форк в своем репозитории и предоставьте ответ в виде ссылки на https://hub.docker.com/username_repo.

ОТВЕТ:
        
        vagrant@server1:~/docker/nginx_netology$ cat Dockerfile
        FROM nginx
        COPY index.html /usr/share/nginx/html/
        
        vagrant@server1:~/docker/nginx_netology$ cat index.html
        <html>
        <head>
        <title>Hey, Netology</title>
        </head>
        <body>
        <h1>I’m DevOps Engineer!</h1>
        </body>
        </html>

        vagrant@server1:~/docker/nginx_netology$ sudo docker tag sergeysvetmelnikov/nginx_netology sergeysvetmelnikov/nginx_netology:v1
        vagrant@server1:~/docker/nginx_netology$ sudo docker push sergeysvetmelnikov/nginx_netology:v1
        vagrant@server1:~/docker/nginx_netology$ sudo docker run -it -p 8080:80 sergeysvetmelnikov/nginx_netology:v1

```html
        vagrant@server1:~/docker/nginx_netology$ curl localhost:8080  
        <html>  
        <head>  
        <title>Hey, Netology</title>  
        </head>  
        <body>  
        <h1>I’m DevOps Engineer!</h1>  
        </body>  
        </html>  
```

https://hub.docker.com/repository/docker/sergeysvetmelnikov/nginx_netology

### 2. Обязательная задача 2

    Посмотрите на сценарий ниже и ответьте на вопрос: "Подходит ли в этом сценарии 
    использование Docker контейнеров или лучше подойдет виртуальная машина, 
    физическая машина? Может быть возможны разные варианты?"

    Детально опишите и обоснуйте свой выбор.

    --

    Сценарий:

    Высоконагруженное монолитное java веб-приложение;

Высоконагрущенные среды лучше держать на отдельных физическихз серверах, 
организовывать аппаратную отказоустойчивость, либо на виртуальных машинах на аппаратных гипервизорах, 
если планируется рост или отказоустойчивость не аппратная (миграция машин)

    Nodejs веб-приложение;

Веб приложение лучше держать на контейнерах, для большой версионной текучки 

    Мобильное приложение c версиями для Android и iOS;

Скорее виртуальные машины, чем контейнеры, контейнеры не работают с графикой, графика требует ресурсов, а так же среду для эмуляции самого пространста прилоежний (ОС).

    Шина данных на базе Apache Kafka;

Маленькие брокеры сообщений не требуют много ресурсов, для большей и оптимально загрузки ресурсов подойдет контейнер, но и аппаратное решение и виртуальная машиа тоже подойдет. но лучше контейнер.

    Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;

Более нагруженные сервисы, чем прошлый, оптимально выделять достаточно требуемых ресурсов на виртуальных машинах под каждые сервисы + откзоустойчивость реализована.

    Мониторинг-стек на базе Prometheus и Grafana;

Виртуальная машина, несколько сервисов собраны в рамках одной машины.

    MongoDB, как основное хранилище данных для java-приложения;

Аппартный сервер с аппаратной избыточностью (железная балансировки или отказоустойчиывость или виртуальным машины), хотя если приложения небольшие, поток небольшой, то можно разбросать на разные сервера в контейнерых.

    Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.

Как угодно, зависит от нагрузок, не требует частой смены или перенастройки.
  
### 3.  Обязательная задача 3

    Запустите первый контейнер из образа centos c любым тэгом в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера;
    Запустите второй контейнер из образа debian в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера;
    Подключитесь к первому контейнеру с помощью docker exec и создайте текстовый файл любого содержания в /data;
    Добавьте еще один файл в папку /data на хостовой машине;
    Подключитесь во второй контейнер и отобразите листинг и содержание файлов в /data контейнера.

ОТВЕТ:



HOST:

    vagrant@server1:/data$ sudo mkdir /data
    vagrant@server1:/data$ sudo chmod 644 /data
    vagrant@server1:/data$ echo 123 > file_host
    vagrant@server1:/data$ ls
    file_host

CentOS:

    vagrant@server1:/data$ sudo docker run -it -v /data:/data --name centos centos
    root@e0fb219fd487 /# ls
    bin  data  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    root@e0fb219fd487 /# cd data
    root@e0fb219fd487 data# ls
    file_host
    root@e0fb219fd487 data# echo 123 > file_centos
    root@e0fb219fd487 data# ls
    file_centos  file_host

Debian:

    vagrant@server1:/data$ sudo docker run -it -v /data:/data --name debian debian
    root@f2304dc481c8:/# ls
    bin  boot  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    root@f2304dc481c8:/# cd data
    root@f2304dc481c8:/data# ls
    file_centos  file_host

### 4.  Задача 4 (*)

    Воспроизвести практическую часть лекции самостоятельно.

    Соберите Docker образ с Ansible, загрузите на Docker Hub и пришлите ссылку 
    вместе с остальными ответами к задачам.

ОТВЕТ:

    Собрали docker образ:

    vagrant@server1:~/docker/ansible_netology$ sudo docker build -t sergeysvetmelnikov/ansible_netology:v1 .

    Для сборки использовали Dockerfile:

    https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/05-virt-03-docker/Dockerfile

    В результате получился образ:

https://hub.docker.com/repository/docker/sergeysvetmelnikov/ansible_netology