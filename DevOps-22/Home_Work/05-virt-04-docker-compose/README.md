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


vagrant@server1:~/yc$ yc vpc network list --format yaml
- id: enp......................
  folder_id: b1g....................
  created_at: "2022-12-24T07:58:27Z"
  name: my-yc-network
  description: my first network via yc
  labels:
    my-label: my-value

vagrant@server1:~/yc$ yc vpc subnet list
+----------------------+----------------+----------------------+----------------+---------------+---------------+
|          ID          |      NAME      |      NETWORK ID      | ROUTE TABLE ID |     ZONE      |     RANGE     |
+----------------------+----------------+----------------------+----------------+---------------+---------------+
| e9b................. | my-yc-subnet-a | enp..................|                | ru-central1-a | [10.1.2.0/24] |
+----------------------+----------------+----------------------+----------------+---------------+---------------+

```
    
    Создадим файл образа для packer на основе CentOS7

```bash
    vagrant@server1:~/packer$ cat first_packer_centos7.json
{
  "builders": [
    {
      "disk_type": "network-hdd",
      "folder_id": "b1g3naro4vjh9i7bh6fj",
      "image_description": "CentOS 7 by packer",
      "image_family": "centos",
      "image_name": "centos-7-base",
      "source_image_family": "centos-7",
      "ssh_username": "centos",
      "subnet_id": "e9b0p0avhcjem7485as4",
      "token": "y0_AgAAAABPRyPjAATuwQAAAADXnHIkZfqZ52IzSdKXBjw-VZUYJ26X4lU",
      "type": "yandex",
      "use_ipv4_nat": true,
      "zone": "ru-central1-a"
    }
  ],
  "provisioners": [
    {
      "inline": [
        "sudo yum -y update",
        "sudo yum -y install bridge-utils bind-utils iptables curl net-tools tcpdump rsync telnet openssh-server"
      ],
      "type": "shell"
    }
  ]
}


```
    ...и создаем образ packer

```bash
    vagrant@server1:~/packer$ packer build first_packer_centos7.json
yandex: output will be in this color.

==> yandex: Creating temporary RSA SSH key for instance...
==> yandex: Using as source image: fd8jvcoeij6u9se84dt5 (name: "centos-7-v20221121", family: "centos-7")
==> yandex: Use provided subnet id e9b0p0avhcjem7485as4
==> yandex: Creating disk...
==> yandex: Creating instance...
==> yandex: Waiting for instance with id fhmqs28h31cg0vufiej6 to become active...
    yandex: Detected instance IP: 158.160.35.121
