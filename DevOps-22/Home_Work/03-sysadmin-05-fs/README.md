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

vagrant@vagrant:~$ sudo pvscan  
  PV /dev/sda3   VG ubuntu-vg       lvm2 [<62.50 GiB / 31.25 GiB free]  
  PV /dev/md1                       lvm2 [<2.00 GiB]   
  PV /dev/md2                       lvm2 [1018.00 MiB]  
  Total: 3 [<65.49 GiB] / in use: 1 [<62.50 GiB] / in no VG: 2 [2.99 GiB]  

### 8.Создайте 2 независимых PV на получившихся md-устройствах.  

vagrant@vagrant:/etc/mdadm$ sudo pvcreate /dev/md1 /dev/md2  
  Physical volume "/dev/md1" successfully created.  
  Physical volume "/dev/md2" successfully created.  

### 9.Создайте общую volume-group на этих двух PV.  

vagrant@vagrant:/etc/mdadm$ sudo vgcreate vgroup /dev/md1 /dev/md2  
  Volume group "vgroup" successfully created  

vagrant@vagrant:/etc/mdadm$ sudo pvscan  
  PV /dev/sda3   VG ubuntu-vg       lvm2 [<62.50 GiB / 31.25 GiB free]  
  PV /dev/md1    VG vgroup          lvm2 [<2.00 GiB / <2.00 GiB free]  
  PV /dev/md2    VG vgroup          lvm2 [1016.00 MiB / 1016.00 MiB free]  
  Total: 3 [65.48 GiB] / in use: 3 [65.48 GiB] / in no VG: 0 [0   ]  
 
vagrant@vagrant:/etc/mdadm$ sudo vgdisplay  
  --- Volume group ---  
  VG Name               ubuntu-vg  
  System ID  
  Format                lvm2  
  Metadata Areas        1  
  Metadata Sequence No  2  
  VG Access             read/write  
  VG Status             resizable  
  MAX LV                0  
  Cur LV                1  
  Open LV               1  
  Max PV                0  
  Cur PV                1  
  Act PV                1  
  VG Size               <62.50 GiB  
  PE Size               4.00 MiB  
  Total PE              15999  
  Alloc PE / Size       7999 / <31.25 GiB  
  Free  PE / Size       8000 / 31.25 GiB   
  VG UUID               4HbbNB-kISH-fXeQ-qzbV-XeNd-At34-cCUUuJ   

  --- Volume group ---  
  VG Name               vgroup  
  System ID  
  Format                lvm2  
  Metadata Areas        2  
  Metadata Sequence No  1  
  VG Access             read/write  
  VG Status             resizable  
  MAX LV                0   
  Cur LV                0  
  Open LV               0   
  Max PV                0   
  Cur PV                2   
  Act PV                2   
  VG Size               <2.99 GiB  
  PE Size               4.00 MiB  
  Total PE              765  
  Alloc PE / Size       0 / 0  
  Free  PE / Size       765 / <2.99 GiB  
  VG UUID               0el9Jq-RZlY-dIuw-wUnn-J7g2-hBjz-329zQh  

### 10.Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.  


vagrant@vagrant:/etc/mdadm$ sudo lvcreate -L 100M -n logical_vol vgroup /dev/md2  
  Logical volume "logical_vol" created.  


vagrant@vagrant:/etc/mdadm$ sudo lvdisplay  
  --- Logical volume ---  
  LV Path                /dev/ubuntu-vg/ubuntu-lv  
  LV Name                ubuntu-lv  
  VG Name                ubuntu-vg  
  LV UUID                mJ8K7e-F4uw-o8Sx-iwt0-JfLQ-Dpoh-E7lSU1  
  LV Write Access        read/write  
  LV Creation host, time ubuntu-server, 2022-06-07 11:41:15 +0000  
  LV Status              available  
  open                 1  
  LV Size                <31.25 GiB    
  Current LE             7999  
  Segments               1  
  Allocation             inherit  
  Read ahead sectors     auto  
  - currently set to     256  
  Block device           253:0  

  --- Logical volume ---  
  LV Path                /dev/vgroup/logical_vol  
  LV Name                logical_vol  
  VG Name                vgroup  
  LV UUID                YWOLon-4a1d-oO7E-FUoA-qMfj-dMPG-y9SrHB  
  LV Write Access        read/write  
  LV Creation host, time vagrant, 2022-09-19 07:11:23 +0000  
  LV Status              available  
  open                 0  
  LV Size                100.00 MiB  
  Current LE             25  
  Segments               1  
  Allocation             inherit  
  Read ahead sectors     auto  
  - currently set to     4096  
  Block device           253:1  

