# Домашнее задание к занятию "4. Оркестрация группой Docker контейнеров на примере Docker Compose"

## Как сдавать задания

Обязательными к выполнению являются задачи без указания звездочки. Их выполнение необходимо для получения зачета и диплома о профессиональной переподготовке.

Задачи со звездочкой (*) являются дополнительными задачами и/или задачами повышенной сложности. Они не являются обязательными к выполнению, но помогут вам глубже понять тему.

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Любые вопросы по решению задач задавайте в чате учебной группы.

---


## Важно!

Перед отправкой работы на проверку удаляйте неиспользуемые ресурсы.
Это важно для того, чтоб предупредить неконтролируемый расход средств, полученных в результате использования промокода.

Подробные рекомендации [здесь](https://github.com/netology-code/virt-homeworks/blob/virt-11/r/README.md)

---

## Задача 1

Создать собственный образ  любой операционной системы (например, centos-7) с помощью Packer ([инструкция](https://cloud.yandex.ru/docs/tutorials/infrastructure-management/packer-quickstart))

Для получения зачета вам необходимо предоставить скриншот страницы с созданным образом из личного кабинета YandexCloud.

ОТВЕТ:

    Устанавливаем Packer на локальную машину

```bash
    wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt update && sudo apt install packer
```
        
    Разварачиваем на локальной машине средства управления виртуальными машинами и сервисами Yandex.Cloud

```bash
    vagrant@server1:~$ curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
    Downloading yc 0.99.0
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100 91.6M  100 91.6M    0     0   9.9M      0  0:00:09  0:00:09 --:--:-- 11.1M
    Yandex Cloud CLI 0.99.0 linux/amd64
    To complete installation, start a new shell (exec -l $SHELL) or type 'source "/home/vagrant/.bashrc"' in the current one
    vagrant@server1:~$ yc init
    Welcome! This command will take you through the configuration process.
    Please go to https://oauth.yandex.ru/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb in order to obtain OAuth token.
    
    Please enter OAuth token: y0_................................
    You have one cloud available: 'sergey-svet-melnikov' (id = b1g...................). It is going to be used by default.
    Please choose folder to use:
    [1] default (id = b1g..........................)
    [2] Create a new folder
    Please enter your numeric choice: 1
    Your current folder has been set to 'default' (id = b1g........................).
    Do you want to configure a default Compute zone? [Y/n] y
    Which zone do you want to use as a profile default?
    [1] ru-central1-a
    [2] ru-central1-b
    [3] ru-central1-c
    [4] Don't set default zone
    Please enter your numeric choice: 1
    Your profile default Compute zone has been set to 'ru-central1-a'.
    vagrant@server1:~$ yc config list
    token: y0_...........................
    cloud-id: b1g........................
    folder-id: b1g..........................
    compute-default-zone: ru-central1-a
```
    Создаем свою виртуальную сеть в облаке яндекса

```bash
    vagrant@server1:~/yc$ yc vpc network create --name my-yc-network --labels my-label=my-value --description "my first network via yc"
    
id: enp...................
folder_id: b1g....................
created_at: "2022-12-24T07:58:27Z"
name: my-yc-network
description: my first network via yc
labels:
  my-label: my-value
  
vagrant@server1:~/yc$ yc vpc subnet create --name my-yc-subnet-a --zone ru-central1-a --range 10.1.2.0/24 --network-name my-yc-network --description "my first subnet via yc"
id: e9b................
folder_id: b1g.....................
created_at: "2022-12-24T08:56:12Z"
name: my-yc-subnet-a
description: my first subnet via yc
network_id: enp....................
zone_id: ru-central1-a
v4_cidr_blocks:
  - 10.1.2.0/24
  
  vagrant@server1:~/yc$ yc vpc network list
+----------------------+---------------+
|          ID          |     NAME      |
+----------------------+---------------+
| enp................. | my-yc-network |
+----------------------+---------------+

```
    

## Задача 2

Создать вашу первую виртуальную машину в YandexCloud.

Для получения зачета, вам необходимо предоставить cкриншот страницы свойств созданной ВМ из личного кабинета YandexCloud.


        

## Задача 3

Создать ваш первый готовый к боевой эксплуатации компонент мониторинга, состоящий из стека микросервисов.

Для получения зачета, вам необходимо предоставить:
- Скриншот работающего веб-интерфейса Grafana с текущими метриками, как на примере ниже
<p align="center">
  <img width="1200" height="600" src="./assets/yc_02.png">
</p>

## Задача 4 (*)

Создать вторую ВМ и подключить её к мониторингу развёрнутому на первом сервере.

Для получения зачета, вам необходимо предоставить:
- Скриншот из Grafana, на котором будут отображаться метрики добавленного вами сервера.
  