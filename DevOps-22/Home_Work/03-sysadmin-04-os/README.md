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

### 2.
### 3.
### 4.
### 5.
### 6.
### 7.