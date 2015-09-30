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

def cadFetch():
    references = []
    xCoord = []
    yCoord = []
    rotation = []
    partType = []
    startSaving = False

    with open('009-00723-01C-top.csv', 'rb') as cadFile:
        reader = csv.reader(cadFile)
        devices = []
        device = []

        for row in reader:
            if row[0] == 'Name':
                startSaving = True
                continue
            if startSaving and (row[0] != '' and not 'H' in row[0]
            and not 'TP' in row[0]):
                device.append(['d', row[0].lower(), row[2], row[1], row[3]])
                devices.append(device)
            elif startSaving and (row[0] == ''):
                break
        return devices

def bomFetch():
    startSaving = False

    with open('086-00155-02.csv', 'rb') as bomFile:
        reader = csv.reader(bomFile)
        # devices = []
        # device = []

        for row in reader:
            if row[0] == 'Part No':
                startSaving = True
                continue
            if startSaving:
                print row[8]
        # return devices

def main():
    print bomFetch()

if __name__ == '__main__':
    main()