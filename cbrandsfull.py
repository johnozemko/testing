import pyexiv2
import os
import os.path
import sys
from xml.dom import minidom


images_in_dir = os.listdir("/Users/Cosmo/Desktop/Folder/images/")
xmls_in_dir = os.listdir("/Users/Cosmo/Desktop/Folder/xml/")
count = 0
for image_in_dir in images_in_dir:
	imagename = os.path.basename(image_in_dir)
	imageNameNoExt = os.path.splitext(imagename)[0]
	xmlName = imageNameNoExt +".xml"
	print xmlName
	pathWithName = '/Users/Cosmo/Desktop/Folder/xml/'+xmlName
	if os.path.exists(pathWithName):
		metadata = pyexiv2.ImageMetadata('/Users/Cosmo/Desktop/Folder/images/'+imagename)
		metadata.read()
		Test_file = open(pathWithName,'r')
		xmldoc = minidom.parse(Test_file)
		for i in range(len(xmldoc.getElementsByTagName('fieldName'))):
			SHIT = xmldoc.getElementsByTagName('fieldName')[i].firstChild.nodeValue
			if SHIT == 'onview_location':
				xmldoc.removeChild(xmldoc.getElementsByTagName('fieldName')[i].firstChild)
			key = xmldoc.getElementsByTagName('fieldName')[i].firstChild.nodeValue
			val = xmldoc.getElementsByTagName('value')[i].firstChild.nodeValue
			
			try:
				key = 'Xmp.xmp.' + key.encode('utf-8')
			except AttributeError:
				key = 'xmp.xmp.Bynder'+str(i)

			try:
				value = val.encode('utf-8')
			except AttributeError:
				value = 'Bynder'

			metadata[key] = pyexiv2.XmpTag(key, value)
			#write metadata to image
			metadata.write()
		Test_file.close()
		count += 1
		print """Added metadata to """ + str(count) + """ total images."""
	else:
		print "No xml for this file. "