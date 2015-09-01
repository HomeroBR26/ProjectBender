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
from UtilitiesHB import *

def cadFetch(BOARD_ORIGIN):
    references = []
    xCoord = []
    yCoord = []
    rotation = []
    partType = []
    startSaving = False

    with open('009-00723-01C-top.csv', 'rb') as cadFile:
        reader = csv.reader(cadFile)
        fiducials = []
        devices = []
        device = []

        for row in reader:
            if row[0] == 'Name':
                startSaving = True
                continue
            if startSaving and (row[0] != '' and not 'H' in row[0]
            and not 'TP' in row[0] and not 'F' in row[0]):
                device = ['d', unitsConverter(int(row[2]), False, BOARD_ORIGIN, False),
                unitsConverter(int(row[1]), False, BOARD_ORIGIN, True), row[0].lower(), 'n0000', row[3],
                'partNo', 'f-1', row[0].lower(), 'SHAPE']
                devices.append(device)
            elif startSaving and 'F' in row[0]:
                if 'GLOBOL' in row[5]:
                    fiducials.append(['f', unitsConverter(int(row[2]), False, BOARD_ORIGIN, False),
                    unitsConverter(int(row[1]), False, BOARD_ORIGIN, True)])
            elif startSaving and (row[0] == ''):
                break
        return fiducials, devices

def bomFetch(devices):
    startSaving = False

    with open('086-00155-02.csv', 'rb') as bomFile:
        reader = csv.reader(bomFile)
        # device = []

        for row in reader:
            if row[0] == 'Part No':
                startSaving = True
                continue
            if startSaving and row[8] != '':
                for elem in row[8].split(','):
                    for component in devices:
                        if elem.lower() == component[3]:
                            component[6] = row[4]

        return sorted(devices, key= lambda x: int(x[2]))

def main():
    cadFetch([200, 200])
    # raw_input("Wrong file! Use plxHelper ")

if __name__ == '__main__':
    main()