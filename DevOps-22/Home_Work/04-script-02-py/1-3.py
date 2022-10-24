#python3

import os
import sys

path = sys.argv[1]
if path != "":
    bash_command = ["cd "+path, "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()
    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(prepare_result)
else:
    Print("Не задан путь к каталогу для проверки!")