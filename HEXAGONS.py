# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:02:47 2019

@author: benjy
"""

from array import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import random

def threeCol(arrays):
    array2 = arrays
    a = np.zeros(6)
    b = np.zeros(6)
    c = 0
    d = np.zeros(6)
    e = np.zeros(6)
    a[0] = arrays[0,0]
    a[1] = arrays[0,2]
    a[2] = arrays[1,2]
    a[3] = arrays[2,2]
    a[4] = arrays[2,0]
    a[5] = arrays[1,0]
    #print("1st a",a)
    for i in np.array([0,1,2,3,4,5]):
        if a[0] != a[1]:
            #print("a[1:6]",a[1:6])
            z = a
            b[0:5] = a[1:6]
            b[-1] = z[0]
            #print("a",a)
            #print("b",b)
            #print("a[0]",a[0])
            a = b
            b = np.zeros(6)

        elif a[0] == 0:
            b[0:5] = a[1:6]
            b[5] = a[0]
            a = b
            b = np.zeros(6)
        else:
            c = i
            break
    #print(a)
    if a[3] == 1:
        d = np.array([0,0,0,1,0,1])
    elif a[4] == 1:
        d = np.array([0,0,1,0,1,0])
    #print(d)
    for i in np.zeros(c):
        e[1:6] = d[0:5]
        e[0] = d[5]
        #print(d)
        d=e
        e = np.zeros(6)
    #print(d)
    array2[0,0] = d[0]
    array2[0,2] = d[1] 
    array2[1,2] = d[2] 
    array2[2,2] = d[3] 
    array2[2,0] = d[4] 
    array2[1,0] = d[5] 
    
    return array2

def threeColStat(array):
    array2 = array
    a = np.zeros(6)
    b = np.zeros(6)
    c = 0
    d = np.zeros(6)
    e = np.zeros(6)
    a[0] = array[0,0]
    a[1] = array[0,2]
    a[2] = array[1,2]
    a[3] = array[2,2]
    a[4] = array[2,0]
    a[5] = array[1,0]
    for i in np.array([0,1,2,3,4,5]):
        if a[0] != a[1]:
            b[0:5] = a[1:6]
            b[5] = a[0]
            a=b
            b = np.zeros(6)
        elif a[0] == 0:
            b[0:5] = a[1:6]
            b[5] = a[0]
            a=b
            b = np.zeros(6)
        else:
            c = i
            break
    if a[3] == 1:
        d = np.array([0,1,0,1,1,1])
    elif a[4] == 1:
        d = np.array([1,0,1,1,1,0])
    for i in np.zeros(c):
        e[1:6] = d[0:5]
        e[0] = d[5]
        #print(d)
        d=e
        e = np.zeros(6)
    #print(d)
    array2[0,0] = d[0]
    array2[0,2] = d[1] 
    array2[1,2] = d[2] 
    array2[2,2] = d[3] 
    array2[2,0] = d[4] 
    array2[1,0] = d[5] 
    
    return array2        
            
        

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

def createGrid(xdim,ydim):
    grid = np.zeros((3*xdim,3*ydim))
    return grid

def evaluate(threeGrid):
    #if np.any(threeGrid == 1):
            #print(threeGrid)
    threeGrid2 = np.zeros((3,3))
    #3way head on collision
    if np.all(threeGrid == np.array([[1,0,0],[0,0,1],[1,0,0]])):
        threeGrid2 = threeGrid
        #print('a')
    
    elif np.all(threeGrid == np.array([[0,0,1],[1,0,0],[0,0,1]])):
        threeGrid2 = threeGrid
       # print('b')
        
    #2way head on collisions
    elif np.all(threeGrid == np.array([[1,0,0],[0,0,0],[0,0,1]])):
        n = random.randint(0,1)
        if n == 1:
            threeGrid2 = np.array([[0,0,0],[1,0,1],[0,0,0]])
            #print('c')
        else:
            threeGrid2 = np.array([[0,0,1],[0,0,0],[1,0,0]])
           # print('d')
    
    elif np.all(threeGrid == np.array([[0,0,0],[1,0,1],[0,0,0]])):
        n = random.randint(0,1)
        if n == 1:
            threeGrid2 = np.array([[1,0,0],[0,0,0],[0,0,1]])
            #print('e')
        else:
            threeGrid2 = np.array([[0,0,1],[0,0,0],[1,0,0]])
            #print('f')
    
    elif np.all(threeGrid == np.array([[0,0,1],[0,0,0],[1,0,0]])):
        n = random.randint(0,1)
        if n == 1:
            threeGrid2 = np.array([[0,0,0],[1,0,1],[0,0,0]])
            #print('g')
        else:
            threeGrid2 = np.array([[1,0,0],[0,0,0],[0,0,1]])
            #print('h')
            
    #2way head on collision with stationary        
    elif np.all(threeGrid == np.array([[1,0,0],[0,1,0],[0,0,1]])):
        n = random.randint(0,1)
        if n == 1:
            threeGrid2 = np.array([[0,0,0],[1,1,1],[0,0,0]])
            #print('i')
        else:
            threeGrid2 = np.array([[0,0,1],[0,1,0],[1,0,0]])
            #print('j')
    
    elif np.all(threeGrid == np.array([[0,0,0],[1,1,1],[0,0,0]])):
        n = random.randint(0,1)
        if n == 1:
            threeGrid2 = np.array([[1,0,0],[0,1,0],[0,0,1]])
            #print('k')
        else:
            threeGrid2 = np.array([[0,0,1],[0,1,0],[1,0,0]])
            #print('l')
    
    elif np.all(threeGrid == np.array([[0,0,1],[0,1,0],[1,0,0]])):
        n = random.randint(0,1)
        if n == 1:
            threeGrid2 = np.array([[0,0,0],[1,1,1],[0,0,0]])
            #print('m')
        else:
            threeGrid2 = np.array([[1,0,0],[0,1,0],[0,0,1]])
            #print('n')
            
    #2way 60deg angled collision        
    elif np.all(threeGrid == np.array([[1,0,0],[0,0,0],[1,0,0]])):
        threeGrid2 = np.array([[0,0,0],[0,1,1],[0,0,0]])
        #print('o')
        #print(threeGrid2)
        
    elif np.all(threeGrid == np.array([[0,0,1],[1,0,0],[0,0,0]])):
        threeGrid2 = np.array([[0,0,0],[0,1,0],[0,0,1]])
        #print('p')
    
    elif np.all(threeGrid == np.array([[1,0,0],[0,0,1],[0,0,0]])):
        threeGrid2 = np.array([[0,0,0],[0,1,0],[1,0,0]])
        #print('q')
    
    elif np.all(threeGrid == np.array([[0,0,1],[0,0,0],[0,0,1]])):
        threeGrid2 = np.array([[0,0,0],[1,1,0],[0,0,0]])
        #print('r')
    
    elif np.all(threeGrid == np.array([[0,0,0],[0,0,1],[1,0,0]])):
        threeGrid2 = np.array([[1,0,0],[0,1,0],[0,0,0]])
        #print('s')
        
    elif np.all(threeGrid == np.array([[0,0,0],[1,0,0],[0,0,1]])):
        threeGrid2 = np.array([[0,0,1],[0,1,0],[0,0,0]])
        #print('t')
        
    #2way stationary collision        
    elif np.all(threeGrid == np.array([[0,0,0],[0,1,1],[0,0,0]])):
        threeGrid2 = np.array([[1,0,0],[0,0,0],[1,0,0]])
        #print('u')
        
    elif np.all(threeGrid == np.array([[0,0,0],[0,1,0],[0,0,1]])):
        threeGrid2 = np.array([[0,0,1],[1,0,0],[0,0,0]])
        #print('v')
    
    elif np.all(threeGrid == np.array([[0,0,0],[0,1,0],[1,0,0]])):
        threeGrid2 = np.array([[1,0,0],[0,0,1],[0,0,0]])
        #print('w')
    
    elif np.all(threeGrid == np.array([[0,0,0],[1,1,0],[0,0,0]])) :
        threeGrid2 = np.array([[0,0,1],[0,0,0],[0,0,1]])
        #print('x')
    
    elif np.all(threeGrid == np.array([[1,0,0],[0,1,0],[0,0,0]])):
        threeGrid2 = np.array([[0,0,0],[0,0,1],[1,0,0]])
        #print('y')
        
    elif np.all(threeGrid == np.array([[0,0,1],[0,1,0],[0,0,0]])):
        threeGrid2 = np.array([[0,0,0],[1,0,0],[0,0,1]])
        #print('z')

    #three particle collisions

    elif np.sum(threeGrid) == 3 and threeGrid[1,1] != 1:
        n = random.randint(0,1)
        
        if n == 1:
            threeGrid2[0:3,0] = (threeGrid[0:3,0] - 1)*-1
            threeGrid2[0:3,2] = (threeGrid[0:3,2] - 1)*-1
            #print('aa')
        else:
            threeGrid2 = threeCol(threeGrid)
            threeGrid2[1,1] = 1
            #print('ab')
            
    #three particle collisions with stationary

    elif np.sum(threeGrid) == 4 and threeGrid[1,1] == 1:
        n = random.randint(0,1)
        
        if n == 1:
            threeGrid2[0:3,0] = (threeGrid[0:3,0] - 1)*-1
            threeGrid2[0:3,2] = (threeGrid[0:3,2] - 1)*-1
            threeGrid2[1,1] = 1
            #print('ac')
        else:
            threeGrid2 = threeColStat(threeGrid)
            #print('ad')
    else:
        threeGrid2[0,0] = threeGrid[2,2]
        threeGrid2[0,1] = threeGrid[2,1]
        threeGrid2[0,2] = threeGrid[2,0]
        threeGrid2[1,0] = threeGrid[1,2]
        threeGrid2[1,1] = threeGrid[1,1]
        threeGrid2[1,2] = threeGrid[1,0]
        threeGrid2[2,0] = threeGrid[0,2]
        threeGrid2[2,1] = threeGrid[0,1]
        threeGrid2[2,2] = threeGrid[0,0]
        #print('ae')
        #if np.any(threeGrid2 == 1):
            #print(threeGrid,threeGrid2)
                      
    return threeGrid2, threeGrid


def runGame(startGrid,iterations):
    n = np.shape(startGrid)
    data = np.zeros((n[0],n[1],iterations*2))
    data[:,:,0]=startGrid
    for i in range(iterations-1):
        print(i)
        for x in range(int(n[0]/3)):
            for y in range(int(n[1]/3)):
                #if x == 0 :
                #    print(data[3:6,3:6,0])
                #    print("int")
                #print(i)
                #print(x,y)
                temp, original = evaluate(data[3*x:3*x+3,3*y:3*y+3,2*i])
                #print(" ")
                #if np.any(temp == 1):
                    #print(original,temp)
                data[3*x:3*x+3,3*y:3*y+3,2*i+1] = temp
                #mid left
                if 3*y-1 == -1:
                    data[3*x+1,3*y,2*i+2] = temp[1,0]                 
                else:
                    data[3*x+1,3*y-1,2*i+2] = temp[1,0]
                #mid right
                if 3*y+3 == n[1]:
                    data[3*x+1,3*y+2,2*i+2] = temp[1,2]
                else:
                    data[3*x+1,3*y+3,2*i+2] = temp[1,2] 
                
                if x%2 == 0:
                    if 3*x-1 == -1:
                        data[3*x,3*y,2*i+2] = temp[0,0]

                    else:    
                        data[3*x-1,3*y+2,2*i+2] = temp[0,0]

                    if 3*x-1 == -1 or 3*y+3 == n[1]:

                        data[3*x,3*y+2,2*i+2] = temp[0,2]
                    else:    

                        data[3*x-1,3*y+3,2*i+2] = temp[0,2]
                    if 3*x+3 == n[0]:
                        data[3*x+2,3*y,2*i+2] = temp[2,0]
                    else:
                        data[3*x+3,3*y+2,2*i+2] = temp[2,0]
                    if 3*y+3 == n[1]:
                        data[3*x+2,3*y+2,2*i+2] = temp[2,2]
                    else:
                        data[3*x+3,3*y+3,2*i+2] = temp[2,2]
                else:
                    if 3*y-1 == -1:
                        data[3*x,3*y,2*i+2] = temp[0,0]
                    else:
                        data[3*x-1,3*y-1,2*i+2] = temp[0,0]
                        
                    data[3*x-1,3*y,2*i+2] = temp[0,2]
                    
                    if 3*x+3 != n[0] and 3*y-1 != -1:  
                        data[3*x+3,3*y-1,2*i+2] = temp[2,0]
                    else:
                        data[3*x+2,3*y,2*i+2] = temp[2,0]
                    if 3*x+3 == n[0]:
                        data[3*x+2,3*y+2,2+x+2] = temp[2,2]
                    else:
                        data[3*x+3,3*y,2*i+2] = temp[2,2]
                
                
                data[3*x+1,3*y+1,2*i+1] = temp[1,1]
                data[3*x+1,3*y+1,2*i+2] = temp[1,1]
                
        data[:,:,0]=startGrid
    return data

def createGrid(xdim,ydim):
    grid = np.zeros((3*xdim,3*ydim))
    return grid

gridh = createGrid(100,100)
gridh[:,0] = 1
datah = runGame(gridh,100)