#!/usr/bin/python3


from datetime import datetime as dt
from time import sleep

while True:
    f = open('timer.txt','a')
    t = '{0.year}-{0.month:02}-{0.day:02} {0.hour:02}:{0.minute:02}\n'.format(dt.now())
    f.write(t)
    f.close()
    sleep(60)
