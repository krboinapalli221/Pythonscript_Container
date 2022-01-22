#!/usr/bin/python3
import subprocess
def main_function(): 
    hello_world()
def hello_world():
   variableX = 'Hello World' 
   for increment_one in range(1, 1000):
       print(variableX)
       for increment_two in range(1, 1000):
           print(variableX)
           subprocess.run('sleep 2', shell=True)
if __name__ == '__main__':
    main_function()