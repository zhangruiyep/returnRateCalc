import csv
import record
import datetime

def readFile(filename):
	accAll = []
	f = open(filename, "rb")
	rdr = csv.reader(f)
	for row in rdr:
		#print row
		name = row[0]
		tradCount = row[1]
		tradDate = row[2]
		curCount = row[3]
		curDate = row[4]
		#print name, tradCount, tradDate, curCount, curDate
		a = record.findInList(name, accAll)
		if a == "":
			a = record.acc(name)
			accAll.append(a)

		if tradCount != "":
			#it is a trad record
			d = tradDate.split("-")
			date = datetime.date(int(d[0]), int(d[1]), int(d[2]))
			r = record.tradRecord(float(tradCount), date)
			a.trad(r)
		if curCount != "":
			#set cur
			d = curDate.split("-")
			date = datetime.date(int(d[0]), int(d[1]), int(d[2]))
			a.setCur(float(curCount), date)
	
	f.close()
	return accAll

def writeFile(acclist, filename):
	row = []
	f = open(filename, "wb")
	wtr = csv.writer(f)
	for a in acclist:
		row.append(a.name)
		row.append(a.getYearRetRate())
		wtr.writerow(row)
		row = []
	
	f.close()
