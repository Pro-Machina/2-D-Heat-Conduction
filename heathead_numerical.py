from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

#Adds a 3D ploting figure
np.random.seed(19680801)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Enter the value of length and breadth in the ratio of L and W provided in the question
#Note that the number of grid-points can be changed
row = int(raw_input("Enter grid length (L): "))
col = int(raw_input("Enter grid width (W): "))

#Since the values start from 0, we have to normalize the variables according to it
row -= 1
col -= 1

#Enter the value of T0 and Ta as specified in the question
t0 = float(raw_input("Enter value of T0: "))
ta = float(raw_input("Enter the value of Ta: "))

#Creating a 2D array/matrix with all entries 0 to signify temperature at different grig points inside the area
#These are the initial values on which the gauss siedel is then applied
T = [[0.0 for x in range(col + 1)] for y in range(row + 1)] 

#Following loops set the boundary temperatures
#Note that the corner temperatures are specified to avoid ambiguity and hence the final result may change due to this
for j in range(0, col+1):
    T[0][j] = ta
    T[row][j] = t0
for i in range(1, row+1):
    T[i][0] = t0
    T[i][col] = t0

#temp value stores the initial temperature of a grid point to compare it to the one after applying gauss siedel
#count is just to specify number of iterations to run to get the final value from gauss siedel method
temp = 0.0
count = 0

#Keeping a value of T0 as 0 effects the number of iterations required to reach the final result
if ( t0 == 0):
    iteration = 100
else:
    iteration = 50

#The following code will impliment Gauss Seidel method to find temperatures at different grid points
while( count < ((row+1)*(col+1)*iteration)):
    for i in range(1, row):
        for j in range(1, col):
            temp = T[i][j]
            T[i][j] = (1.0/4.0)*(T[i-1][j] + T[i+1][j] + T[i][j-1] + T[i][j+1])

            #math.fabs() gives the absolute value of the argument inside the bracket
            #Decreasing the absolute difference will increase the stability 
            if( math.fabs(temp - T[i][j]) <= 0.0000001):
                count += 1
#The final values of temperature at different grid points are finally printed just for a refrence
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

#Plotting in a 2D plot 
x = np.arange(1, col+2)

for i in range(0, row+1):
    plt.plot(x, T[i])

# naming the x axis
plt.xlabel('Length (L)')

# naming the y axis
plt.ylabel('Temperature')

#Title of the graph
plt.title('Temperature plot of grid points')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()