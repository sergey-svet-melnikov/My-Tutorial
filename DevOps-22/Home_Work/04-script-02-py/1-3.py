#python3
#1-3.py

import os
import sys

path = os.getcwd()
if len(sys.argv) > 1:
    path = sys.argv[1]
bash_command = [f'cd '+path, 'git status 2>&1']
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('not a git') != -1:
        print('Текущий или указанный каталог: ', path, '- не являтся репозиторием!')
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print('File', prepare_result, 'is modyfied and located at: ', path)
