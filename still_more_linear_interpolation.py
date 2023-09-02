# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Alexis Cline
# Brennon Sherrod
# Drew Viner
# Zachary Harbert
# Section: 562
# Assignment: 3.16 LAB: Still More Linear Interpolation
# Date: 1 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math

global time1
time1 = float(input("Enter time 1: "))
print()
x1 = float(input("Enter the x position of the object at time 1: "))
print()
y1 = float(input("Enter the y position of the object at time 1: "))
print()
z1 = float(input("Enter the z position of the object at time 1: "))
print()

global time2
time2 = float(input("Enter time 2: "))
print()
x2 = float(input("Enter the x position of the object at time 2: "))
print()
y2 = float(input("Enter the y position of the object at time 2: "))
print()
z2 = float(input("Enter the z position of the object at time 2: "))
print()
print()

global point1
point1 = (x1,y1,z1)
global point2
point2 = (x2,y2,z2)
def linear_interpolation():
    global point1
    global point2
    global time1
    global time2
    timesToTest = (time2 - time1) / 4
    x = 0
    timeTest = time1
    while x < 5:
        if x > 0:
            timeTest = float(timeTest) + float(timesToTest)
        else: 
            timeTest = time1
        Interpolate = (format(((point2[0] - point1[0])/(time2 - time1)) * (timeTest - time1) + point1[0], '0.3f'),
                        format(((point2[1] - point1[1])/(time2 - time1)) * (timeTest - time1) + point1[1], '0.3f'),
                        format(((point2[2] - point1[2])/(time2 - time1)) * (timeTest - time1) + point1[2], '0.3f'))
        print("At time " + str(format(timeTest, '0.2f')) + " seconds the object is at " + "(" + 
            str(Interpolate[0] + ", " + str(Interpolate[1]) + ", " + str(Interpolate[2]) + ")"))
        x += 1
linear_interpolation()