from subprocess import call
import xlwt
#run tesseract's OCR
#ONLY FOR COSTCO formmat
def charIsNumber(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

call(["tesseract", "reciept2.png", "parsed"])
f=open('parsed.txt')

itemList=[]
priceList=[]
parsingList = []
for line in f:
	if str(line[-1:]) == '\n':
		parsingList.append(line[:-1])
		print line[:-1]
	else:
		parsingList.append(line)
		print line


#If item is not equal to E then gg
#additionally can implement regex
numbers=['1','2','3','4','5','6','7','8','9','0','.']
numbers2=['1','2','3','4','5','6','7','8','9','0']
mistake=[',','_','-']
mistakeNum=['g']
count = 0
while count < len(parsingList):
	if parsingList[count]=='' or parsingList[count][0] != 'E' or parsingList[count][0] not in numbers:
		parsingList.pop(count)
	else:
		count+=1
for element in parsingList:
	count = 1
	word =""
	while count < len(element) and element[count] in numbers or element[count]==' ':
		count+=1

	# print count
	while count < len(element) and element[count] not in numbers2:
		word+=element[count]
		count+=1

	price =""
	while count < len(element):
		if element[count] in mistake:
			price+='.'
		elif element[count] in mistakeNum:
			price+='9'
		elif element[count] in numbers:
			price+=element[count]
		elif element[count] == ' ':
			print ""
		else:
			break
		count+=1
	print price
	print word
	itemList.append(word)
	priceList.append(price)
	# try: 
 #    	priceList.append(float(price))
 #    	break
 #    except:
 #        priceList.append(price)


print parsingList
print len(parsingList)



book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
names=["Ryan","Leonard","Alex","Henry","Colin","Alvin"]
for x,name in enumerate(names):
	sheet1.write(0, 2+x, name)
for x,name in enumerate(itemList):
	sheet1.write(1+x, 0, name)
for x,name in enumerate(priceList):
	sheet1.write(1+x, 1, name)	



book.save("trial.xls")