==> yandex: Using SSH communicator to connect: 158.160.35.121
==> yandex: Waiting for SSH to become available...
==> yandex: Connected to SSH!
==> yandex: Provisioning with shell script: /tmp/packer-shell1820688551
    yandex: Loaded plugins: fastestmirror
    yandex: Determining fastest mirrors
    yandex:  * base: mirror.yandex.ru
    yandex:  * extras: centos-mirror.rbc.ru
    yandex:  * updates: centos-mirror.rbc.ru
    yandex: Resolving Dependencies
    yandex: --> Running transaction check
    yandex: ---> Package grub2.x86_64 1:2.02-0.87.0.1.el7.centos.9 will be updated
    yandex: ---> Package grub2.x86_64 1:2.02-0.87.0.2.el7.centos.11 will be an update
    yandex: ---> Package grub2-common.noarch 1:2.02-0.87.0.1.el7.centos.9 will be updated
    yandex: ---> Package grub2-common.noarch 1:2.02-0.87.0.2.el7.centos.11 will be an update
    yandex: ---> Package grub2-pc.x86_64 1:2.02-0.87.0.1.el7.centos.9 will be updated
    yandex: ---> Package grub2-pc.x86_64 1:2.02-0.87.0.2.el7.centos.11 will be an update
    yandex: ---> Package grub2-pc-modules.noarch 1:2.02-0.87.0.1.el7.centos.9 will be updated
    yandex: ---> Package grub2-pc-modules.noarch 1:2.02-0.87.0.2.el7.centos.11 will be an update
    yandex: ---> Package grub2-tools.x86_64 1:2.02-0.87.0.1.el7.centos.9 will be updated
    yandex: ---> Package grub2-tools.x86_64 1:2.02-0.87.0.2.el7.centos.11 will be an update
    yandex: ---> Package grub2-tools-extra.x86_64 1:2.02-0.87.0.1.el7.centos.9 will be updated
    yandex: ---> Package grub2-tools-extra.x86_64 1:2.02-0.87.0.2.el7.centos.11 will be an update
    yandex: ---> Package grub2-tools-minimal.x86_64 1:2.02-0.87.0.1.el7.centos.9 will be updated
    yandex: ---> Package grub2-tools-minimal.x86_64 1:2.02-0.87.0.2.el7.centos.11 will be an update
    yandex: ---> Package kernel.x86_64 0:3.10.0-1160.81.1.el7 will be installed
    yandex: ---> Package kernel-tools.x86_64 0:3.10.0-1160.80.1.el7 will be updated
    yandex: ---> Package kernel-tools.x86_64 0:3.10.0-1160.81.1.el7 will be an update
    yandex: ---> Package kernel-tools-libs.x86_64 0:3.10.0-1160.80.1.el7 will be updated
    yandex: ---> Package kernel-tools-libs.x86_64 0:3.10.0-1160.81.1.el7 will be an update
    yandex: ---> Package kpartx.x86_64 0:0.4.9-135.el7_9 will be updated
    yandex: ---> Package kpartx.x86_64 0:0.4.9-136.el7_9 will be an update
    yandex: ---> Package krb5-libs.x86_64 0:1.15.1-54.el7_9 will be updated
    yandex: ---> Package krb5-libs.x86_64 0:1.15.1-55.el7_9 will be an update
    yandex: ---> Package python-perf.x86_64 0:3.10.0-1160.80.1.el7 will be updated
    yandex: ---> Package python-perf.x86_64 0:3.10.0-1160.81.1.el7 will be an update
    yandex: ---> Package rsync.x86_64 0:3.1.2-11.el7_9 will be updated
    yandex: ---> Package rsync.x86_64 0:3.1.2-12.el7_9 will be an update
    yandex: ---> Package tzdata.noarch 0:2022e-1.el7 will be updated
    yandex: ---> Package tzdata.noarch 0:2022g-1.el7 will be an update
    yandex: --> Finished Dependency Resolution
    yandex:
    yandex: Dependencies Resolved
    yandex:
    yandex: ================================================================================
    yandex:  Package               Arch     Version                         Repository
    yandex:                                                                            Size
    yandex: ================================================================================
    yandex: Installing:
    yandex:  kernel                x86_64   3.10.0-1160.81.1.el7            updates    52 M
    yandex: Updating:
    yandex:  grub2                 x86_64   1:2.02-0.87.0.2.el7.centos.11   updates    34 k
    yandex:  grub2-common          noarch   1:2.02-0.87.0.2.el7.centos.11   updates   733 k
    yandex:  grub2-pc              x86_64   1:2.02-0.87.0.2.el7.centos.11   updates    34 k
    yandex:  grub2-pc-modules      noarch   1:2.02-0.87.0.2.el7.centos.11   updates   860 k
    yandex:  grub2-tools           x86_64   1:2.02-0.87.0.2.el7.centos.11   updates   1.8 M
    yandex:  grub2-tools-extra     x86_64   1:2.02-0.87.0.2.el7.centos.11   updates   1.0 M
    yandex:  grub2-tools-minimal   x86_64   1:2.02-0.87.0.2.el7.centos.11   updates   177 k
    yandex:  kernel-tools          x86_64   3.10.0-1160.81.1.el7            updates   8.2 M
    yandex:  kernel-tools-libs     x86_64   3.10.0-1160.81.1.el7            updates   8.1 M
    yandex:  kpartx                x86_64   0.4.9-136.el7_9                 updates    81 k
    yandex:  krb5-libs             x86_64   1.15.1-55.el7_9                 updates   810 k
    yandex:  python-perf           x86_64   3.10.0-1160.81.1.el7            updates   8.2 M
    yandex:  rsync                 x86_64   3.1.2-12.el7_9                  updates   408 k
    yandex:  tzdata                noarch   2022g-1.el7                     updates   490 k
    yandex:
    yandex: Transaction Summary
    yandex: ================================================================================
    yandex: Install   1 Package
    yandex: Upgrade  14 Packages
    yandex:
    yandex: Total download size: 82 M
    yandex: Downloading packages:
    yandex: Delta RPMs disabled because /usr/bin/applydeltarpm not installed.
    yandex: --------------------------------------------------------------------------------
    yandex: Total                                               50 MB/s |  82 MB  00:01
    yandex: Running transaction check
    yandex: Running transaction test
    yandex: Transaction test succeeded
    yandex: Running transaction
    yandex:   Updating   : 1:grub2-common-2.02-0.87.0.2.el7.centos.11.noarch           1/29
    yandex:   Updating   : 1:grub2-tools-minimal-2.02-0.87.0.2.el7.centos.11.x86_64    2/29
    yandex:   Updating   : 1:grub2-tools-2.02-0.87.0.2.el7.centos.11.x86_64            3/29
    yandex:   Updating   : 1:grub2-tools-extra-2.02-0.87.0.2.el7.centos.11.x86_64      4/29
    yandex:   Updating   : 1:grub2-pc-modules-2.02-0.87.0.2.el7.centos.11.noarch       5/29
    yandex:   Updating   : 1:grub2-pc-2.02-0.87.0.2.el7.centos.11.x86_64               6/29
    yandex:   Updating   : kernel-tools-libs-3.10.0-1160.81.1.el7.x86_64               7/29
    yandex:   Updating   : kernel-tools-3.10.0-1160.81.1.el7.x86_64                    8/29
    yandex:   Updating   : 1:grub2-2.02-0.87.0.2.el7.centos.11.x86_64                  9/29
    yandex:   Updating   : python-perf-3.10.0-1160.81.1.el7.x86_64                    10/29
    yandex:   Updating   : tzdata-2022g-1.el7.noarch                                  11/29
    yandex:   Updating   : krb5-libs-1.15.1-55.el7_9.x86_64                           12/29
    yandex:   Updating   : kpartx-0.4.9-136.el7_9.x86_64                              13/29
    yandex:   Installing : kernel-3.10.0-1160.81.1.el7.x86_64                         14/29
    yandex:   Updating   : rsync-3.1.2-12.el7_9.x86_64                                15/29
    yandex:   Cleanup    : 1:grub2-2.02-0.87.0.1.el7.centos.9.x86_64                  16/29
    yandex:   Cleanup    : 1:grub2-pc-2.02-0.87.0.1.el7.centos.9.x86_64               17/29
    yandex:   Cleanup    : 1:grub2-tools-extra-2.02-0.87.0.1.el7.centos.9.x86_64      18/29
    yandex:   Cleanup    : 1:grub2-pc-modules-2.02-0.87.0.1.el7.centos.9.noarch       19/29
    yandex:   Cleanup    : 1:grub2-tools-2.02-0.87.0.1.el7.centos.9.x86_64            20/29
    yandex:   Cleanup    : 1:grub2-tools-minimal-2.02-0.87.0.1.el7.centos.9.x86_64    21/29
    yandex:   Cleanup    : kernel-tools-3.10.0-1160.80.1.el7.x86_64                   22/29
    yandex:   Cleanup    : 1:grub2-common-2.02-0.87.0.1.el7.centos.9.noarch           23/29
    yandex:   Cleanup    : tzdata-2022e-1.el7.noarch                                  24/29
    yandex:   Cleanup    : kernel-tools-libs-3.10.0-1160.80.1.el7.x86_64              25/29
    yandex:   Cleanup    : python-perf-3.10.0-1160.80.1.el7.x86_64                    26/29
    yandex:   Cleanup    : krb5-libs-1.15.1-54.el7_9.x86_64                           27/29
    yandex:   Cleanup    : kpartx-0.4.9-135.el7_9.x86_64                              28/29
    yandex:   Cleanup    : rsync-3.1.2-11.el7_9.x86_64                                29/29
    yandex:   Verifying  : 1:grub2-common-2.02-0.87.0.2.el7.centos.11.noarch           1/29
    yandex:   Verifying  : 1:grub2-tools-minimal-2.02-0.87.0.2.el7.centos.11.x86_64    2/29
    yandex:   Verifying  : rsync-3.1.2-12.el7_9.x86_64                                 3/29
    yandex:   Verifying  : 1:grub2-pc-2.02-0.87.0.2.el7.centos.11.x86_64               4/29
    yandex:   Verifying  : kernel-3.10.0-1160.81.1.el7.x86_64                          5/29
    yandex:   Verifying  : kernel-tools-3.10.0-1160.81.1.el7.x86_64                    6/29
    yandex:   Verifying  : kpartx-0.4.9-136.el7_9.x86_64                               7/29
    yandex:   Verifying  : krb5-libs-1.15.1-55.el7_9.x86_64                            8/29
    yandex:   Verifying  : 1:grub2-pc-modules-2.02-0.87.0.2.el7.centos.11.noarch       9/29
    yandex:   Verifying  : 1:grub2-tools-extra-2.02-0.87.0.2.el7.centos.11.x86_64     10/29
    yandex:   Verifying  : tzdata-2022g-1.el7.noarch                                  11/29
    yandex:   Verifying  : python-perf-3.10.0-1160.81.1.el7.x86_64                    12/29
    yandex:   Verifying  : kernel-tools-libs-3.10.0-1160.81.1.el7.x86_64              13/29
    yandex:   Verifying  : 1:grub2-2.02-0.87.0.2.el7.centos.11.x86_64                 14/29
    yandex:   Verifying  : 1:grub2-tools-2.02-0.87.0.2.el7.centos.11.x86_64           15/29
    yandex:   Verifying  : 1:grub2-pc-2.02-0.87.0.1.el7.centos.9.x86_64               16/29
    yandex:   Verifying  : kpartx-0.4.9-135.el7_9.x86_64                              17/29
    yandex:   Verifying  : 1:grub2-tools-extra-2.02-0.87.0.1.el7.centos.9.x86_64      18/29
    yandex:   Verifying  : 1:grub2-tools-minimal-2.02-0.87.0.1.el7.centos.9.x86_64    19/29
    yandex:   Verifying  : rsync-3.1.2-11.el7_9.x86_64                                20/29
    yandex:   Verifying  : 1:grub2-tools-2.02-0.87.0.1.el7.centos.9.x86_64            21/29
    yandex:   Verifying  : 1:grub2-2.02-0.87.0.1.el7.centos.9.x86_64                  22/29
    yandex:   Verifying  : kernel-tools-3.10.0-1160.80.1.el7.x86_64                   23/29
    yandex:   Verifying  : 1:grub2-pc-modules-2.02-0.87.0.1.el7.centos.9.noarch       24/29
    yandex:   Verifying  : tzdata-2022e-1.el7.noarch                                  25/29
    yandex:   Verifying  : python-perf-3.10.0-1160.80.1.el7.x86_64                    26/29
    yandex:   Verifying  : kernel-tools-libs-3.10.0-1160.80.1.el7.x86_64              27/29
    yandex:   Verifying  : 1:grub2-common-2.02-0.87.0.1.el7.centos.9.noarch           28/29
    yandex:   Verifying  : krb5-libs-1.15.1-54.el7_9.x86_64                           29/29
    yandex:
    yandex: Installed:
    yandex:   kernel.x86_64 0:3.10.0-1160.81.1.el7
    yandex:
    yandex: Updated:
    yandex:   grub2.x86_64 1:2.02-0.87.0.2.el7.centos.11
    yandex:   grub2-common.noarch 1:2.02-0.87.0.2.el7.centos.11
    yandex:   grub2-pc.x86_64 1:2.02-0.87.0.2.el7.centos.11
    yandex:   grub2-pc-modules.noarch 1:2.02-0.87.0.2.el7.centos.11
    yandex:   grub2-tools.x86_64 1:2.02-0.87.0.2.el7.centos.11
    yandex:   grub2-tools-extra.x86_64 1:2.02-0.87.0.2.el7.centos.11
    yandex:   grub2-tools-minimal.x86_64 1:2.02-0.87.0.2.el7.centos.11
    yandex:   kernel-tools.x86_64 0:3.10.0-1160.81.1.el7
    yandex:   kernel-tools-libs.x86_64 0:3.10.0-1160.81.1.el7
    yandex:   kpartx.x86_64 0:0.4.9-136.el7_9
    yandex:   krb5-libs.x86_64 0:1.15.1-55.el7_9
    yandex:   python-perf.x86_64 0:3.10.0-1160.81.1.el7
    yandex:   rsync.x86_64 0:3.1.2-12.el7_9
    yandex:   tzdata.noarch 0:2022g-1.el7
    yandex:
    yandex: Complete!
    yandex: Loaded plugins: fastestmirror
    yandex: Loading mirror speeds from cached hostfile
    yandex:  * base: mirror.yandex.ru
    yandex:  * extras: centos-mirror.rbc.ru
    yandex:  * updates: centos-mirror.rbc.ru
    yandex: Package iptables-1.4.21-35.el7.x86_64 already installed and latest version
    yandex: Package curl-7.29.0-59.el7_9.1.x86_64 already installed and latest version
    yandex: Package net-tools-2.0-0.25.20131004git.el7.x86_64 already installed and latest version
    yandex: Package rsync-3.1.2-12.el7_9.x86_64 already installed and latest version
    yandex: Package openssh-server-7.4p1-22.el7_9.x86_64 already installed and latest version
    yandex: Resolving Dependencies
    yandex: --> Running transaction check
    yandex: ---> Package bind-utils.x86_64 32:9.11.4-26.P2.el7_9.10 will be installed
    yandex: --> Processing Dependency: bind-libs-lite(x86-64) = 32:9.11.4-26.P2.el7_9.10 for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: --> Processing Dependency: bind-libs(x86-64) = 32:9.11.4-26.P2.el7_9.10 for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: --> Processing Dependency: liblwres.so.160()(64bit) for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: --> Processing Dependency: libisccfg.so.160()(64bit) for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: --> Processing Dependency: libisc.so.169()(64bit) for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: --> Processing Dependency: libirs.so.160()(64bit) for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: --> Processing Dependency: libdns.so.1102()(64bit) for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: --> Processing Dependency: libbind9.so.160()(64bit) for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: --> Processing Dependency: libGeoIP.so.1()(64bit) for package: 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64
    yandex: ---> Package bridge-utils.x86_64 0:1.5-9.el7 will be installed
    yandex: ---> Package tcpdump.x86_64 14:4.9.2-4.el7_7.1 will be installed
    yandex: --> Processing Dependency: libpcap >= 14:1.5.3-10 for package: 14:tcpdump-4.9.2-4.el7_7.1.x86_64
    yandex: --> Processing Dependency: libpcap.so.1()(64bit) for package: 14:tcpdump-4.9.2-4.el7_7.1.x86_64
    yandex: ---> Package telnet.x86_64 1:0.17-66.el7 will be installed
    yandex: --> Running transaction check
    yandex: ---> Package GeoIP.x86_64 0:1.5.0-14.el7 will be installed
    yandex: --> Processing Dependency: geoipupdate for package: GeoIP-1.5.0-14.el7.x86_64
    yandex: ---> Package bind-libs.x86_64 32:9.11.4-26.P2.el7_9.10 will be installed
    yandex: --> Processing Dependency: bind-license = 32:9.11.4-26.P2.el7_9.10 for package: 32:bind-libs-9.11.4-26.P2.el7_9.10.x86_64
    yandex: ---> Package bind-libs-lite.x86_64 32:9.11.4-26.P2.el7_9.10 will be installed
    yandex: ---> Package libpcap.x86_64 14:1.5.3-13.el7_9 will be installed
    yandex: --> Running transaction check
    yandex: ---> Package bind-license.noarch 32:9.11.4-26.P2.el7_9.10 will be installed
    yandex: ---> Package geoipupdate.x86_64 0:2.5.0-1.el7 will be installed
    yandex: --> Finished Dependency Resolution
    yandex:
    yandex: Dependencies Resolved
    yandex:
    yandex: ================================================================================
    yandex:  Package            Arch       Version                        Repository   Size
    yandex: ================================================================================
    yandex: Installing:
    yandex:  bind-utils         x86_64     32:9.11.4-26.P2.el7_9.10       updates     261 k
    yandex:  bridge-utils       x86_64     1.5-9.el7                      base         32 k
    yandex:  tcpdump            x86_64     14:4.9.2-4.el7_7.1             base        422 k
    yandex:  telnet             x86_64     1:0.17-66.el7                  updates      64 k
    yandex: Installing for dependencies:
    yandex:  GeoIP              x86_64     1.5.0-14.el7                   base        1.5 M
    yandex:  bind-libs          x86_64     32:9.11.4-26.P2.el7_9.10       updates     158 k
    yandex:  bind-libs-lite     x86_64     32:9.11.4-26.P2.el7_9.10       updates     1.1 M
    yandex:  bind-license       noarch     32:9.11.4-26.P2.el7_9.10       updates      91 k
    yandex:  geoipupdate        x86_64     2.5.0-1.el7                    base         35 k
    yandex:  libpcap            x86_64     14:1.5.3-13.el7_9              updates     139 k
    yandex:
    yandex: Transaction Summary
    yandex: ================================================================================
    yandex: Install  4 Packages (+6 Dependent packages)
    yandex:
    yandex: Total download size: 3.8 M
    yandex: Installed size: 9.0 M
    yandex: Downloading packages:
    yandex: --------------------------------------------------------------------------------
    yandex: Total                                               11 MB/s | 3.8 MB  00:00
    yandex: Running transaction check
    yandex: Running transaction test
    yandex: Transaction test succeeded
    yandex: Running transaction
    yandex:   Installing : 32:bind-license-9.11.4-26.P2.el7_9.10.noarch                1/10
    yandex:   Installing : geoipupdate-2.5.0-1.el7.x86_64                              2/10
    yandex:   Installing : GeoIP-1.5.0-14.el7.x86_64                                   3/10
    yandex:   Installing : 32:bind-libs-lite-9.11.4-26.P2.el7_9.10.x86_64              4/10
    yandex:   Installing : 32:bind-libs-9.11.4-26.P2.el7_9.10.x86_64                   5/10
    yandex:   Installing : 14:libpcap-1.5.3-13.el7_9.x86_64                            6/10
    yandex: pam_tally2: Error opening /var/log/tallylog for update: Permission denied
    yandex: pam_tally2: Authentication error
    yandex: useradd: failed to reset the tallylog entry of user "tcpdump"
    yandex:   Installing : 14:tcpdump-4.9.2-4.el7_7.1.x86_64                           7/10
    yandex:   Installing : 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64                  8/10
    yandex:   Installing : bridge-utils-1.5-9.el7.x86_64                               9/10
    yandex:   Installing : 1:telnet-0.17-66.el7.x86_64                                10/10
    yandex:   Verifying  : GeoIP-1.5.0-14.el7.x86_64                                   1/10
    yandex:   Verifying  : 14:libpcap-1.5.3-13.el7_9.x86_64                            2/10
    yandex:   Verifying  : 1:telnet-0.17-66.el7.x86_64                                 3/10
    yandex:   Verifying  : geoipupdate-2.5.0-1.el7.x86_64                              4/10
    yandex:   Verifying  : 32:bind-license-9.11.4-26.P2.el7_9.10.noarch                5/10
    yandex:   Verifying  : 32:bind-libs-9.11.4-26.P2.el7_9.10.x86_64                   6/10
    yandex:   Verifying  : 14:tcpdump-4.9.2-4.el7_7.1.x86_64                           7/10
    yandex:   Verifying  : bridge-utils-1.5-9.el7.x86_64                               8/10
    yandex:   Verifying  : 32:bind-libs-lite-9.11.4-26.P2.el7_9.10.x86_64              9/10
    yandex:   Verifying  : 32:bind-utils-9.11.4-26.P2.el7_9.10.x86_64                 10/10
    yandex:
    yandex: Installed:
    yandex:   bind-utils.x86_64 32:9.11.4-26.P2.el7_9.10   bridge-utils.x86_64 0:1.5-9.el7
    yandex:   tcpdump.x86_64 14:4.9.2-4.el7_7.1            telnet.x86_64 1:0.17-66.el7
    yandex:
    yandex: Dependency Installed:
    yandex:   GeoIP.x86_64 0:1.5.0-14.el7
    yandex:   bind-libs.x86_64 32:9.11.4-26.P2.el7_9.10
    yandex:   bind-libs-lite.x86_64 32:9.11.4-26.P2.el7_9.10
    yandex:   bind-license.noarch 32:9.11.4-26.P2.el7_9.10
    yandex:   geoipupdate.x86_64 0:2.5.0-1.el7
    yandex:   libpcap.x86_64 14:1.5.3-13.el7_9
    yandex:
    yandex: Complete!
