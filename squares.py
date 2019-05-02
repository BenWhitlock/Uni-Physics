# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:01:19 2019

@author: benjy
"""
from array import *
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

def createGrid(xdim,ydim):
    grid = np.zeros((3*xdim,3*ydim))
    return grid

def evaluate(threeGrid):
    
    threeGrid2 = np.zeros((3,3))
    a = threeGrid[0,1]
    b = threeGrid[1,0]
    c = threeGrid[2,1]
    d = threeGrid[1,2]
    #print(a,b,c,d)
    a1 = 0.0
    b1 = 0.0
    c1 = 0.0
    d1 = 0.0
    sum = a+b+c+d
    
    if a == c:
        b1 = a
        d1 = c
    if b == d:
        a1 = b
        c1 = d
    if a != c:
        a1 = c
        c1 = a
    if b != d:
        b1 = d
        d1 = b
    if sum == 3:
        a1 = c
        b1 = d
        c1 = a
        d1 = b
    threeGrid2[0,1] = a1
    threeGrid2[1,0] = b1
    threeGrid2[2,1] = c1
    threeGrid2[1,2] = d1
    #print(a1,b1,c1,d1)
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
                #print(original,temp)
                data[3*x:3*x+3,3*y:3*y+3,2*i+1] = temp
                if 3*x-1 == -1:
                    data[3*x,3*y+1,2*i+2] = temp[0,1]
                else:
                    data[3*x-1,3*y+1,2*i+2] = temp[0,1]
                
                if 3*y-1 == -1:
                    data[3*x+1,3*y,2*i+2] = temp[1,0]                 
                else:
                    data[3*x+1,3*y-1,2*i+2] = temp[1,0]
               
                if 3*x+3 == n[0]:
                    data[3*x+2,3*y+1,2*i+2] = temp[2,1]
                else:
                    data[3*x+3,3*y+1,2*i+2] = temp[2,1]
                
                if 3*y+3 == n[1]:
                    data[3*x+1,3*y+2,2*i+2] = temp[1,2]
                else:
                    data[3*x+1,3*y+3,2*i+2] = temp[1,2]                

    return data
grids = createGrid(100,100)

def fillGridQuarter(grid):
    n = np.shape(grid)
    for i in range(int(n[0]/2)):
        for j in range(int(n[1]/2)):
            if i % 3 == 0 and j % 3 == 1:
                grid[i,j] = 1
            if j % 3 == 0 and i % 3 == 1:
                grid[i,j] = 1
            if i % 3 == 2 and j % 3 == 1:
                grid[i,j] = 1
            if j % 3 == 2 and i % 3 == 1:
                grid[i,j] = 1
def fillGridHalf(grid):
    n = np.shape(grid)
    for i in range(int(n[0]/(2**0.5))):
        for j in range(int(n[1]/(2**0.5))):
            if i % 3 == 0 and j % 3 == 1:
                grid[i,j] = 1
            if j % 3 == 0 and i % 3 == 1:
                grid[i,j] = 1
            if i % 3 == 2 and j % 3 == 1:
                grid[i,j] = 1
            if j % 3 == 2 and i % 3 == 1:
                grid[i,j] = 1
#fillGridQuarter(start)
#start[3,4]=1
#print(start)
for i in range(25):
    if i%3 == 1:
        grids[i,0] = 1
datas = runGame(grids,100)
#conc = np.zeros((50000,4))
#ns = np.shape(dat)
#qarea = ns[0]*ns[1]*4/9
#half0 = int(ns[0]/2)
#half1 = int(ns[1]/2)
#for i in np.arange(0,50000,1): #loop for length of number of iterations
        #plt.figure(0,figsize=(20,10))
        #plt.subplot(221)
        #plt.imshow(upscale(dat[:,:,i],10),cmap='gray') #plots grid of current iteration as an image, with greyscale colour map
        #clears figure to avoid memory issues
        #conc[i,0] = np.sum(dat[0:half0,0:half1,i])/qarea
        #conc[i,1] = np.sum(dat[0:half0,half1:-1,i])/qarea
        #conc[i,2] = np.sum(dat[half0:-1,0:half1,i])/qarea
        #conc[i,3] = np.sum(dat[half0:-1,half1:-1,i])/qarea
        #plt.subplot(222)
        #plt.ylim([0,0.25])
        #plt.xlabel("Quadrant")
        #plt.xticks(range(1,5))
        #plt.ylabel("Concentration (Proportion of total available space)")
        #plt.plot(np.array([1,1]),np.array([0,conc[i,0]]),linewidth=7.0)
        #plt.plot(np.array([2,2]),np.array([0,conc[i,1]]),linewidth=7.0)
        #plt.plot(np.array([3,3]),np.array([0,conc[i,2]]),linewidth=7.0)
        #plt.plot(np.array([4,4]),np.array([0,conc[i,3]]),linewidth=7.0)
        #plt.pause(0.001) #pauses loop briefly
        #name = "Qframe" + str(i)
        #plt.savefig(name)
       # plt.cla()
#plt.figure(0,figsize =(20,10))
#plt.plot(np.arange(0,50000,1),conc[:,0],label="Q1")
#plt.plot(np.arange(0,50000,1),conc[:,1],label="Q2")
#plt.plot(np.arange(0,50000,1),conc[:,2],label="Q3")
#plt.plot(np.arange(0,50000,1),conc[:,3],label="Q4")
#plt.legend(loc='best')
#plt.xlabel("Time (iterations")
#plt.ylabel("Concentration (particles per space)")
#plt.title("Graph showing concentrations of particles over time in each quadrant. Starting number = 1/4")