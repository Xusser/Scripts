#!/usr/bin/python3
# coding: utf=8

import os
from pathlib import Path

LIMIT_IN = False
LIMIT_OUT = True
LIMIT_TOTAL = 1024 # GB

LOCK = Path("/var/run/trafficlimit.lock")


if __name__ == '__main__':
    RX = 0
    TX = 0
    
    vnstat = os.popen('vnstat --dumpdb').readlines()
    for line in vnstat:
        if line[0:4] == "m;0;":/
            mdata = line.split(";")
            RX=int(mdata[3])/1024
            TX=int(mdata[4])/1024
            break
    
    print('RX = ' + str(RX) + 'GB')
    print('TX = ' + str(TX) + 'GB')
    print('LIMIT = ' + str(LIMIT_TOTAL))
    
    TOTAL = 0
    if LIMIT_IN:
        #print('RX is limited')
        TOTAL += RX
    if LIMIT_OUT:
        #print('TX is limited')
        TOTAL += TX
    if TOTAL >= LIMIT_TOTAL:
        print('Limit reached!')
        if LOCK.is_file() == False:
            os.system('systemctl stop nginx.service')
            os.system('touch /var/run/trafficlimit.lock')
    else:
        print('Limit not reached')
        if LOCK.is_file() == True:
            os.system('systemctl start nginx.service')
            os.system('rm /var/run/trafficlimit.lock')
