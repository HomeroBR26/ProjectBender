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
    BOARD_WIDTH = ['w', unitsConverter(int(raw_input('Board Width: ')), True, BOARD_ORIGIN)]
    return HEADER, BOARD_ORIGIN, BOARD_WIDTH

def unitsConverter(mils, isBoardWidth, BOARD_ORIGIN):
    if isBoardWidth:
        # 1 Mil equals 25.4 Microns
        # Added a tolerance for board width
        return int(math.ceil(mils * 25.4/100)*100)+300
    else:
        return int((mils + BOARD_ORIGIN[0]) * 25.4)

def main():
    raw_input("Wrong file! Use plxHelper ")

if __name__ == '__main__':
    main()
