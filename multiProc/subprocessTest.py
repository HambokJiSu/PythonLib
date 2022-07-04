#	시스템 명령어를 실행하려면? ― subprocess

import subprocess

with open('out.txt', 'wb') as f:
    out = subprocess.run(['cmd', "/c" 'dir'], capture_output=True)
    f.write(out.stdout)

#	복잡한 명령어의 실행
import subprocess

subprocess.run('find ./ -name "*.html"|xargs grep "python"', shell=True)