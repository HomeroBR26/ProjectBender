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
from UtilitiesHB import *
import CSVReader

def plxGenerator(HEADER, BOARD_WIDTH, fiducials, devices, PLX_FILENAME):
    writableItems = [HEADER, BOARD_WIDTH]

    with open(PLX_FILENAME + '.plx', 'w+') as plxFile:
        for item in writableItems:
            textWriter(item, plxFile)
        for item in fiducials:
            textWriter(item, plxFile)
        for item in devices:
            textWriter(item, plxFile)

def textWriter(text, myFile):
    fileWriter = csv.writer(myFile, dialect='excel-tab')
    fileWriter.writerow(text)

def main():
    BOM_FILENAME, CAD_FILENAME, PLX_FILENAME = fileNamer();
    HEADER, BOARD_ORIGIN, BOARD_WIDTH = varInitializer()
    fiducials, components = CSVReader.cadFetch(BOARD_ORIGIN, CAD_FILENAME)
    devices = CSVReader.bomFetch(components, BOM_FILENAME)
    plxGenerator(HEADER, BOARD_WIDTH, fiducials, devices, PLX_FILENAME)

    raw_input('.plx File created! ')

if __name__ == '__main__':
    main()