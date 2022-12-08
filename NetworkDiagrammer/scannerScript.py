import sys
import os

targetIP = sys.argv[0]
outputName = 'nmapOutput2222.xml'

def setInfo(target):
    targetIP = target
    basicNmapScan()

def basicNmapScan():
    print("--Starting SCAN--")
    os.system("nmap -oX " + outputName + " " + targetIP)
    print("--Scan Complete--")
