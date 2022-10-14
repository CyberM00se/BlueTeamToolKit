import xml.etree.ElementTree as ET


myTree = ET.parse('elrond_Scan_XML.xml')

myRoot = myTree.getroot()

##print(myRoot[0].attrib)

#for x in myRoot[3]:
#	print(x.tag, x.attrib)

##for x in myRoot[2]:
##	print(x.text)

for host in myRoot.findall('host'):
	print(host.tag, host.attrib)
	for port in host.findall('port'):
		print (port.tag)