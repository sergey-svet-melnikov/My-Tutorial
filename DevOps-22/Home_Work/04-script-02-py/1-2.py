#python3

import os

bash_command = ["cd /Git/devops-netology/", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print('file', prepare_result, 'is located at: ', os.getcwd())
