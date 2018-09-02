# 2-D-Heat-Conduction
The two types of methods to find the temperature at each grid-point of a 2D plate where three adjucent side temperature is same (taken as To) and the fourth side temperature is higher (taken as Ta)

The problem of 2D heat conduction solved using Python as a tool. The method used in approximating the values of temperature is Gauss Seidel and Analytical formula.

# Motivation
The analysis of a 44 grid requires to solve 4 equation with 4 unknown and by gauss seidel, manually doing it involves iterating the 4 values about 5 times. It is highly convenient to find out results more accurately and visualising it in a 3D plot using a computer for better understanding. Also analytical method is available which is discussed in the second part.

# Code Style
The code is purely written in Python with the use of libraries matplotlib, numpy and math. --------------------------------------------------------

# For Numerical Part

# Tech/Framework used
Build with-
Visual Studios Code

# Installation
 The following are the links to websites to install the required libraries.
https://matplotlib.org/users/installing.html
https://docs.scipy.org/doc/numpy/user/install.html

These libraries are needed by the program to run on your personal computer. Apart from that Python version 2.7.0 or above is required to run the program. 

# How to use?
The basic design of the code lies in the problem statement. The given plate / 2D surface is divided into a grid / array where each point in the array contains the value of temperature corresponding to that particular grid point / array point.

The temperature of the grid point is calculated using the formula:

    T(i,j) = 1/4( T(i-1,j) + T(i+1,j) + T(i,j-1) + T(i,j+1) )

Where T(i,j) is the corresponding temperature of grid-point (i,j).
The above equation is iterated in a loop to find the final values of T(i,j) using Gauss Seidel method.
Mention the values of Length (L) and Width (W) in the ratio of number of grid-points you wish to iterate in.
Then, mention the values of To and Ta according to the question to get the graph plots in 3D and 2D for temperature variation.
To check / get a reference, the the LW dimensional array of values of temperature is displayed in the terminal.
Close the first 3D plot to open the 2D plot. (The two are not displayed simultaneously)

It is advisable to keep the number of grid-points  5050 if the computational power of the computer is low.
--------------------------------------------------------


# For Analytical Part

# Tech/Framework used
Build with-
Visual Studios Code

# Installation
 The following are the links to websites to install the required libraries.
https://matplotlib.org/users/installing.html
https://docs.scipy.org/doc/numpy/user/install.html

These libraries are needed by the program to run on your personal computer. Apart from that Python version 2.7.0 or above is required to run the program. 

# How to use?
   The analytical solution is given by the equation:
   
 T(i,j) - ToTa - To = 2 n = 1 (1 + (-1)nn) (sinh(nj)sinh(nw)) (sin(ni))

The known values here (to be entered by the user) are To and Ta along with the desired number of iterations. 
The corresponding 3D plot of temperature is displayed.

The number of iterations are advised to be  300 as the problem of overflow can occur.
