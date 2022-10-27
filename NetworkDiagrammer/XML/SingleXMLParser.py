import xml.etree.ElementTree as ET
import pandas as pd

#-------

raw_Ip_List = []
ScannedIPList = []
numOfScannedIps = 0

#This function is responsible for copying the xml informatin to a data frame
def host_intr_docs(xml_doc):
	#Get all atributes in the xml file
	attr = xml_doc.attrib

	#for eac of the xml elements within the address field
	for xml in xml_doc.iter('address'):

		#Copy the element to the datafram
		doc_dict = attr.copy()

		#update the dataframe
		doc_dict.update(xml.attrib)

		#set the dataframe data to the text of the xml attribute
		doc_dict['data'] = xml.text

		yield doc_dict

def port_intr_docs(xml_doc):

	attr = xml_doc.attrib

	for xml in xml_doc.iter('port'):

		#Copy the element to the datafram
		doc_dict = attr.copy()

		#update the dataframe
		doc_dict.update(xml.attrib)

		#set the dataframe data to the text of the xml attribute
		doc_dict['data'] = xml.text

		yield doc_dict

#This function takes in a list with duplicates, removes the duplicates, and sets the results to a new list
def clearDuplicates(dupList, newList):
	newList = [*set(dupList), 1]


#This parses the xml file into a variable
etree = ET.parse("Full_Scan_XML.xml")
#This sets a dataframe content from the function above. 
Host_df = pd.DataFrame(list(host_intr_docs(etree.getroot())))

Port_df = pd.DataFrame(list(port_intr_docs(etree.getroot())))

#This loop can get the contents of a column. In this case a target
for item in Host_df['addr']:
	#print(item)
	raw_Ip_List.append(item)

ScannedIPList = [*set(raw_Ip_List)]
ScannedIPList.sort()

print(ScannedIPList)

numOfScannedIps = len(ScannedIPList)

print('Number of Ips: ', numOfScannedIps)






#for event, elem in ET.iterparse("elrond_Scan_XML.xml"):
#	if elem.tag == 'address':
#		
#		printText = ET.tostring(elem, method="xml")
#		print(printText)
#
#		#print(addressString.split(':'))
#	
#
#	#if elem.tag == 'port':
#		#print(ET.tostring(elem, 'UTF-8', 'xml'))