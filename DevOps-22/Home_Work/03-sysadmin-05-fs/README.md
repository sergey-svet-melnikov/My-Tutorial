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

Готово, машина создана.

### 4. 
### 5.  
### 6. 
### 7. 