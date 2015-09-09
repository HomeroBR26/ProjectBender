#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MAT.TE
#
# Created:     08/09/2015
# Copyright:   (c) MAT.TE 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(myString):
    if '-' in myString:
        strMod = myString.split('-')
        devRange = range(int(filter(lambda x: x.isdigit(), strMod[0])),
                         int(filter(lambda x: x.isdigit(), strMod[1]))+1)
        devType = filter(lambda x: x.isalpha(), strMod[0])
        return [devType + str(d) for d in devRange]
    else:
        return [myString.replace(' ','')]

if __name__ == '__main__':
    print main('   d99')
