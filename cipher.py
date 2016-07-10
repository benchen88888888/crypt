#!/usr/bin/python

import sys
import os
from dictionary import shifter

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

# def arrayToString(array):
#     string = ''
#     for index in range(len(array)):
#         string = array[index]
#     return string

def crypt(operator,key,target):
    print '------------------------------------------------------'
    print 'Method:\t\t',operator.__name__
    print 'Key:\t\t', key
    print 'Message:\t', target
    print '------------------------------------------------------'
    ALPHABET_SIZE = 26
    mapToNum = shifter.mapToNum
    mapToChar = shifter.mapToChar
    shiftNumArr = [None] * len(target)
    rootNumArr = [None] * len(target)
    finalProduct = [None] * len(target)
    keyLength = len(key)
    for index in range(len(target)):
        #print mapToNum[mapToNum[key[index]]%len(key)]
        shiftNumArr[index] = mapToNum[key[index % keyLength]]
        rootNumArr[index] = mapToNum[target[index]]
    #print shiftNumArr



    for index in range(len(target)):
        finalProduct[index] =  mapToChar[operator(rootNumArr[index] , shiftNumArr[index]) % ALPHABET_SIZE]

    finalProduct = ''.join(finalProduct)
    print 'Final Message: ',finalProduct
    return finalProduct

if __name__ == "__main__":
    os.system("rm *.pyc")
    if sys.argv[1] == '-h' or sys.argv[1] == '-help':
        print "Help stuff"
        sys.exit()

    alg = sys.argv[1]

    if alg == '-e':
        crypt(addition,sys.argv[2],sys.argv[3])
    elif alg == '-d':
        crypt(subtraction,sys.argv[2],sys.argv[3])
    else:
        print "ERROR: need to have encrypt/decrypt"
        sys.exit()
