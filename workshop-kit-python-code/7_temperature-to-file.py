import os
import glob
import time
import datetime
#initialize the device 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
	date_now = datetime.datetime.now()
        return temp_c, temp_f, date_now
	f = open("tempout.txt", 'w')
	f.write('temp is' + temp_c() + temp_f() + date_now())
	f.close()

while True:
	print(read_temp())
	time.sleep(5)
	#fh = open("tempout.txt", 'w')
	#fh.write(read_temp())
	#fh.write(temp_c, temp_f)
	#fh.close()
	#f = open("tempout.txt", 'w')
	#f.write('read_temp = ' + repr(read_temp) + '\n')
	#f.write('read_temp, (read_temp, repr(val))' + '\n')
	#f.write(temp_c, temp_f)
	#currenttime = print(datetimenow)
	#currenttemp = temp_c
	#f.write(read_temp)
	#f.close()
	#print(read_temp())	
	#time.sleep(3)
    	#f = open(/tmp/temp.txt, 'w')
    	#lines = f.readlines()
    	#f.close()

### NOTES : 
# check with following commands if the device is working
# if all outputs are blank device is not working
# 
#  modprobe w1-gpio 
#  modprobe w1-therm
#  cd /sys/bus/w1/devices/
#  ll
#
# FIX : 
# 
# add following string on end of file : /boot/config.txt
# 
# # For GPIO Thermometer : 
# dtoverlay=w1-gpio

