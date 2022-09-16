## Домашнее задание к занятию "3.5. Файловые системы"

### 1. Узнайте о sparse (разряженных) файлах.

Ознакомился.   
Технология "сжатия" файлов за счет отказа от записи 0 значений на диск, а лишь пометкой их начала и конца в файле.   
Принцип архивирования (как бы сжатия) файлов средствами файловой системы при их хранении.

### 2.  Могут ли файлы, являющиеся жесткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?

Жесткие ссылки имеют те же параметры, что и сам файл, на который они ссылаются, фактически являясь этим же файлом, но доступным из другого адресного пространства (в рамках одной файловой системы). отсюда и название ЖЕСТКИЕ - можно сказать строгие, со строхим соотвествием.

### 3.  Сделайте vagrant destroy на имеющийся инстанс Ubuntu. Замените содержимое Vagrantfile следующим (нмже); Данная конфигурация создаст новую виртуальную машину с двумя дополнительными неразмеченными дисками по 2.5 Гб.:

>Vagrant.configure("2") do |config|  
  config.vm.box = "bento/ubuntu-20.04"  
  config.vm.provider :virtualbox do |vb|  
    lvm_experiments_disk0_path = "/tmp/lvm_experiments_disk0.vmdk"  
    lvm_experiments_disk1_path = "/tmp/lvm_experiments_disk1.vmdk"  
    vb.customize ['createmedium', '--filename', lvm_experiments_disk0_path, '--size', 2560]  
    vb.customize ['createmedium', '--filename', lvm_experiments_disk1_path, '--size', 2560]  
    vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', lvm_experiments_disk0_path]  
    vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', lvm_experiments_disk1_path]  
  end  
end  

Готово, машина создана. Проверим дисковую подсистему:

vagrant@vagrant:~$ lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0                       7:0    0 43.6M  1 loop /snap/snapd/14978
loop1                       7:1    0 67.2M  1 loop /snap/lxd/21835
loop2                       7:2    0 61.9M  1 loop /snap/core20/1328
sda                         8:0    0   64G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0  1.5G  0 part /boot
└─sda3                      8:3    0 62.5G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0 31.3G  0 lvm  /
sdb                         8:16   0  2.5G  0 disk
sdc                         8:32   0  2.5G  0 disk

### 4. Используя fdisk, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.




### 5.  Используя sfdisk, перенесите данную таблицу разделов на второй диск.

### 6. Соберите mdadm RAID1 на паре разделов 2 Гб.

### 7. Соберите mdadm RAID0 на второй паре маленьких разделов.

### 8.Создайте 2 независимых PV на получившихся md-устройствах.

### 9.Создайте общую volume-group на этих двух PV.

### 10.Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.

### 11.Создайте mkfs.ext4 ФС на получившемся LV.

### 12.Смонтируйте этот раздел в любую директорию, например, /tmp/new

### 13.Поместите туда тестовый файл, например wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz.

### 14.Прикрепите вывод lsblk.

### 15.Протестируйте целостность файла:

>root@vagrant:~# gzip -t /tmp/new/test.gz
root@vagrant:~# echo $?
0


### 16.Используя pvmove, переместите содержимое PV с RAID0 на RAID1.


### 17.Сделайте --fail на устройство в вашем RAID1 md.

### 18.Подтвердите выводом dmesg, что RAID1 работает в деградированном состоянии.

### 19.Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен:

>root@vagrant:~# gzip -t /tmp/new/test.gz
root@vagrant:~# echo $?
0

### 20.Погасите тестовый хост, vagrant destroy.

