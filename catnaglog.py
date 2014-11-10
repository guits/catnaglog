#!/usr/bin/python

__author__ = 'Guillaume Abrioux'

import time
import re
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument("-f", "--file",
            help="Path to the log file (Default: ./nagios.log)", type=str, required=False)

ARGS = PARSER.parse_args()

if ARGS.file:
    FILENAME = ARGS.file
else:
    FILENAME = './nagios.log'

try:
    F = open(FILENAME, 'r')
except IOError:
    print "Can't open file."
    exit(-1)

try:
    for line in F:
        m = re.match(r'^\[([^\]]+)\] (.+)$', line)
        if m is not None:
            timestamp = m.group(1)
            infos = m.group(2)
            hdate = time.strftime('%d/%m/%Y %H:%M:%S',
                                  time.localtime(int(timestamp)))
            print "[%s] %s" % (hdate, infos)
except (KeyboardInterrupt, IOError):
    pass
