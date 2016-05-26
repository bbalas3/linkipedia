import urllib, urllib2
from lxml import etree as ET
import re
import codecs
from lxml import objectify
import io

tree = ET.parse('XmlEtree1.xml')
root = tree.getroot()
f1 = codecs.open("work1.txt", "w", "utf-8")

context = ET.iterparse("XmlEtree1.xml",tag='dataset')

print 'Title:'
for title1 in tree.xpath('//dataset/title'):
	if title1.text is not None:
		title = title1.text
		title = title.strip()
		# print title
# with open ('proc1.txt','a') as procseq:
          	f1.write("RowClass"+"\t"+"rdfs:label"+"\t"+title+"\n")

print('\n')
print 'Abstract:'
for abstract1 in tree.xpath('//dataset/abstract/para'):
	if abstract1.text is not None:
		abstract = abstract1.text
		abstract = abstract.strip()
		# print abstract
# with open ('proc1.txt','a') as procseq:
          	f1.write("RowClass"+"\t"+"rdfs:comment"+"\t"+abstract+"\n")

print("******")
for dTab in root.iter("dataTable"):
	# print(dTab)
	# dLev = dTab.xpath('.//attributeName')
	f1.write("RowClass"+"\t"+"hasDataTable"+"\t"+dTab.attrib['id']+"\n")
	eNameList = []
	for df4 in dTab.xpath('.//entityName'):
		if df4.text is not None:
			eName = df4.text
			eName = eName.strip()
			# print eName
			f1.write(dTab.attrib['id']+"\t"+"hasEntity"+"\t"+eName+"\n")
			# eNameList.append(eName)
	for df5 in dTab.xpath('.//entityDescription'):
		if df5.text is not None:
			eDesc = df5.text
			eDesc = eDesc.strip()
			# print eDesc
			f1.write(dTab.attrib['id']+"\t"+"hasEntityDescription"+"\t"+eDesc+"\n")
	i = 0	
	j = 0
	df13List = []
	df3List = []
	df6List = []
	df7List = []
	df8List = []
	df9List = []
	df10List = []
	for df13 in dTab.xpath('.//attribute'):
		# print ("yay!!!")
		# print df13.attrib['id']
		df13List.append(df13.attrib['id'])
		
	for df3 in dTab.xpath('.//attributeName'):
		aName = df3.text
		aName = aName.strip()
		df3List.append(aName)
	for df6 in dTab.xpath('.//attributeLabel'):
		aLabel = df6.text
		aLabel = aLabel.strip()
		df6List.append(aLabel)
	for df7 in dTab.xpath('.//attributeDefinition'):
		aDefn = df7.text
		aDefn = aDefn.strip()
		df7List.append(aDefn)
	print("$$$$$$$$$$$$$$$$$$$$")
	print len(df13List)
	t = []
	for j in range(len(df13List)):
		for df143 in dTab.xpath('.//attribute'):
			if df143.attrib['id'] == df13List[j]:
				print (df13List[j]+' :   ')
				if (df143.xpath('.//nonNumericDomain/textDomain/definition/text()') != t):
					x = df143.xpath('.//nonNumericDomain/textDomain/definition/text()')
					f1.write(df13List[j] + "\t"+"hasMeasurementType"+"\t"+x[0]+"\n")
					#f1.write(x[0])
				else:
					if (df143.xpath('.//measurementScale/ratio/unit/standardUnit/text()') != t):
						x = df143.xpath('.//measurementScale/ratio/unit/standardUnit/text()')
						f1.write(df13List[j] + "\t"+"hasMeasurementUnit"+"\t"+x[0]+"\n")
						#f1.write(x[0])
						if (df143.xpath('.//numericDomain/numberType/text()') != t):
							y = df143.xpath('.//numericDomain/numberType/text()')
							f1.write(df13List[j] + "\t"+"hasMeasurementNumType"+"\t"+y[0]+"\n")
							#f1.write(y[0])
					else:
						if (df143.xpath('.//measurementScale/ratio/unit/customUnit/text()') != t):
							x = df143.xpath('.//measurementScale/ratio/unit/customUnit/text()')
							f1.write(df13List[j] + "\t"+"hasMeasurementUnit"+"\t"+x[0]+"\n")
							#f1.write(x[0])
							if (df143.xpath('.//numericDomain/numberType/text()') != t):
								y = df143.xpath('.//numericDomain/numberType/text()')
								f1.write(df13List[j] + "\t"+"hasMeasurementNumType"+"\t"+y[0]+"\n")
								#f1.write(y[0])
						else:
							if (df143.xpath('.//dateTime/formatString/text()') != t):
								x = df143.xpath('.//dateTime/formatString/text()')
								f1.write(df13List[j] + "\t"+"hasMeasurementType"+"\t"+x[0]+"\n")
								#f1.write(x[0])

				
				
	print df13List
	print df3List
	print df6List
	print df7List
	print df8List
	for i in range (len(df13List)):
		print(df13List[i]+" : "+df3List[i]+" : "+df6List[i]+" : "+df7List[i])
		f1.write(eName + "\t"+"hasAttributeName"+"\t"+df3List[i]+"\n")
		f1.write(df3List[i] + "\t"+"hasAttributeLabel"+"\t"+df6List[i]+"\n")
		f1.write(df3List[i] + "\t"+"hasAttributeDefinition"+"\t"+df7List[i]+"\n")
		# print(df8List[i])
		
		
		

f1.close()


		
