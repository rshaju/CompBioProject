import os
import numpy as np
from csv import reader
filepath = '/Users/Rahul/Desktop/'
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
    tableAXY = np.delete(table, np.s_[4:8], 1) #delete 2-7
    #print headerAXY
    return tableAXY
    #print tableAXY #table includes: cell, area, x, y

def InsertZ(pt, zt): #will add the Z to the P
    row = 0
    i=0
    for cs in zt:
        if cs[1] > 0:
            cc = cs[1]
            csn = cs[0]
            while i < cc: #add csn to as many cc lines 
                np.put (pt[row], 3, csn)
                i +=1
                row = row + 1
            i = 0
    return pt

def AddBinaryKey (nt):
    for line in range(len(nt)):
        np.put(nt[line], 2, 0)
    return nt


ParsedTable = ReadIntoTable('Results.txt')
z = Ztable ('ZtableResults.txt')
print z #prints the ztable
#print ParsedTable #prints the parsed results table
newtable = InsertZ (ParsedTable, z)
newtable = AddBinaryKey(newtable)
print newtable


def CountFunction(nt):
    cellcount = 0
    flag = 0
    for item1 in nt:
        tempX = item1[4]
        tempY = item1[5]
        tempZ = item1[3]
        for item2 in nt:
            if item2[2] == 0:
                if item2[3] == tempZ + 1:
                    tempZ += 1
                    CompareX = abs(item2[4] - tempX)
                    CompareY = abs(item2[5] - tempY)
                    if 0 <= CompareX or CompareY <= 7:
                        item2[2] == 1
                    flag += 1
    cellcount += 1
    return cellcount

print CountFunction(newtable)
             
        
    
    


