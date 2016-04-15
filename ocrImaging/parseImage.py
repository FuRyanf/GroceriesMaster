from subprocess import call
import xlwt
import re
# run tesseract's OCR
# Only tested with costco reciepts
# assumptions and considerations:
# 1.binarisation gives more exact numbers
# 2.prioritize number accuracy over word accuracy, words just have to be decipherable
# 3.assumes that users look over spreadsheat generated

# border removal using numpy
# regex format \w\s*(\d+)\s*(.+)\s*(\d+\.\d+) try on the non converted

# call(["tesseract", "reciept3.png", "parsedNorm"])
# binarisation rotation using ImageMagick helps with getting exact numbers
# call(["convert", "-colorspace", "gray", "-colors", "2", "-normalize", "reciept3.png", "reciept3conv.png"])
# call(["tesseract", "reciept3conv.png", "parsedBin"])

# to extract only numbers, start from last element until first period

f=open('parsedBin.txt')
g=open('parsedNorm.txt')
#put this in a seperate method



def removeUselessLines(lines):
	parsingList = []
	for line in lines:
		line = line.replace(" ","")
		line = line.strip()
		if str(line[-1:]) == '\n' and ('.' in line or '-' in line):
			parsingList.append(line[:-1])
			print line[:-1]
		elif '.' in line:
			parsingList.append(line)
	return parsingList

parsingListBin = removeUselessLines(f)
parsingListNorm = removeUselessLines(g)

listBin=[]
countBin = 0
for parse in parsingListBin:
	#make the first number optional.
	tempList=[s for s in re.findall(r'[0-9]?[0-9]?[0-9]?[0-9]?[\.\-][0-9]{1,2}', parse)]
	try:
		#underscore?
		tempList[-1]=tempList[-1].replace("-",".")
		tempList[-1]=tempList[-1].replace("_",".")
		listBin.append(tempList[-1])
		countBin+=1
	except IndexError:
		print "not valid"

listNorm=[]
countNorm = 0
for parse in parsingListNorm:
	#make the first number optional.
	tempList=[s for s in re.findall(r'[0-9]?[0-9]?[0-9]?[0-9]?[\.\-][0-9]{1,2}', parse)]
	try:
		tupl = ()
		tempList[-1]=tempList[-1].replace("-",".")
		tempList[-1]=tempList[-1].replace("_",".")
		listNorm.append(tempList[-1])
		parse = parse[:len(parse)-len(tempList[-1])] #remove the price and everything after it from the line
		countNorm+=1
	except IndexError:
		print "not valid"

	
print listBin
print listNorm





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