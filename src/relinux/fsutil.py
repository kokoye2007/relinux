'''
General filesystem utilities
@author: MiJyn
'''

import os

def makedir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def maketree(arr):
    for i in arr:
        makedir(i)