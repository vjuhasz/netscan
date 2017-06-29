#!/usr/bin/env python

import nmap

nm = nmap.PortScannerAsync()
nm.all_hosts()  
nm.scan(hosts='10.10.101.0/30', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.host)