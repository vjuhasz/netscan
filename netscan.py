#!/usr/bin/env python

import nmap
import json

result = []

nm = nmap.PortScannerAsync()
def callback_result(host, scan_result):
#    print (host, scan_result)
#    print (host, scan_result['nmap']['scanstats']['uphosts'])
    global result
    isUP = scan_result['nmap']['scanstats']['uphosts']
#    print (isUP)
    if isUP == '1':
        print (host, " UP")
        
        result.append([host,'UP'])
    else:
        print (host, " DOWN")        
        result.append([host,'DOWN'])
    
print "processing started"

nm.scan('10.10.101.0/30', arguments="-sP", callback=callback_result)
while nm.still_scanning():
    #print("Waiting >>>")
    nm.wait(1)
print "processing ended"

for i in range(len(result)):
        print result[i][0]
        print result[i][1]