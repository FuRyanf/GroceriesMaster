from subprocess import call
import difflib
import xlwt
import re
# Things it doesn't cover:
# 1. coupons
# 2. tax
# 3. covers items up to 999.99
# run tesseract's OCR
# Only tested with costco reciepts
# assumptions and considerations:
# 1.binarisation gives more exact numbers
# 2.prioritize number accuracy over word accuracy, words just have to be decipherable
# 3.assumes that users look over spreadsheat generated

# border removal using numpy
# regex format \w\s*(\d+)\s*(.+)\s*(\d+\.\d+) try on the non converted

call(["tesseract", "c1.jpeg", "parsedNorm"])
# binarisation rotation using ImageMagick helps with getting exact numbers
# call(["convert", "-colorspace", "gray", "-colors", "2", "-normalize", "hand.png", "handconv.png"])
# call(["tesseract", "handconv.png", "parsedBin"])

# to extract only numbers, start from last element until first period

f=open('parsedBin.txt')
g=open('parsedNorm.txt')
#put this in a seperate method

def similar(seq1, seq2):
	return difflib.SequenceMatcher(a=seq1.lower(), b=seq2.lower()).ratio() > .6

def removeUselessLines(lines):
	parsingList = []
	for line in lines:
		#line = line.replace(" ","")
		line = line.strip()
		if str(line[-1:]) == '\n' and ('.' in line or '-' in line or '_' in line):
			parsingList.append(line[:-1])
			print line[:-1]
		elif ('.' in line or '-' in line or '_' in line):
			parsingList.append(line)
	return parsingList

# parsingListBin = removeUselessLines(f)
parsingListNorm = removeUselessLines(g)

# dictBin={}
# positionBin = 0
# for parse in parsingListBin:
# 	# make the first number optional.
# 	tempList=[s for s in re.findall(r'[0-9]?[0-9]?[0-9]?[\.\-][0-9]{1,2}', parse)]
# 	try:
# 		tempList[-1]=tempList[-1].replace("-",".")
# 		tempList[-1]=tempList[-1].replace("_",".")
# 		price=tempList[-1]
# 		dictBin[positionBin] = float(price)
# 		positionBin+=1
# 	except IndexError:
# 		print "not valid"

dictNorm={}
positionNorm = 0
prevDictKey=0
excludedlines=0

for parse in parsingListNorm:
	# make the first number optional.
	tempList=[s for s in re.findall(r'[0-9]?[0-9]?[0-9]?[\.\-][0-9]{1,2}', parse)]
	try:
		#in the case that it is a coupon
		if parse[-1] == '-' and len(tempList)!= 0 and ('C' in parse or 'P' in parse or 'N' in parse): 
			dictNorm[int(prevDictKey)][0]-=float(tempList[-1])
			print "Coupon used on: {0} for ${1}".format(dictNorm[int(prevDictKey)][1],str(float(tempList[-1])))
			continue
		tempList[-1]=tempList[-1].replace("-",".")
		tempList[-1]=tempList[-1].replace("_",".")
		price=tempList[-1]
		parse = parse[:len(parse)-len(tempList[-1])] # remove the price and everything after it from the line
		parse=filter(lambda x: x.isalpha(), parse)
		if parse[0] =='E':
			parse=parse[1:]
		if len(parse)<2:
			continue
		#in the case that it is SUBTOTAL or TAX
		grocItem = parse
		if similar("TAX", grocItem) or similar("SUBTOTAL",grocItem):
			continue
		dictNorm[positionNorm]=[float(price),grocItem]
		prevDictKey = positionNorm
		positionNorm+=1
	except IndexError:
		excludedlines+=1


# if last two SUBTOTAL and TAX Fuzzy matches
	
# print dictBin # form {position: price}
# print len(dictBin)
# print '\n'
# print '\n'
# print dictNorm # form {position: [price, item]}

# split listNorm into two lists, ones with similar, ones without factor distance between positions
# dictNormSame ={}
# dictNormConflict = {}
# for keyNorm, value in dictNorm.iteritems():
# 	if value[0] in dictBin.values(): # if price in dictNorm is in the prices in dictBin
# 		index = dictBin.keys()[dictBin.values().index(value[0])]#find key where value lies
# 		dictNormSame[keyNorm] = [dictBin.pop(index), value[1]]
# 	else:
# 		dictNormConflict[keyNorm]=value

# print '\n'
# print '\n'
# print "Same"
# print dictNormSame
# print '\n'
# print '\n'
# print "Different"
# print dictNormConflict
# print '\n'
# print '\n'
# print "Leftover"
# print dictBin
# print len(dictBin)
# print len(dictNormConflict)

# Algorithm for leftovers. Based on two criteria, similarity and position, pair up choose the smaller value
# in that case, those without pair remain itself.
# apply Levenshtein distance App


# print len(parsingList)



book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
names=["Andy","John","Ryan","Mathew","Evans","Tim"]
for x,name in enumerate(names):
	sheet1.write(0, 2+x, name)
for x,value in enumerate(dictNorm.values()):
	sheet1.write(1+x, 0, value[1])
	sheet1.write(1+x, 1, value[0])	
	



book.save("trial.xls")