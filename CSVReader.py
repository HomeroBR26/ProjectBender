#-------------------------------------------------------------------------------
# Name:        CSVReader
# Purpose:     Contanis methods to go and fetch information from CAD and BOM
#              files.
#
# Author:      Homero Benavides
#
# Created:     20/08/2015
# Copyright:   (c) MAT.TE 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv
from UtilitiesHB import *

def cadFetch(BOARD_ORIGIN, CAD_FILENAME):
    """Read and save all useful information from CAD file.

    BOARD_ORIGIN -- offset used for this board
    CAD_FILENAME -- CAD file's path
    """
    startSaving = False

    with open(CAD_FILENAME + '.csv', 'rb') as cadFile:
        reader = csv.reader(cadFile)
        fiducials = []
        devices = []

        for row in reader:

            if row[0] == 'Name':
                startSaving = True
                continue

            if startSaving and (row[0] != '' and not 'H' in row[0]
                and not 'TP' in row[0] and not 'F' in row[0]
                and not 'N' in row[0] and not 'P' in row[0]
                and not 'K' in row[0] and not 'LED' in row[0]
                and not 'MOV' in row[0] and not 'E' in row[0]):
                #Since none of the previous char appear in row, execute:
                devices.append(['d', unitsConverter(int(row[2]), False,
                                BOARD_ORIGIN, False), unitsConverter(int\
                                (row[1]), False, BOARD_ORIGIN, True),
                                row[0].lower(), 'n0000', row[3], 'partNo',
                                'f-1', row[0].lower(), 'SHAPE'])

            elif startSaving and 'F' in row[0]:
                fiducials.append(['f', unitsConverter(int(row[2]), False,
                                  BOARD_ORIGIN, False), unitsConverter(int\
                                  (row[1]), False, BOARD_ORIGIN, True)])

            elif startSaving and (row[0] == ''):
                break

        return fiducials, devices

def bomFetch(devices, BOM_FILENAME):
    """Read and save all useful information from BOM file.

    devices -- list containing all devices and their information
    BOM_FILENAME -- BOM file's path
    """
    startSaving = False

    with open(BOM_FILENAME + '.csv', 'rb') as bomFile:
        reader = csv.reader(bomFile)

        for row in reader:
            currentDevices = []
            for elem in row[8].split(','):
                currentDevices.extend(deviceEnumerator(elem))

            if row[0] == 'Part No':
                startSaving = True
                continue

            if startSaving and row[8] != '':
                for elem in currentDevices:
                    for component in devices:
                        if elem.lower() == component[3]:
                            component[6] = row[4]



        return sorted(devices, key= lambda x: int(x[2]))

def main():
    """Print a message with an error description."""
    raw_input("ERROR 004. Wrong file! Use plxHelper.py ")

if __name__ == '__main__':
    main()