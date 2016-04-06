import os
import numpy as np
from csv import reader
filepath = '/Users/yatri/Desktop/'
os.chdir(filepath)

def Ztable (zfile): #function to read in Z file
    csv_reader = reader(open(zfile,'r'), quotechar = "\"")
    i = 0
    Zlist = []
    for row in csv_reader:
        i=i+1
        zlist = []
        for string in row:
            string = string.split('\t')
            zslice = i
            cellcount = string[1]
            zlist.append(zslice)
            zlist.append(cellcount)
            Zlist.append(zlist)
    return Zlist
            
    
def ReadIntoTable(resultsfile): #function to read Restuls into table
    f = open (resultsfile) #opens the results file
    headers = f.readline()
    headers = headers.strip().split()
    headerAXY = ['Cell',headers[0],headers[7],headers[8]]
    table = np.loadtxt(resultsfile, skiprows=1)
    #Table: [0] = cell; [1] = area [2-7; don't want]
    #[8] = Xcoordinate [9] = Ycoordinate
    tableAXY = np.delete(table, np.s_[2:8], 1) #delete 2-7
    print headerAXY
    return tableAXY
    #print tableAXY #table includes: cell, area, x, y

ParsedTable = ReadIntoTable('Results.txt')
z = Ztable ('ZtableResults.txt')
print z
print ParsedTable


##def CompareCells(editedtable): #take in the edited table array
##    for row in 

##class CellCounter (editedtable):
##    for row in table:
##        Cellnumber = row[0]
##        Area = row[1]
##        Xstart = row[2]
##        Ystart = row[3]
##    
