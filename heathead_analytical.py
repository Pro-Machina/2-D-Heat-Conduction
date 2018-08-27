from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

#Adds a 3D ploting figure
np.random.seed(19680801)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Defining value of PI
PI = 3.14159265358979323846264

#Enter the value of length and breadth in the ratio of L and W provided in the question
#Note that the number of grid-points can be changed
row = int(raw_input("Enter grid length (L): "))
col = int(raw_input("Enter grid width (W): "))

#The length or plate is the number of columns and the width is the number of rows
w = row
l = col

#Since the values start from 0, we have to normalize the variables according to it
row -= 1
col -= 1

#Enter the value of T0 and Ta as specified in the question
t0 = float(raw_input("Enter value of T0: "))
ta = float(raw_input("Enter the value of Ta: "))

#Defining a 2D matrix to store value of temperature of grid-points
T = [[0.0 for x in range(col + 1)] for y in range(row + 1)] 

#The number of iterations can be changed
iteration = int(raw_input("Enter the number of iterations: "))

#Assigning the values of temperature as per the analytical method
for i in range(0, row+1):
    for j in range(0, col+1):
        n = 1
        temp = 0.0
        while(n <= iteration):
            lam = (n*PI)/l #Defining lambda
            temp += ( (1 + math.pow(-1, n+1))*(math.sinh(lam*j))*(math.sin(lam*i)) )/( (n*PI)*(math.sinh(lam*w)) )
            n += 1
             
        T[i][j] = ( 2*temp*(ta - t0) ) + t0

#Printing value of temperatures for refrence and comparision
print (T)

#Plotting using the scatter plot where a 3D scatter plot is plotted with specified grid values in x-y plane and the corrosponding temperature in the z-axis
for i in range(0, row+1):
    for j in range(0, col+1):
        xs = i
        ys = j
        zs = T[i][j]
        ax.scatter(xs, ys, zs, c = 'r')  #c = 'r' specifies that the scatter points are red in color

#Naming the x, y and z axis
ax.set_xlabel('Length: L')
ax.set_ylabel('Width: W')
ax.set_zlabel('Temperature')

# function to show the plot
plt.show()