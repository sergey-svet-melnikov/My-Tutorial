# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
 { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }

```


ОТВЕТ:
```
    { "info" : "Sample JSON output from our service",
        "elements" : [
            { 
            "name" : "first",
            "type" : "server",
            "ip" : "7.1.7.5"
            },
            {
            "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
    
```

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#python3
#jy.py


import socket
import yaml
import json
import time

site = {'drive.google.com':'1.1.1.1', 'mail.google.com':'2.2.2.2', 'google.com':'3.3.3.3'}
while 1 == 1 :
  for address in site :
    ip = socket.gethostbyname(address)
    if ip != site[address] :
      print('[ERROR] ' + str(address) + ' IP mismatch: ' + site[address] + ' new IP is: ' + ip)
      site[address] = ip
      with open(address + ".json", 'w') as jfile:
        json_data = json.dumps({address : ip})
        jfile.write(json_data)
      with open(address + ".yaml", 'w') as yfile:
        yaml_data= yaml.dump([{address : ip}])
        yfile.write(yaml_data)
    else :
        print(str(address) + ' IP is: ' + ip)
    time.sleep(3)
```

### Вывод скрипта при запуске при тестировании:
```
PS C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-03-yaml> python3 jy.py                        
[ERROR] drive.google.com IP mismatch: 1.1.1.1 new IP is: 64.233.162.194
[ERROR] mail.google.com IP mismatch: 2.2.2.2 new IP is: 172.217.21.165
[ERROR] google.com IP mismatch: 3.3.3.3 new IP is: 216.58.211.14
drive.google.com IP is: 64.233.162.194
mail.google.com IP is: 172.217.21.165
google.com IP is: 216.58.211.14

```

### json-файл(ы), который(е) записал ваш скрипт:
```

PS C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-03-yaml> ls *json

    Каталог: C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-03-yaml

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        01.11.2022     11:08             39 drive.google.com.json
-a----        01.11.2022     11:08             31 google.com.json
-a----        01.11.2022     11:08             37 mail.google.com.json

PS C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-03-yaml> cat *.json
{"drive.google.com": "173.194.222.194"}
{"google.com": "216.58.211.14"}
{"mail.google.com": "172.217.21.165"}

```

### yml-файл(ы), который(е) записал ваш скрипт:
```

PS C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-03-yaml> ls *yaml   

    Каталог: C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-03-yaml

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        01.11.2022     11:08             37 drive.google.com.yaml
-a----        01.11.2022     11:08             29 google.com.yaml
-a----        01.11.2022     11:08             35 mail.google.com.yaml

PS C:\Git\My-Tutorial\DevOps-22\Home_Work\04-script-03-yaml> cat *.yaml
- drive.google.com: 173.194.222.194
- google.com: 216.58.211.14
- mail.google.com: 172.217.21.165

```

