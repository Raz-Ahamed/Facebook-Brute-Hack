#install 
green="\033[0;32m"        # Green
import os
import os
import sys
import time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
delay_print(green+'%37s' % '   INSTALL.. \n')
os.system('apt update -y')
os.system('apt install termimage -y')
os.system('pip install requests bs4')
os.system('pip install pip install mechanize')
os.system('python3 fb2.py')
	