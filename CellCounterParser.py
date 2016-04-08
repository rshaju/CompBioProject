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
            cellcount = int(cellcount) #hopefully this works
            zlist.append(zslice)
            zlist.append(cellcount)
            Zlist.append(zlist)
    Zlist = np.array(Zlist) #return as numpy array
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
    #print headerAXY
    return tableAXY
    #print tableAXY #table includes: cell, area, x, y

ParsedTable = ReadIntoTable('Results.txt')
z = Ztable ('ZtableResults.txt')
print z

##def InsertZ (ptable, ZTABLE):
##    i = 0 #follow length of ztable
##    j = 0 #follow parser table
##    lengthZ = len(ZTABLE)


##def insertZ (potato, zoo):
##    i = 0 #follow length of zoo, and CS
##    flag = 0 #keep up with the Parser table. and CC
##    lengthZ = len(zoo) #final length of the z table
##    temp_info_holder = [] #stores XY
##    Pillow = [] #final list of updated info holding XYZ
##    for num in zoo: #iterate through Z, get the cell counts per cross section
##        while i < lengthZ: 
##            item = zoo[i] #the element holding CS and CC
##            item = item[1] #item has become the cell count
##            if item > 0: #if there is a cell
##                for order in range(item):
##                    temp = (potato[flag])
##                    temp.append(i + 1)
##                    Pillow.append(temp)
##                    #print(potato[flag])#.append(i) #the cell info
##                    print(i + 1) #the CS
##                    flag = flag + 1 #move up to next CC
##            #print(item)
##            i = i + 1
##    
##            
##    return 4
##
##hi = insertZ (ParsedTable, z)

#print z
print ParsedTable
##print hi


##def CompareCells(editedtable): #take in the edited table array
##    for row in 

##class CellCounter (editedtable):
##    for row in table:
##        Cellnumber = row[0]
##        Area = row[1]
##        Xstart = row[2]
##        Ystart = row[3]
##    
