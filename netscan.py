#!/usr/bin/env python

import nmap
import json


nm = nmap.PortScannerAsync()
def callback_result(host, scan_result):
#    print (host, scan_result)
#    print (host, scan_result['nmap']['scanstats']['uphosts'])
    result = []
    isUP = scan_result['nmap']['scanstats']['uphosts']
#    print (isUP)
    if isUP == '1':
        print (host, " UP")
        result.append([host,'UP'])
    else:
        print (host, " DOWN")
        result.append([host,'DOWN'])
    


nm.scan('10.10.101.0/28', arguments="-sP", callback=callback_result)
while nm.still_scanning():
    #print("Waiting >>>")
    nm.wait(1)

for i in range(len(result)):
        print result[i][0]
        print result[i][1]