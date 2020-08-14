import os
import glob
import time

base_dir = '/tmp'
output_file = base_dir + '/output.txt'

def read_file():
    f = open(output_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def write_file():
    timenow = datetime.now()
    f = open(output_file, 'w')
    f.write = ("timenow")
    f.close()

