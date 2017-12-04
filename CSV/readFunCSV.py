import csv
 
def readMyFile(filename):
    dates = []
    scores = []
 
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            dates.append(row[0])
            scores.append(row[1])
 
    return dates, scores
 
 
dates,scores = readMyFile('sample.csv')
 
print(dates)
print(scores)