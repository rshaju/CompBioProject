import os
import numpy as np
from csv import reader
import math
filepath = '/Users/Salma/Desktop/'
os.chdir(filepath)

def Ztable (zfile): #function to read in Z file
    csv_reader = reader(open(zfile,'r'), quotechar = "\"") #Read in the file
    i = 0 #index beginning
    Zlist = [] #The list we want to return
    for row in csv_reader: #lets go through this
        i=i+1 #move up the index
        zlist = [] #the list to add to master Z
        for string in row:
            string = string.split('\t') #split it
            zslice = i #the cross section
            cellcount = string[1] #cell count is the 1st element of string
            cellcount = int(cellcount) #convert to integer
            zlist.append(zslice) #add cross section to zlist
            zlist.append(cellcount) #add cell count to zlist
            Zlist.append(zlist) #add new list to list holding all cs & cc
    Zlist = np.array(Zlist) #convert & return as numpy array
    return Zlist


def ReadIntoTable(resultsfile): #function to read Restuls into table
    f = open (resultsfile) #opens the results file
    headers = f.readline() #read the headers, if we need this later, we can use it
    headers = headers.strip().split()
    headerAXY = ['Cell',headers[0],headers[7],headers[8]] #keep header labels
    table = np.loadtxt(resultsfile, skiprows=1) #read table as numpy array
    tableAXY = np.delete(table, np.s_[4:8], 1) #delete 4-7, keep 2&3 to overwrite later
    return tableAXY
    #print tableAXY #table includes: cell, area, x, y #debugging

def InsertZ(pt, zt): #will add the Z to the Parsed results table
    row = 0 #keeps track of the row we are on
    i=0 #increments to meet cell count number
    for cs in zt: #go through cross sections from the Ztable
        if cs[1] > 0: #if the 1st index contains a cell count (more than 0)
            cc = cs[1] #set cell count equal to the 1st index of the cell count
            csn = cs[0] #set the cross section number equal to the 0th index
            while i < cc: #add csn to as many cell count lines
                np.put (pt[row], 3, csn) #replace the 3rd index of the Parsed table with cross section
                i +=1 #increment to indicate you added
                row = row + 1 #increment to continue to track row
            i = 0 #after adding to the number of cell count lines, set i to zero
    return pt #return the edited parsed table

def AddBinaryKey (nt): #function takes in the newly edited parsed table to add key
    for line in range(len(nt)): #go through line for the length of the new table
        np.put(nt[line], 2, 0) #replace the 2nd index with a 0
    return nt #return the edited table again

def SingleCellCountFunction(nt, avg_area):
    cellcount = 0
    list1 = []
    flag = 0
    for item1 in nt:
        if item1[2] == 0:
            flag = BlobTracker(item1[1], avg_area)
            print flag, item1[1]
            tempX = item1[4]
            tempY = item1[5]
            tempZ = item1[3]
            if flag < 1: #change only individual cells
                np.put(item1, 2, 1)
                cellcount += 1
                #cellcount = cellcount + flag
            if item1[1] > avg_area:
                list1.append(item1)
            for item2 in nt:
                if item2[2] == 0 and flag <= 1: # lets only filter our individual cells, no blobs
                    if item2[3] == tempZ + 1:
                        tempZ += 1
                        CompareX = abs(item2[4] - tempX)
                        CompareY = abs(item2[5] - tempY)
                        if 0 <= (CompareX or CompareY)  <= 7:
                            np.put(item2, 2, 1)
    return cellcount + 1


def AreaCheck (nt): #Will create
    size_list = []
    for item in nt:
        temp = item[1]
        size_list.append(temp)
    return size_list

def SortandSpit (st, th):
    flag = 0
    total = 0.0
    for item in st:
        if item < th*2:
            total = total + item
            flag = flag + 1
    total = total/flag
    return total
    #return total
    #Sort size_list by size
    #Return Average cell size(median value)
    #return 66.249

def BlobTracker (blob, avg_area):
    cellcount = blob/avg_area
    cellcount = math.floor(cellcount)
    return cellcount

size_threshold = 50.87
ParsedTable = ReadIntoTable('Results_table.txt')
z = Ztable ('z_table.txt')
#print z #prints the ztable
#print ParsedTable #prints the parsed results table
newtable = InsertZ (ParsedTable, z)
newtable = AddBinaryKey(newtable)

size_list = AreaCheck(newtable)
avg_area = SortandSpit(size_list, size_threshold)

print newtable
print SingleCellCountFunction(newtable, avg_area)
print newtable

