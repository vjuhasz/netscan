#!/usr/bin/env python

import nmap
import operator
from natsort import natsorted

nm = nmap.PortScanner()
nm.scan(hosts='10.10.101.0/24', arguments='-n -v -sn')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))

sorted_list = natsorted(hosts_list, key=lambda host: host[0])

print "sorted"

for host, status in sorted_list:
    print('{0}:{1}'.format(host, status))