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
    HEADER = ['P 1']
    BOARD_ORIGIN = [int(raw_input('Board Xcoord:')), int(raw_input('Board Ycoord:'))]
    BOARD_WIDTH = ['w', unitsConverter(int(raw_input('Board Width:')), False, BOARD_ORIGIN)]
    writableItems = [HEADER, BOARD_WIDTH]

    with open('myPLXfile.txt', 'w+') as plxFile:
        for item in writableItems:
            textWriter(item, plxFile)

def textWriter(text, myFile):
    fileWriter = csv.writer(myFile, dialect='excel-tab')
    fileWriter.writerow(text)

def unitsConverter(mils, isBoardWidth, BOARD_ORIGIN):
    if isBoardWidth:
        # 1 Mil equals 25.4 Microns
        # Added a tolerance for board width
        return int(math.ceil(mils * 25.4/100)*100)+300
    else:
        return int((mils + BOARD_ORIGIN[0]) * 25.4)

def main():
    matrixGenerator()
    plxGenerator()

if __name__ == '__main__':
    main()