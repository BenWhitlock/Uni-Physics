# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:46:51 2019

@author: benjy
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

def upscale(img,scale):
    shape = np.shape(img)
    
    scaledShape = [shape[0]*scale,shape[1]*scale]
    
    newImg = np.zeros((scaledShape[0],scaledShape[1]))
    a = int(scaledShape[0])
    b = int(scaledShape[1])
    for i in range(a):
        for j in range(b):
            x = int(i/scale)
            y = int(j/scale)
            c  = img[x,y]
            newImg[i,j] = c
    return newImg

def setRule(rule):
    binRule = bin(rule)
    length = len(binRule)
    totalKey = binRule[2:length]
    key = np.zeros(8)
    for i in range(length-2):
        key[-1-i] = totalKey[-1-i]
    return key[::-1]

def evaluate(a,b,c,key):
    #print(a,b,c)
    num = int(a*4 + b*2 + c)
    #print(num)
    newValue = key[num]
    return newValue

def extendArray(array2):
    length = len(array2)
    newLength = length + 6
    newArray2 = np.zeros(newLength)
    newArray2[1:-2] = array2
    return newArray2

def passArray(array3,key):
    newArray3 = np.zeros(len(array3))
    temp = np.zeros(len(array3)+2)
    temp[1:len(array3)+1] = array3
    #print(temp)
    for i in range(len(array3)):
        #print(i)
        n = i+1
        newValue = evaluate(temp[n-1],temp[n],temp[n+1],key)
        #print(newValue)
        newArray3[i] = newValue 
    return newArray3


def runGame(startArray,iterations,rule):
    key = setRule(rule)
    #print(key)
    data = np.zeros((iterations,len(startArray)))
    data[0,:] = startArray
    for j in range(iterations-1):
        data[j+1,:] = passArray(data[j,:],key)
    return data

initialArray =  np.zeros(100)
initialArray[int(len(initialArray)/2)] = 1
data1 = runGame(initialArray,30,110)

img = upscale(data1,10)
scipy.misc.imsave("Rule110.jpg", img)