#-------------------------------------------------------------------------------
# Name:        plxHelper
# Purpose:     Main module. Creates the structure of the plx file
#              and writes the data to a new file.
#
# Author:      Homero Benavides
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
    """Create a PLX file and write all the information to it.

    HEADER -- header of the PLX file
    BOARD_WIDTH -- width of the current board
    fiducials -- list containing all fiducials and their information
    devices -- list containing all devices and their information
    PLX_FILENAME -- name that is going to be asigned to the file
    """
    writableItems = [HEADER, BOARD_WIDTH]

    with open(PLX_FILENAME + '.plx', 'w+') as plxFile:
        for item in writableItems:
            textWriter(item, plxFile)
        for item in fiducials:
            textWriter(item, plxFile)
        for item in devices:
            textWriter(item, plxFile)

def textWriter(text, myFile):
    """Write information in a tab-delimited format to given file."""
    fileWriter = csv.writer(myFile, dialect='excel-tab')
    fileWriter.writerow(text)

def main():
    """Execute main program."""
    while True:
        try:
            BOM_FILENAME, CAD_FILENAME, PLX_FILENAME = fileNamer();
            HEADER, BOARD_ORIGIN, BOARD_WIDTH = varInitializer()
            fiducials, components = CSVReader.cadFetch(BOARD_ORIGIN,
                                                       CAD_FILENAME)
            devices = CSVReader.bomFetch(components, BOM_FILENAME)
            plxGenerator(HEADER, BOARD_WIDTH, fiducials, devices, PLX_FILENAME)
            break
        except IOError:
            print '\nERROR 002. Archivo no encontrado. La direccion puede '+\
            'ser incorrecta\no la extension diferente a .csv\n'

    raw_input('\nEl archivo .plx ha sido creado exitosamente! ASEGURESE DE'+\
              ' QUE EL NOMBRE\nDEL ARCHIVO SEA IGUAL AL DEL BOM')

if __name__ == '__main__':
    main()