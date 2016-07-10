#!/usr/bin/python

import sys
import os
from dictionary import shifter

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def crypt(operator,key,target):
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

    os.system("rm *.pyc")

    for index in range(len(target)):
        finalProduct[index] =  mapToChar[operator(rootNumArr[index] , shiftNumArr[index]) % ALPHABET_SIZE]
        #print mapToChar[(shiftNumArr[index] + rootNumArr[index]) % ALPHABET_SIZE]
    return finalProduct

if __name__ == "__main__":
    print 'Hello '
    if sys.argv[1] == '-e':
        print crypt(addition,sys.argv[2],sys.argv[3])
    elif sys.argv[1] == '-d':
        print crypt(subtraction,sys.argv[2],sys.argv[3])
    else:
        print "ERROR: need to have encrypt/decrypt"
        sys.exit()
