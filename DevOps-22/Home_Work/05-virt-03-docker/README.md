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

        vagrant@server1:~/docker/nginx_netology$ sudo docker run -d -p 8080:80 sergeysvetmelnikov/nginx_netology:v3  

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
![](https://hub.docker.com/repository/docker/sergeysvetmelnikov/nginx_netology) 

### 2. Обязательная задача 2


  
### 3.  Обязательная задача 3
