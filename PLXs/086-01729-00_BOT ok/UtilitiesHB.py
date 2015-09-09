#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MAT.TE
#
# Created:     28/08/2015
# Copyright:   (c) MAT.TE 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

def varInitializer():
    HEADER = ['P 1']
    BOARD_ORIGIN = [int(raw_input('Board Origin Xcoord: ')), int(raw_input('Board Origin Ycoord: '))]
    BOARD_WIDTH = ['w', unitsConverter(int(raw_input('Board Width: ')), True, BOARD_ORIGIN, False)]
    return HEADER, BOARD_ORIGIN, BOARD_WIDTH


def unitsConverter(mils, isBoardWidth, BOARD_ORIGIN, X_COORD):
    if isBoardWidth:
        # 1 Mil equals 25.4 Microns
        # Added a tolerance for board width
        return int(math.ceil(mils * 25.4))
    elif X_COORD:
        return int((mils + BOARD_ORIGIN[0]) * 25.4)
    else:
        return int((mils + BOARD_ORIGIN[1]) * -25.4)


def fileNamer():
    BOM_FILENAME = raw_input('Enter BOM filename: ').replace("\"","").replace(".csv", "")
    CAD_FILENAME = raw_input('Enter CAD filename: ').replace("\"","").replace(".xls", "")
    PLX_FILENAME = BOM_FILENAME

    return BOM_FILENAME, CAD_FILENAME, PLX_FILENAME


def deviceEnumerator(myString):
    if '-' in myString:
        strMod = myString.split('-')
        devRange = range(int(filter(lambda x: x.isdigit(), strMod[0])),
                         int(filter(lambda x: x.isdigit(), strMod[1]))+1)
        devType = filter(lambda x: x.isalpha(), strMod[0])
        return [devType + str(d) for d in devRange]
    else:
        return [myString.replace(' ','')]

def main():
    raw_input("Wrong file! Use plxHelper ")

if __name__ == '__main__':
    main()
