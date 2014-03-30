#!/usr/bin/python

__author__ = 'guits'

import os
import sys
import time
import re


filename = './nagios.log'

f = open(filename, 'r')

try:
    for line in f:
        m = re.match('^\[([^\]]+)\] (.+)$', line)
        if re is not None:
            timestamp = m.group(1)
            infos = m.group(2)
            hdate = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(int(timestamp)))
            print "[%s] %s" % (hdate, infos)
except (KeyboardInterrupt, IOError):
    pass