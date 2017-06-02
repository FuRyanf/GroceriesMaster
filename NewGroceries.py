#! /usr/bin/env python2.7
#Ryan Fu 2015
from xlrd import open_workbook
import sys
excelFile = 'groceries.xls'
print excelFile

xls = open_workbook(excelFile)
for sheets in xls.sheets():
    lists = [[] for _ in xrange(100)]
    counter = 0
    for row in range(sheets.nrows):
        for col in range(sheets.ncols):
        	if sheets.cell(row,col).value == '':
        		lists[counter].append('o')
        	else:
        		lists[counter].append(str(sheets.cell(row,col).value))
    	counter += 1
lists = filter(lambda a:a!=[],lists)
for count, i in enumerate(lists):
	lists[count] = filter(lambda a:a != '',i)

#print lists
xolist = []
for i in lists:
	xolist.append(i[2:])
#print xolist

lists[0] = ' '.join(lists[0])
	
names = lists.pop(0).split()
#attaches a sum of zero

for counter, name in enumerate(names):
	names[counter] = [name,0]
names = names[2:]
#print names
prices = []
#print lists
for counter, array in enumerate(lists):
	try:
		prices.append(float(array[1])/(array.count('o')))
	except ZeroDivisionError:
		prices.append(float('0'))
		print 'everyone excluded price for {0} : ${1}'.format(array[0],array[1]) 
	
#print prices

for counter, array in enumerate(lists):
	for counter2, name in enumerate(names):
		if array[counter2+2] == 'o':
			name[1] += prices[counter]
total = 0
for name in names:
	print '{0}, total: ${1} '.format(name[0], round(name[1]*100)/100)
	total += round(name[1]*100)/100
print 'total: $', total
