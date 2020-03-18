import csv 
from decimal import *

filename = "mls_analysis.csv"

getcontext().prec = 3

fields = [] 
rows = [] 

teams = {}

wlt = {}
wltPts = {}
wltTotal = {}
wltDifference = {}

adjGoals = {}
adjGoalsPts = {}
adjGoalsTotal = {}
adjGoalsDifference = {}

shotXg = {}
shotXgPts = {}
shotXgTotal = {}
shotXgDifference = {}

nonshotXg = {}
nonshotXgPts = {}
nonshotXgTotal = {}
nonshotXgDifference = {}

optaXg = {}
optaXgPts = {}
optaXgTotal = {}
optaXgDifference = {}

xgt = {}
xgtPts = {}
xgtTotal = {}
xgtDifference = {}

xgp = {}
xgpPts = {}
xgpTotal = {}
xgpDifference = {}

fbrefXg = {}
fbrefXgPts = {}
fbrefXgTotal = {}
fbrefXgDifference = {}


xPts = {}

def addToRecord(row, records, points, total, difference, homeScoreCol, awayScoreCol):
    if(row[2] in total):
        total[row[2]] = total[row[2]]+Decimal(row[homeScoreCol])
        difference[row[2]] = difference[row[2]]+(Decimal(row[homeScoreCol])-Decimal(row[awayScoreCol]))
    else:
        total[row[2]] = Decimal(row[homeScoreCol])
        difference[row[2]] = (Decimal(row[homeScoreCol])-Decimal(row[awayScoreCol]))
    if(row[3] in total):
        total[row[3]] = total[row[3]]+Decimal(row[awayScoreCol])
        difference[row[3]] = difference[row[3]]+(Decimal(row[awayScoreCol])-Decimal(row[homeScoreCol]))
    else:
        total[row[3]] = Decimal(row[awayScoreCol])
        difference[row[3]] = (Decimal(row[awayScoreCol])-Decimal(row[homeScoreCol]))
    if (row[homeScoreCol] > row[awayScoreCol]):
        if (row[2] in records):
            points[row[2]] = points[row[2]]+3
            records[row[2]] = [records[row[2]][0]+1,records[row[2]][1],records[row[2]][2]]
        else:
            points[row[2]] = 3
            records[row[2]] = [1,0,0]
        if (row[3] in records):
            records[row[3]] = [records[row[3]][0],records[row[3]][1]+1,records[row[3]][2]]
        else:
            points[row[3]] = 0
            records[row[3]] = [0,1,0]
    if (row[awayScoreCol] > row[homeScoreCol]):
        if (row[2] in records):
            records[row[2]] = [records[row[2]][0],records[row[2]][1]+1,records[row[2]][2]]
        else:
            points[row[2]] = 0
            records[row[2]] = [0,1,0]
        if (row[3] in records):
            points[row[3]] = points[row[3]]+3
            records[row[3]] = [records[row[3]][0]+1,records[row[3]][1],records[row[3]][2]]
        else:
            points[row[3]] = 3
            records[row[3]] = [1,0,0]
    if (row[homeScoreCol] == row[awayScoreCol]):
        if (row[2] in records):
            points[row[2]] = points[row[2]]+1
            records[row[2]] = [records[row[2]][0],records[row[2]][1],records[row[2]][2]+1]
        else:
            points[row[2]] = 1
            records[row[2]] = [0,0,1]
        if (row[3] in records):
            points[row[3]] = points[row[3]]+1
            records[row[3]] = [records[row[3]][0],records[row[3]][1],records[row[3]][2]+1]
        else:
            points[row[3]] = 1
            records[row[3]] = [0,0,1]
  
def addXPts(row, points, homeScoreCol, awayScoreCol):
    if (row[2] in points):
        points[row[2]] = points[row[2]]+Decimal(row[homeScoreCol])
    else:
        points[row[2]] = Decimal(row[homeScoreCol])
        teams[row[2]] = []
    if (row[3] in points):
        points[row[3]] = points[row[3]]+Decimal(row[awayScoreCol])
    else:
        points[row[3]] = Decimal(row[awayScoreCol])
        teams[row[3]] = []

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
    fields = csvreader.next() 
  
    for row in csvreader: 
        rows.append(row) 

        addToRecord(row,wlt,wltPts,wltTotal,wltDifference,4,5)
        addToRecord(row,adjGoals,adjGoalsPts,adjGoalsTotal,adjGoalsDifference,6,7)
        addToRecord(row,shotXg,shotXgPts,shotXgTotal,shotXgDifference,8,9)
        addToRecord(row,nonshotXg,nonshotXgPts,nonshotXgTotal,nonshotXgDifference,10,11)
        addToRecord(row,optaXg,optaXgPts,optaXgTotal,optaXgDifference,12,13)
        addToRecord(row,xgt,xgtPts,xgtTotal,xgtDifference,18,19)
        addToRecord(row,xgp,xgpPts,xgpTotal,xgpDifference,20,21)
        addToRecord(row,fbrefXg,fbrefXgPts,fbrefXgTotal,fbrefXgDifference,24,25)

        addXPts(row,xPts,22,23)

    for key in teams.keys():
        teams[key] = [
            wlt[key],
            wltPts[key],
            wltTotal[key],
            wltDifference[key],
            adjGoals[key],
            adjGoalsPts[key],
            adjGoalsTotal[key],
            adjGoalsDifference[key],
            shotXg[key],
            shotXgPts[key],
            shotXgTotal[key],
            shotXgDifference[key],
            nonshotXg[key],
            nonshotXgPts[key],
            nonshotXgTotal[key],
            nonshotXgDifference[key],
            optaXg[key],
            optaXgPts[key],
            optaXgTotal[key],
            optaXgDifference[key],
            xgt[key],
            xgtPts[key],
            xgtTotal[key],
            xgtDifference[key],
            xgp[key],
            xgpPts[key],
            xgpTotal[key],
            xgpDifference[key],
            fbrefXg[key],
            fbrefXgPts[key],
            fbrefXgTotal[key],
            fbrefXgDifference[key],
            xPts[key]
        ]

    print(teams)

output = "mls_analysis_calc.csv"

outfields = [
"Team",
"wlt",
"wltPts",
"wltTotal",
"wltDifference",
"adjGoals",
"adjGoalsPts",
"adjGoalsTotal",
"adjGoalsDifference",
"shotXg",
"shotXgPts",
"shotXgTotal",
"shotXgDifference",
"nonshotXg",
"nonshotXgPts",
"nonshotXgTotal",
"nonshotXgDifference",
"optaXg",
"optaXgPts",
"optaXgTotal",
"optaXgDifference",
"xgt",
"xgtPts",
"xgtTotal",
"xgtDifference",
"xgp",
"xgpPts",
"xgpTotal",
"xgpDifference",
"fbrefXg",
"fbrefXgPts",
"fbrefXgTotal",
"fbrefXgDifference",
"xPts"
]

with open(output, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(outfields) 
      
    for k,v in teams.items():
        v.insert(0,k)
        csvwriter.writerow(v)
  