==> yandex: Stopping instance...
==> yandex: Deleting instance...
    yandex: Instance has been deleted!
==> yandex: Creating image: centos-7-base
==> yandex: Waiting for image to complete...
==> yandex: Success image create...
==> yandex: Destroying boot disk...
    yandex: Disk has been deleted!
Build 'yandex' finished after 3 minutes 55 seconds.

==> Wait completed after 3 minutes 55 seconds

==> Builds finished. The artifacts of successful builds are:
--> yandex: A disk image was created: centos-7-base (id: fd8ab7gc8ijo9e1qi2bg) with family name centos

```

    Теперь мы имеем готовый образ ОС Centos7 в облаке Yandex.Cloud

```bash
    vagrant@server1:~/packer$ yc compute image list
+----------------------+---------------+--------+----------------------+--------+
|          ID          |     NAME      | FAMILY |     PRODUCT IDS      | STATUS |
+----------------------+---------------+--------+----------------------+--------+
| fd8ab7gc8ijo9e1qi2bg | centos-7-base | centos | f2ei2tsbd97v7jap5rhc | READY  |
+----------------------+---------------+--------+----------------------+--------+

```
![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/05-virt-04-docker-compose/yc_centos8_image.png)

## Задача 2

Создать вашу первую виртуальную машину в YandexCloud.

Для получения зачета, вам необходимо предоставить cкриншот страницы свойств созданной ВМ из личного кабинета YandexCloud.

ОТВЕТ:

    Создаем виртуальную машину с заранее подготовленными параметрами 

```bash

  vagrant@server1:~/.ssh$ yc compute instance create --name my-yc-instance --network-interface subnet-name=my-yc-subnet-a, nat-ip-version=ipv4 --zone ru-central1-a --ssh-key ~/.ssh/yc.pub
    done (20s)
  id: fhm..................
  folder_id: b1g...................
  created_at: "2022-12-24T09:58:22Z"
  name: my-yc-instance
  zone_id: ru-central1-a
  platform_id: standard-v2
  resources:
    memory: "2147483648"
    cores: "2"
    core_fraction: "100"
  status: RUNNING
  metadata_options:
    gce_http_endpoint: ENABLED
    aws_v1_http_endpoint: ENABLED
    gce_http_token: ENABLED
    aws_v1_http_token: ENABLED
  boot_disk:
    mode: READ_WRITE
    device_name: fhm...........
    auto_delete: true
    disk_id: fhmv..............
  network_interfaces:
    - index: "0"
      mac_address: d0:0d:79:*:*:*
      subnet_id: e9b.....................
      primary_v4_address:
        address: 10.1.2.27
        one_to_one_nat:
          address: 51.250.*.*
          ip_version: IPV4
  fqdn: ******.auto.internal
  scheduling_policy: {}
  network_settings:
    type: STANDARD
  placement_policy: {}
  
  vagrant@server1:~/.ssh$ yc compute instance list
+----------------------+----------------+---------------+---------+--------------+-------------+
|          ID          |      NAME      |    ZONE ID    | STATUS  | EXTERNAL IP  | INTERNAL IP |
+----------------------+----------------+---------------+---------+--------------+-------------+
| fhm................. | my-yc-instance | ru-central1-a | RUNNING | 51.250.**.***| 10.1.2.27   |
+----------------------+----------------+---------------+---------+--------------+-------------+
```        



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
  