import xml.etree.ElementTree as ET
import pandas as pd
from PIL import Image, ImageDraw, ImageFilter

#-----------------------------------------------------------
# Variables
raw_Ip_List = []
ScannedIPList = []
numOfScannedIps = 0
#-----------------------------------------------------------

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

#print('--------------------------------------------------------------------------')
#print(Host_df)
#print('--------------------------------------------------------------------------')
#print(Port_df)

print('--------------------------------------------------------------------------')
print('Scanned IP List:', ScannedIPList)

numOfScannedIps = len(ScannedIPList)

print('Number of Ips: ', numOfScannedIps)
print('--------------------------------------------------------------------------')

#--------------START of Image Creator-----------------------------------------------

#Variables
PaddingSizeX = 40
PaddingSizeY = 15

# (TODO) - To calculate number of wks per row use % to make sure there is no remainder, if there is increase the amt per row by 1
numWksPerRow = 6

# (TODO) - Incorperate numWksPerRow into this calculation instead of just raw number
BaseImageSizeX = (150 * numWksPerRow) + (PaddingSizeX * (numOfScannedIps + 1))
BaseImageSizeY = 500
Image_Filename = "TestImage1.png"


# (TODO) - Find the function to get these values from the image directly for modularity sake
iconWidth = 150
iconHeight = 80

#Images
# Image is 150x80
workstationIcon = Image.open('Images/Workstation.png')

#Create the base image
Canvas = Image.new('RGB', (BaseImageSizeX, BaseImageSizeY), color = 'white')
Canvas.save(Image_Filename)

count = 0
inRowCount = 0
numCurrentRows = 1
startX = 0 + PaddingSizeX
startY = 0 + PaddingSizeY

while count < numOfScannedIps:

	
	#This if statment checks to see how many icons have been placed in a row then starts a new row
	if inRowCount >= numWksPerRow:
		numCurrentRows = numCurrentRows + 1
		startX = PaddingSizeX
		startY = (iconHeight * numCurrentRows)
		inRowCount = 0
		print('###########################')
		print('CREATING NEW ROW')
		print('###########################')

	# Add the IP address of the workstation to the bottom of the image
	wksTextBox = ImageDraw.Draw(Canvas)
	
	#The text is positioned from the left side of the string. you have to get the full size of the string component and incorperate it into the calculation.
	txtSize = wksTextBox.textlength(ScannedIPList[count])
	
	#Setting the midpoints for the text
	midX = (((iconWidth - txtSize) / 2) + startX)
	midY = (startY + iconHeight + 5)
	
	# (TODO) - Potentially add the correct icon of the system to the image, this would just be an if statement comparing the list

	# This pastes the workstaton image on the white canvas.
	Canvas.paste(workstationIcon, (startX, startY), workstationIcon)

	wksTextBox.text(((midX), (midY)), ScannedIPList[count], fill=(0,0,0), align = "center")
	print('---------------------------')
	print('Number: ' + str(count + 1) + ' | Placing Text: ' + ScannedIPList[count] + ' | at position: ' + str(midX) + ' ' + str(midY))
	print('---------------------------')

	#Increasing the x position of the icon
	startX = startX + 150 + PaddingSizeX
	inRowCount = inRowCount + 1
	print('Workstation Pos : ', startX, startY)

	count = count + 1

#save the file
Canvas.save(Image_Filename)



#---Notes--

#if startX == (0 + PaddingSizeX):
	#	midX = (((iconWidth + (PaddingSizeX * 2)) / 2) + (PaddingSizeX * 2))
	#	midY = (startY + iconHeight + PaddingSizeY)
	#else:
	#	midX = (startX - (((iconWidth + (PaddingSizeX * 2)) / 2) + (PaddingSizeX * 2)))
	#	midY = (startY + iconHeight + (PaddingSizeY * 2))