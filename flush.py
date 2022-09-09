# https://stackoverflow.com/questions/15608229/what-does-prints-flush-do

import sys
from time import sleep

fp = sys.stdout
print("Do you want to continue (Y/n): ", end="")
# fp.flush() # comment and uncomment this to see flush work
sleep(5)
