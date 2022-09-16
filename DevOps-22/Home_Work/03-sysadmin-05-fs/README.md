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

* Создаем основной раздел первого диска (sdb 2,5Gb) объемом 2Gb

vagrant@vagrant:~$ sudo fdisk /dev/sdb                                                                                  
Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x3b0a8283.

Command (m for help): p
Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x3b0a8283

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-5242879, default 2048): 2048
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-5242879, default 5242879): +2G

Created a new partition 1 of type 'Linux' and of size 2 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

* Проверяем результат

vagrant@vagrant:~$ sudo fdisk -l | grep sdb
\Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
/dev/sdb1        2048 4196351 4194304   2G 83 Linux


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
└─sdb1                      8:17   0    2G  0 part
sdc                         8:32   0  2.5G  0 disk

### 5.  Используя sfdisk, перенесите данную таблицу разделов на второй диск.

vagrant@vagrant:~$ sudo sfdisk --dump /dev/sdb | sudo sfdisk /dev/sdc
Checking that no-one is using this disk right now ... OK

Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

>>> Script header accepted.
>>> Script header accepted.
>>> Script header accepted.
>>> Script header accepted.
>>> Created a new DOS disklabel with disk identifier 0x3b0a8283.
/dev/sdc1: Created a new partition 1 of type 'Linux' and of size 2 GiB.
/dev/sdc2: Done.

New situation:
Disklabel type: dos
Disk identifier: 0x3b0a8283

Device     Boot Start     End Sectors Size Id Type
/dev/sdc1        2048 4196351 4194304   2G 83 Linux

The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
vagrant@vagrant:~$ lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0                       7:0    0 43.6M  1 loop /snap/snapd/14978
loop1                       7:1    0 67.2M  1 loop /snap/lxd/21835
loop2                       7:2    0 61.9M  1 loop /snap/core20/1328
loop3                       7:3    0 63.2M  1 loop /snap/core20/1623
loop4                       7:4    0   48M  1 loop /snap/snapd/16778
loop5                       7:5    0 67.8M  1 loop /snap/lxd/22753
sda                         8:0    0   64G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0  1.5G  0 part /boot
└─sda3                      8:3    0 62.5G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0 31.3G  0 lvm  /
sdb                         8:16   0  2.5G  0 disk
└─sdb1                      8:17   0    2G  0 part
sdc                         8:32   0  2.5G  0 disk
└─sdc1                      8:33   0    2G  0 part

### 6. Соберите mdadm RAID1 на паре разделов 2 Гб.

vagrant@vagrant:~$ sudo mdadm --create --verbose /dev/md1 -l 1 -n 2 /dev/sd{b1,c1}
mdadm: Note: this array has metadata at the start and
    may not be suitable as a boot device.  If you plan to
    store '/boot' on this device please ensure that
    your boot-loader understands md/v1.x metadata, or use
    --metadata=0.90
mdadm: size set to 2094080K
Continue creating array? y
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md1 started.

vagrant@vagrant:~$ lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
loop0                       7:0    0 43.6M  1 loop  /snap/snapd/14978
loop1                       7:1    0 67.2M  1 loop  /snap/lxd/21835
loop2                       7:2    0 61.9M  1 loop  /snap/core20/1328
loop3                       7:3    0 63.2M  1 loop  /snap/core20/1623
loop4                       7:4    0   48M  1 loop  /snap/snapd/16778
loop5                       7:5    0 67.8M  1 loop  /snap/lxd/22753
sda                         8:0    0   64G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0  1.5G  0 part  /boot
└─sda3                      8:3    0 62.5G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0 31.3G  0 lvm   /
sdb                         8:16   0  2.5G  0 disk
└─sdb1                      8:17   0    2G  0 part
  └─md1                     9:1    0    2G  0 raid1
sdc                         8:32   0  2.5G  0 disk
└─sdc1                      8:33   0    2G  0 part
  └─md1                     9:1    0    2G  0 raid1

### 7. Соберите mdadm RAID0 на второй паре маленьких разделов.

* забыл сразу сделать второй раздел на 500 перед копированием sdb на sdc, прийдется сейчас создать эти два раздела:

vagrant@vagrant:~$ sudo fdisk /dev/sdb

Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (2-4, default 2):
First sector (4196352-5242879, default 4196352):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (4196352-5242879, default 5242879):

Created a new partition 2 of type 'Linux' and of size 511 MiB.

Command (m for help): w
The partition table has been altered.
Syncing disks.

vagrant@vagrant:~$ sudo fdisk /dev/sdc

Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (2-4, default 2):
First sector (4196352-5242879, default 4196352):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (4196352-5242879, default 5242879):

Created a new partition 2 of type 'Linux' and of size 511 MiB.

Command (m for help): w
The partition table has been altered.
Syncing disks.

* Просмотрим, все ли корректно

vagrant@vagrant:~$ lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
loop0                       7:0    0 43.6M  1 loop  /snap/snapd/14978
loop1                       7:1    0 67.2M  1 loop  /snap/lxd/21835
loop2                       7:2    0 61.9M  1 loop  /snap/core20/1328
loop3                       7:3    0 63.2M  1 loop  /snap/core20/1623
loop4                       7:4    0   48M  1 loop  /snap/snapd/16778
loop5                       7:5    0 67.8M  1 loop  /snap/lxd/22753
sda                         8:0    0   64G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0  1.5G  0 part  /boot
└─sda3                      8:3    0 62.5G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0 31.3G  0 lvm   /
sdb                         8:16   0  2.5G  0 disk
├─sdb1                      8:17   0    2G  0 part
│ └─md1                     9:1    0    2G  0 raid1
└─sdb2                      8:18   0  511M  0 part
sdc                         8:32   0  2.5G  0 disk
├─sdc1                      8:33   0    2G  0 part
│ └─md1                     9:1    0    2G  0 raid1
└─sdc2                      8:34   0  511M  0 part

* Создаем RAID0 мз двух разделов по 500

vagrant@vagrant:~$ sudo mdadm --create --verbose /dev/md2 -l 0 -n 2 /dev/sd{b2,c2}
mdadm: chunk size defaults to 512K
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md2 started.

vagrant@vagrant:~$ lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
loop0                       7:0    0 43.6M  1 loop  /snap/snapd/14978
loop1                       7:1    0 67.2M  1 loop  /snap/lxd/21835
loop2                       7:2    0 61.9M  1 loop  /snap/core20/1328
loop3                       7:3    0 63.2M  1 loop  /snap/core20/1623
loop4                       7:4    0   48M  1 loop  /snap/snapd/16778
loop5                       7:5    0 67.8M  1 loop  /snap/lxd/22753
sda                         8:0    0   64G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0  1.5G  0 part  /boot
└─sda3                      8:3    0 62.5G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0 31.3G  0 lvm   /
sdb                         8:16   0  2.5G  0 disk
├─sdb1                      8:17   0    2G  0 part
│ └─md1                     9:1    0    2G  0 raid1
└─sdb2                      8:18   0  511M  0 part
  └─md2                     9:2    0 1018M  0 raid0
sdc                         8:32   0  2.5G  0 disk
├─sdc1                      8:33   0    2G  0 part
│ └─md1                     9:1    0    2G  0 raid1
└─sdc2                      8:34   0  511M  0 part
  └─md2                     9:2    0 1018M  0 raid0

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

