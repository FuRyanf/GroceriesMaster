from subprocess import call
import xlwt
import re
# run tesseract's OCR
# Only tested with costco reciepts
# assumptions and considerations
# Each line has a period
# binarisation gives 

# border removal using numpy
# regex format \w\s*(\d+)\s*(.+)\s*(\d+\.\d+) try on the non converted

call(["tesseract", "hello.png", "parsed"])
# binarisation rotation using ImageMagick helps with getting exact numbers
call(["convert", "-colorspace", "gray", "-colors", "2", "-normalize", "reciept3.png", "reciept3conv.png"])
call(["tesseract", "reciept3conv.png", "parsed2"])

# to extract only numbers, start from last element until first period

f=open('parsed.txt')

itemList=[]
priceList=[]
parsingList = []
for line in f:
	if str(line[-1:]) == '\n' and '.' in line:
		parsingList.append(line[:-1])
		print line[:-1]
	elif '.' in line:
		parsingList.append(line)
		#print line

print "+++++++++++++++"
print parsingList[0]

#f2=open('parsed2.txt')
# itemList2=[]
# priceList2=[]
# parsingList2= []
# for line in f2:
# 	if str(line[-1:]) == '\n' and '.' in line:
# 		parsingList2.append(line[:-1])
# 		print line[:-1]
# 	elif '.' in line:
# 		parsingList2.append(line)
# 		print line


# #If item is not equal to E then gg
# #additionally can implement regex
# numbers=['1','2','3','4','5','6','7','8','9','0','.']
# numbers2=['1','2','3','4','5','6','7','8','9','0']
# initVals=['1','2','3','4','5','6','7','8','9','0','E']
# mistake=[',','_','-']
# mistakeNum=['g']
# count = 0
# while count < len(parsingList):
# 	if parsingList[count]=='' or parsingList[count][0]!='E':
# 		parsingList.pop(count)
# 	else:
# 		count+=1
# for element in parsingList:
# 	count = 1
# 	word =""
# 	while count < len(element) and element[count] in numbers or element[count]==' ':
# 		count+=1

# 	# print count
# 	while count < len(element) and element[count] not in numbers2:
# 		word+=element[count]
# 		count+=1

# 	price =""
# 	while count < len(element):
# 		if element[count] in mistake:
# 			price+='.'
# 		elif element[count] in mistakeNum:
# 			price+='9'
# 		elif element[count] in numbers:
# 			price+=element[count]
# 		elif element[count] == ' ':
# 			print ""
# 		else:
# 			break
# 		count+=1
# 	print price
# 	print word
# 	itemList.append(word)
# 	try: 
# 		priceList.append(float(price))
# 	except:
# 		priceList.append(price)


# print parsingList
# print len(parsingList)



# book = xlwt.Workbook(encoding="utf-8")
# sheet1 = book.add_sheet("Sheet 1")
# names=["Ryan","Leonard","Alex","Henry","Colin","Alvin"]
# for x,name in enumerate(names):
# 	sheet1.write(0, 2+x, name)
# for x,name in enumerate(itemList):
# 	sheet1.write(1+x, 0, name)
# for x,name in enumerate(priceList):
# 	sheet1.write(1+x, 1, name)	



# book.save("trial.xls")