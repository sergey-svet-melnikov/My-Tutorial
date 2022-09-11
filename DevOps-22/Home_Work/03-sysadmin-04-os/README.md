## Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

### 1. На лекции мы познакомились с node_exporter. В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой unit-файл для node_exporter:

vagrant@vagrant:/$ wget https://github.com/prometheus/node_exporter/releases/download/v1.4.0-rc.0/node_exporter-1.4.0-rc.0.linux-amd64.tar.gz

vagrant@vagrant:/$ tar zxvf node_exporter-*.linux-amd64.tar.gz

vagrant@vagrant:/$ cd node_exporter-*.linux-amd64

vagrant@vagrant:/$ cp node_exporter /usr/local/bin/node_exporter

vagrant@vagrant:/$ cat /etc/systemd/system/node_exporter.service

>[Unit]  
Description=Node Exporter GovorinAO (ByMe Edition)
After=multi-user.target
>
>[Service]  
EnvironmentFile=-/etc/default/node_exporter
ExecStart=/usr/local/bin/node_exporter $OPTIONS
IgnoreSIGPIPE=false
KillMode=process
Restart=on-failure
>
>[Install]  
WantedBy=multi-user.target

* поместите его в автозагрузку

vagrant@vagrant:~$ sudo systemctl enable node_exporter.service

* предусмотрите возможность добавления опций к запускаемому процессу через внешний файл (посмотрите, например, на systemctl cat cron),
* удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается.

Reboot

vagrant@vagrant:~$ ps -aux | grep node  
root        1235  0.0  1.2 716296 12052 ?        Ssl  13:06   0:00 /usr/local/bin/node_exporter

### 2. Ознакомьтесь с опциями node_exporter и выводом /metrics по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.

Пробрасываем порт 9100 на хость через конфиг Vagrant (vagrantfile):  

config.vm.network  "forwarded_port", guest: 9100, host: 9100, auto_correct: true

![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-04-os/node_exporter.png)

### 3. Установите в свою виртуальную машину Netdata. Воспользуйтесь готовыми пакетами для установки (sudo apt install -y netdata). После успешной установки:

vagrant@vagrant:~$ sudo apt install -y netdata

* в конфигурационном файле /etc/netdata/netdata.conf в секции [web] замените значение с localhost на bind to = 0.0.0.0,  

vagrant@vagrant:~$ cat /etc/netdata/netdata.conf

[global]
        run as user = netdata
        web files owner = root
        web files group = root
        # Netdata is not designed to be exposed to potentially hostile
        # networks. See https://github.com/netdata/netdata/issues/164
        bind socket to IP = 0.0.0.0

* добавьте в Vagrantfile проброс порта Netdata на свой локальный компьютер и сделайте vagrant reload: config.vm.network "forwarded_port", guest: 19999, host: 19999    

![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/03-sysadmin-04-os/netdata.png)


### 4. Можно ли по выводу dmesg понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?

vagrant@vagrant:~$ dmesg | grep virt  
[    0.004865] CPU MTRRs all blank - virtualized system.  
[    0.140272] Booting paravirtualized kernel on KVM  
[    5.821062] systemd[1]: Detected virtualization oracle.  

### 5.  


### 6.
### 7.