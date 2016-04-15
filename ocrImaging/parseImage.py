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
		if str(line[-1:]) == '\n' and ('.' in line or '-' in line or '_' in line):
			parsingList.append(line[:-1])
			print line[:-1]
		elif ('.' in line or '-' in line or '_' in line):
			parsingList.append(line)
	return parsingList

parsingListBin = removeUselessLines(f)
parsingListNorm = removeUselessLines(g)

listBin={}
positionBin = 0
for parse in parsingListBin:
	# make the first number optional.
	tempList=[s for s in re.findall(r'[0-9]?[0-9]?[0-9]?[0-9]?[\.\-][0-9]{1,2}', parse)]
	try:
		tempList[-1]=tempList[-1].replace("-",".")
		tempList[-1]=tempList[-1].replace("_",".")
		price=tempList[-1]
		listBin[positionBin] = [price]
		positionBin+=1
	except IndexError:
		print "not valid"

listNorm={}
positionNorm = 0
for parse in parsingListNorm:
	# make the first number optional.
	tempList=[s for s in re.findall(r'[0-9]?[0-9]?[0-9]?[0-9]?[\.\-][0-9]{1,2}', parse)]
	try:
		tempList[-1]=tempList[-1].replace("-",".")
		tempList[-1]=tempList[-1].replace("_",".")
		price=tempList[-1]
		parse = parse[:len(parse)-len(tempList[-1])] # remove the price and everything after it from the line
		parse=filter(lambda x: x.isalpha(), parse)
		if parse[0] =='E':
			parse=parse[1:]
		if len(parse)<2:
			continue
		grocItem = parse
		listNorm[positionNorm]=[price,grocItem]
		positionNorm+=1
	except IndexError:
		print "not valid"

	
print listBin # form (price, position)
print '\n'
print '\n'
print listNorm # form (price, item name, position)

# split listNorm into two lists, ones with similar, ones without factor distance between positions
# listNormSame =[]
# listNormConflict = []
# for tupl in listNorm:
# 	for price in listBin:
# 		if tupl[0] in price: # check if the price is in list of prices
# 			listNormSame.append(tupl)
# 			[]
# 		else:
# 			listNormConflict

# print listNormSame
# print listNormConflict

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