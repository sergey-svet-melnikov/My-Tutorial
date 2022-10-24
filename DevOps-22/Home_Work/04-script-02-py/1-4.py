#python3
#1-4.py

import time
import socket

site = {'drive.google.com':'1.1.1.1', 'mail.google.com':'2.2.2.2', 'google.com':'3.3.3.3'}
while 1 == 1 :
  for address in site :
    ip = socket.gethostbyname(address)
    if ip != site[address] :
      print('[ERROR] ' + str(address) + ' IP mismatch: ' + site[address] + ' ' + ip)
      site[address] = ip
    else :
        print(str(address) + ' ' + ip)
    time.sleep(3)