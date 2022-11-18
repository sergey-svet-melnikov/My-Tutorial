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