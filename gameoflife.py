
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

def Glider(grid,x,y): #creates glider at coordinates x, y in grid
    grid[y,x+1] = 1 
    grid[y+1,x+2] = 1
    grid[y+2,x:x+3] = 1
    
def Pillar(grid,x,y): #creates pillar at coordinates x, y in grid
    grid[y:y+3,x] = 1

def LWSship(grid,x,y): # creates a lightweight space ship at x, y in grid
    grid[y,x+1] = 1
    grid[y+1:y+3,x] = 1
    grid[y+3,x:x+4] = 1
    grid[y,x+4] = 1
    grid[y+2,x+4] = 1
    
def Survival(gridInput,interval,NumberOfSteps):
    shape = np.shape(gridInput) #retrieves dimensions of inputed grid
    gridOutput = np.zeros((shape[0],shape[1],NumberOfSteps)) #creates a 3d array with dimensions of inputed grid and number of steps to store all 'frames' of the simulation
    steps = np.arange(0,NumberOfSteps,1) #creates an array of 0 to number of steps with intervals of 1
    gridTemp0 = gridInput #creates starting 2d array to run the game of life process on
    for i in steps:#runs the game of life process, the number of times is the length of the steps array
        print(i)
        plt.pause(interval)
        gridTemp1 = np.roll(gridTemp0,1,axis=0) + np.roll(gridTemp0,-1,axis=0) + np.roll(gridTemp0,1,axis=1) + np.roll(gridTemp0,-1,axis=1) + np.roll(np.roll(gridTemp0,1,axis=1),1,axis=0) + np.roll(np.roll(gridTemp0,-1,axis=1),1,axis=0) + np.roll(np.roll(gridTemp0,1,axis=1),-1,axis=0) + np.roll(np.roll(gridTemp0,-1,axis=1),-1,axis=0) #creates grid which has the sum of the 8 surrounding cells in each cell, ie how many neighbours
        grid2 = gridInput * 0 #creates output grid the same size as input grid
        gridTemp2 = gridTemp1 * gridTemp0 #creates grid with values only when the cell was alive last, time, otherwise cells =0
        grid2[gridTemp2 == 0] = 0 #Death by underpopulation
        grid2[gridTemp2 == 1] = 0 #Death by underpopulation
        grid2[gridTemp2 == 2] = 1 #Life by survival
        grid2[gridTemp2 == 3] = 1 #Life by survival
        grid2[gridTemp2 > 3] = 0 #Death by overpopulation
        grid2[gridTemp1 == 3] = 1 #Life by reproduction
        gridOutput[:,:,i] = grid2 #saves this iteration of the grid
        gridTemp0 = grid2 #sets the starting array for the next iteration to the final grid of the last iteration
    return gridOutput #outputs the final 3d array containing the entire simulation/all iterations

def runGame(data,intervalTime):
    length = np.shape(data)[2] # retrieves number of iterations
    plt.figure(0,figsize=(20,10)) #creates figure
    for i in np.arange(0,length,1): #loop for length of number of iterations
        plt.imshow(data[:,:,i],cmap='gray') #plots grid of current iteration as an image, with greyscale colour map
        plt.pause(intervalTime) #pauses loop briefly
        plt.cla()#clears figure to avoid memory issues
        name = "gunframe" + str(i) + ".jpg"
        image = upscale(data[:,:,i],10)
        scipy.misc.imsave(name, image)
    plt.close() #closes plot at end of loop

#grid = np.zeros((100,100))
#Glider(grid,5,5)
#data = Survival(grid,1,1000)
runGame(data,0.01)

