#python3
#1-4.py

import time
import socket

site = {'mail.ru':'1.1.1.1', 'yandex.ru':'2.2.2.2', 'google.ru':'3.3.3.3'}
while 1 == 1 :
  for address in site :
    ip = socket.gethostbyname(address)
    if ip != site[adress] :
      print(' Ошибка ' + str(address) +' несовпадение адреса узла: '+site[address]+' '+ip)
      site[address]=ip
    else :
        print(str(address) + ' ' + ip)
    time.sleep(1)