### 11.Создайте mkfs.ext4 ФС на получившемся LV.  

vagrant@vagrant:/etc/mdadm$ sudo mkfs.ext4 /dev/vgroup/logical_vol   
mke2fs 1.45.5 (07-Jan-2020)  
Creating filesystem with 25600 4k blocks and 25600 inodes  

Allocating group tables: done  
Writing inode tables: done  
Creating journal (1024 blocks): done  
Writing superblocks and filesystem accounting information: done  

vagrant@vagrant:/etc/mdadm$ lsblk -o NAME,PATH,SIZE,FSTYPE  
NAME                      PATH                               SIZE FSTYPE  
loop0                     /dev/loop0                        61.9M squashfs  
loop1                     /dev/loop1                        67.8M squashfs  
loop2                     /dev/loop2                        67.2M squashfs  
loop3                     /dev/loop3                        63.2M squashfs  
loop4                     /dev/loop4                          48M squashfs  
loop5                     /dev/loop5                        43.6M squashfs  
sda                       /dev/sda                            64G  
├─sda1                    /dev/sda1                            1M  
├─sda2                    /dev/sda2                          1.5G ext4  
└─sda3                    /dev/sda3                         62.5G LVM2_member  
  └─ubuntu--vg-ubuntu--lv /dev/mapper/ubuntu--vg-ubuntu--lv 31.3G ext4  
sdb                       /dev/sdb                           2.5G  
├─sdb1                    /dev/sdb1                            2G linux_raid_member  
│ └─md1                   /dev/md1                             2G LVM2_member  
└─sdb2                    /dev/sdb2                          511M linux_raid_member  
  └─md2                   /dev/md2                          1018M LVM2_member  
    └─vgroup-logical_vol  /dev/mapper/vgroup-logical_vol     100M ext4  
sdc                       /dev/sdc                           2.5G  
├─sdc1                    /dev/sdc1                            2G linux_raid_member  
│ └─md1                   /dev/md1                             2G LVM2_member  
└─sdc2                    /dev/sdc2                          511M linux_raid_member  
  └─md2                   /dev/md2                          1018M LVM2_member  
    └─vgroup-logical_vol  /dev/mapper/vgroup-logical_vol     100M ext4  

### 12.Смонтируйте этот раздел в любую директорию, например, /tmp/new  

vagrant@vagrant:/tmp$ mkdir new  

vagrant@vagrant:/tmp$ sudo mount /dev/vgroup/logical_vol /tmp/new  

vagrant@vagrant:/tmp/new$ ll  
total 24  
drwxr-xr-x  3 root root  4096 Sep 19 07:13 ./  
drwxrwxrwt 13 root root  4096 Sep 19 07:16 ../  
drwx------  2 root root 16384 Sep 19 07:13 lost+found/  

### 13.Поместите туда тестовый файл, например wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz.  

vagrant@vagrant:/tmp/new$ sudo wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz  
--2022-09-19 07:18:52--  https://mirror.yandex.ru/ubuntu/ls-lR.gz  
Resolving mirror.yandex.ru (mirror.yandex.ru)... 213.180.204.183, 2a02:6b8::183  
Connecting to mirror.yandex.ru (mirror.yandex.ru)|213.180.204.183|:443... connected.  
HTTP request sent, awaiting response... 200 OK  
Length: 22324708 (21M) [application/octet-stream]  
Saving to: ‘/tmp/new/test.gz’  

/tmp/new/test.gz                         100%[=================================================================================>]  21.29M  1.16MB/s    in 17s  
  
2022-09-19 07:19:10 (1.22 MB/s) - ‘/tmp/new/test.gz’ saved [22324708/22324708]  

### 14.Прикрепите вывод lsblk.   

vagrant@vagrant:/tmp/new$ lsblk  
NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT  
loop0                       7:0    0 61.9M  1 loop  /snap/core20/1328  
loop1                       7:1    0 67.8M  1 loop  /snap/lxd/22753  
loop2                       7:2    0 67.2M  1 loop  /snap/lxd/21835  
loop3                       7:3    0 63.2M  1 loop  /snap/core20/1623  
loop4                       7:4    0   48M  1 loop  /snap/snapd/16778  
loop5                       7:5    0 43.6M  1 loop  /snap/snapd/14978  
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
    └─vgroup-logical_vol  253:1    0  100M  0 lvm   /tmp/new  
sdc                         8:32   0  2.5G  0 disk  
├─sdc1                      8:33   0    2G  0 part  
│ └─md1                     9:1    0    2G  0 raid1  
└─sdc2                      8:34   0  511M  0 part  
  └─md2                     9:2    0 1018M  0 raid0  
    └─vgroup-logical_vol  253:1    0  100M  0 lvm   /tmp/new  

