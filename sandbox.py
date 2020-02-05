#!/usr/bin/python3

# port subprocess
# 
#  try:
#          subprocess.check_call("ls")
#  except:
#          print("subprocess.check_call() failed")
# ;
# import subprocess

# res = subprocess.check_output("ls"/
# command = ["ls", "-l"]
# subprocess.call(command)

# command = ["cd", "../"]
# subprocess.call(command)
# subprocess.call("cd")
# print(command)
#
#
 # import subprocess
 # import sys
#  
#  command = ["ls", "-l"]
#  
#  res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#  
#  sys.stdout.buffer.write(res.stdout)
#
# print('Hello')

import os;
import sys;
# def isPipe():
#         if select.select([sys.stdin,],[],[],0.0)[0]:
#                     return True
#                     return False
#
#                 if isPipe():
#                       print(sys.stdin.readlines())
#                   else:
#                         print("nothing")

def change_dir():
    curDir = os.getcwd();
    print(curDir)

    os.chdir("..//")

    curDir = os.getcwd();
    print(curDir)


for line in sys.stdin:
    print("===>", line)


# lines = sys.stdin.readlines()
# print(lines)

