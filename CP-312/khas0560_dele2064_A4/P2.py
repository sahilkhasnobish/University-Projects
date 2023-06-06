"""
------------------------------------------------------------
Program will read input file passing an argument to the 
program and output to question will be written on the 
console screen 
------------------------------------------------------------
Author: Sahil Khasnobish
        Emily De Leon
ID: 190990560
    129012064
Email: khas0560@mylaurier.ca
        dele2064@mylaurier.ca
__updated__ = "2022-03-04"
------------------------------------------------------------
"""
import sys

input_file = open(sys.argv[1], 'r') #this called to open the input file
packSize = []
m = 0

def fileInput(input_file): #initializes file read method
   
    packSizeStr = input_file.readline().strip()
    packSize = packSizeStr.split(",")
    
    m = input_file.readline()
    int(m)
    
    return(packSize, m)

packSize, m = fileInput(input_file)


def packMin(packSize, m): #initializes min packaging method
    if m == None:
        return -1
    if packSize == None:
        return -1
    
    packNum = 0
    sizePack = 0
    packAvail = False
    
    for i in packSize:
        
        mDiv = int(m) % int(i)
        
        if mDiv == 0:
            if int(i) > sizePack:
                sizePack = int(i)
                packAvail = True
    if packAvail:
        packNum = int(m) // sizePack
    else:
        packNum = -1 #means no available product to fit m size
    
    return packNum, sizePack

packNum, sizePack = packMin(packSize, m)
    
print(packNum) #prints value size used 

if packNum == - 1: 
    print("There is no solution.")
else:
    print(packNum, " Packages of size ", sizePack)