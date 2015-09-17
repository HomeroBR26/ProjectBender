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
    """Initialice variables with constant values according to user input."""
    HEADER = ['P 1']
    print "\nPuede obtener las coordenadas de origen y el ancho"+\
          " de la tablilla\ndel pdf correspondiente."
    while True:
        try:
            BOARD_ORIGIN = [int(raw_input('\nCoordenada X del origen: ')),
                            int(raw_input('\nCoordenada Y del origen: '))]
            BOARD_WIDTH = ['w', unitsConverter(int(raw_input\
                           ('\nAncho de la tablilla: ')), True,
                           BOARD_ORIGIN, False)]
            break
        except (TypeError, ValueError):
            print '\nERROR 001. Introduzca un valor numerico'+\
            '. No se permiten los caracteres\nalfabeticos o especiales.'

    return HEADER, BOARD_ORIGIN, BOARD_WIDTH


def unitsConverter(mils, isBoardWidth, BOARD_ORIGIN, isXcoord):
    """Convert mil units to micron units.

    Keyword Arguments:
    mils -- value in mils
    isBoardWidth -- is the current value a board width?
    BOARD_ORIGIN -- offset used for this board
    isXcoord -- is the current value an X coord?
    """
    if isBoardWidth:
        # 1 Mil equals 25.4 Microns
        # Added a tolerance for board width
        return int(math.ceil(mils * 25.4))
    elif isXcoord:
        return int((mils + BOARD_ORIGIN[0]) * 25.4)
    else:
        return int((mils + BOARD_ORIGIN[1]) * -25.4)


def fileNamer():
    """Return a path for each file."""
    print "Recuerde que ambos archivos deben tener extension .csv"
    BOM_FILENAME = raw_input('\nIntroduzca la direccion del archivo BOM: ')\
                             .replace(".csv", "").replace("\"","")
    CAD_FILENAME = raw_input('\nIntroduzca la direccion del archivo CAD: ')\
                             .replace(".csv", "").replace("\"","")
    PLX_FILENAME = BOM_FILENAME

    return BOM_FILENAME, CAD_FILENAME, PLX_FILENAME


def deviceEnumerator(myString):
    """Return a list of names for devices in a group.

    myString -- string grouping devices in this format: 'aXXX-aXXX'
    """
    if '-' in myString:
        strMod = myString.split('-')
        devRange = range(int(filter(lambda x: x.isdigit(), strMod[0])),
                         int(filter(lambda x: x.isdigit(), strMod[1]))+1)
        devType = filter(lambda x: x.isalpha(), strMod[0])
        return [devType + str(d) for d in devRange]
    else:
        return [myString.replace(' ','')]

def main():
    """Print a message with an error description."""
    raw_input("ERROR 003. Wrong file! Use plxHelper.py ")

if __name__ == '__main__':
    main()
