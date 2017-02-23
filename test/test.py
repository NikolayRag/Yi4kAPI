import logging
logging.basicConfig(level= logging.DEBUG)


import sys, os
sys.path.append(os.path.abspath('../..'))

from Yi4kAPI import *



import time, threading

a= YiAPI()

time.sleep(5)

a.close()

print('end')
