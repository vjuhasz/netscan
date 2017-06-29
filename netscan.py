#!/usr/bin/env python

import nmap
import json

host_result = []

host_result.append(['kocsog'])

nm = nmap.PortScannerAsync()
def callback_result(host, scan_result, host_result):
#    print (host, scan_result)
#    print (host, scan_result['nmap']['scanstats']['uphosts'])
    
    isUP = scan_result['nmap']['scanstats']['uphosts']
#    print (isUP)
    if isUP == '1':
        print (host, " UP")
        
        host_result.append([host,'UP'])
    else:
        print (host, " DOWN")        
        host_result.append([host,'DOWN'])

    
    
print "processing started"

nm.scan('10.10.101.0/30', arguments="-sP", callback=callback_result)
while nm.still_scanning():
    #print("Waiting >>>")
    nm.wait(1)
print "processing ended"

for p in host_result: print p