### 15.Протестируйте целостность файла:  

vagrant@vagrant:/tmp/new$ gzip -t /tmp/new/test.gz  
vagrant@vagrant:/tmp/new$ echo $?  
0  

### 16.Используя pvmove, переместите содержимое PV с RAID0 на RAID1.  

vagrant@vagrant:/tmp/new$ sudo pvmove -n /dev/vgroup/logical_vol /dev/md2 /dev/md1  
  /dev/md2: Moved: 32.00%  
  /dev/md2: Moved: 100.00%  
vagrant@vagrant:/tmp/new$ lsblk  
NAME                      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT  
loop0                       7:0    0 61.9M  1 loop  /snap/core20/1328  
loop1                       7:1    0 67.8M  1 loop  /snap/lxd/22753  
loop2                       7:2    0 67.2M  1 loop  /snap/lxd/21835  
loop3                       7:3    0 63.2M  1 loop  /snap/core20/1623  
loop4                       7:4    0   48M  1 loop  /snap/snapd/16778  
loop5                       7:5    0 43.6M  1 loop  /snap/snapd/14978  
sda                         8:0    0   64G  0 disk  
├─sda1                      8:1    0    1M  0 part  
├─sda2                      8:2    0  1.5G  0 part  /boot  
└─sda3                      8:3    0 62.5G  0 part  
  └─ubuntu--vg-ubuntu--lv 253:0    0 31.3G  0 lvm   /  
sdb                         8:16   0  2.5G  0 disk  
├─sdb1                      8:17   0    2G  0 part  
│ └─md1                     9:1    0    2G  0 raid1    
│   └─vgroup-logical_vol  253:1    0  100M  0 lvm   /tmp/new  
└─sdb2                      8:18   0  511M  0 part  
  └─md2                     9:2    0 1018M  0 raid0  
sdc                         8:32   0  2.5G  0 disk  
├─sdc1                      8:33   0    2G  0 part  
│ └─md1                     9:1    0    2G  0 raid1  
│   └─vgroup-logical_vol  253:1    0  100M  0 lvm   /tmp/new  
└─sdc2                      8:34   0  511M  0 part  
  └─md2                     9:2    0 1018M  0 raid0  

### 17.Сделайте --fail на устройство в вашем RAID1 md.  

vagrant@vagrant:/tmp/new$ sudo mdadm /dev/md1 --fail /dev/sdb1  
mdadm: set /dev/sdb1 faulty in /dev/md1  

vagrant@vagrant:/tmp/new$ sudo mdadm --detail /dev/md1  
/dev/md1:  
           Version : 1.2  
     Creation Time : Fri Sep 16 06:09:09 2022   
        Raid Level : raid1  
        Array Size : 2094080 (2045.00 MiB 2144.34 MB)  
     Used Dev Size : 2094080 (2045.00 MiB 2144.34 MB)  
      Raid Devices : 2  
     Total Devices : 2  
       Persistence : Superblock is persistent  

Update Time : Mon Sep 19 07:37:55 2022  
             State : clean, degraded  
    Active Devices : 1  
   Working Devices : 1  
    Failed Devices : 1  
     Spare Devices : 0  

Consistency Policy : resync  

Тame : vagrant:1  (local to host vagrant)  
        UUID : 352a3faf:48bfb7bc:054ef78b:0fe27201  
           Events : 21  

    Number   Major   Minor   RaidDevice State
       -       0        0        0      removed
       1       8       33        1      active sync   /dev/sdc1

       0       8       17        -      faulty   /dev/sdb1

### 18.Подтвердите выводом dmesg, что RAID1 работает в деградированном состоянии.  

vagrant@vagrant:/tmp/new$ dmesg | grep fail  
[    0.329858] acpi PNP0A03:00: fail to add MMCONFIG information, can't access extended PCI configuration space under this bridge.  
[    3.568753] vboxvideo: module verification failed: signature and/or required key missing - tainting kernel  
[   10.376722] vboxsf: SHFL_FN_MAP_FOLDER failed for '/vagrant': share not found  
[ 6984.036256] md/raid1:md1: Disk failure on sdb1, disabling device.  

### 19.Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен:  

>root@vagrant:~# gzip -t /tmp/new/test.gz 
root@vagrant:~# echo $?  
0  

vagrant@vagrant:/tmp/new$ gzip -t /tmp/new/test.gz  
vagrant@vagrant:/tmp/new$ echo $?  
0  

### 20.Погасите тестовый хост, vagrant destroy.  
  
Готово.  

