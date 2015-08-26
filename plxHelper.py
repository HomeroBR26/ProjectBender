#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MAT.TE
#
# Created:     20/08/2015
# Copyright:   (c) MAT.TE 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv
import math

def columnFinder(colToFind):
    pass

def rowFinder(rowToFind):
    pass

def plxGenerator():
    HEADER = ['P', '1']
    boardWidth = ['w', int(math.ceil(int(raw_input('Board Width:')) * 25.4/100)*100)+300]  # 1 Mil equals 25.4 Microns
    fiducial1 = ['f', raw_input('Fiducial 1 Xcoord:'), raw_input('Fiducial 1 Ycoord:')]
    fiducial2 = ['f', raw_input('Fiducial 2 Xcoord:'), raw_input('Fiducial 2 Ycoord:')]
    writableItems = [HEADER, boardWidth, fiducial1, fiducial2]

    with open('myPLXfile.txt', 'w+') as plxFile:
        for item in writableItems:
            textWriter(item, plxFile)

def textWriter(text, myFile):
    fileWriter = csv.writer(myFile, dialect='excel-tab')
    fileWriter.writerow(text)


def main():
    plxGenerator()

if __name__ == '__main__':
    main()