#python3

import os
import sys

path = os.getcwd()
if len(sys.argv) != 1:
    path = sys.argv[1]
    bash_command = [f'cd '+path, 'git status']
    result_os = os.popen(' && '.join(bash_command)).read()
    for result in result_os.split('\n'):
        if result.find('fatal') != 0:
            print('Текущий или указанный каталог: ', path ,' - не являтся репозиторием!')
            if result.find('modified') != 0:
                print('File', prepare_result, 'is modyfied and located at: ', os.getcwd())
                print(os.getcwd() ,'/' , prepare_result)