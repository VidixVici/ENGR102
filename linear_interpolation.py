# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Caleb Anders
# Quinton Walberg
# Elisabeth Guzman
# Zachary Harbert
# Section: 562
# Assignment: 2.8 LAB: Linear Interpolation
# Date: 29 AUGUST 2023
#
#
# YOUR CODE HERE
#
from math import *
pos1 = 2027
pos2 = 23027
time1 = 10
time2 = 55
timeEval = 25
radOfEarth = 6745
circOfEarth = (2 * pi * radOfEarth)
posEval = ((pos2 - pos1)/(time2 - time1)) * (timeEval - time1) + pos1
print("Part 1:")
print("For t = 25 minutes, the position p = " + str(posEval) + " kilometers")
timeEval = 300
posEval = ((pos2 - pos1)/(time2 - time1)) * (timeEval - time1) + pos1
x = 0
if posEval > circOfEarth:
    numOfSub = posEval // circOfEarth
    while x < numOfSub:
        posEval -= circOfEarth
        x += 1
print("Part 2:")
print("For t = 300 minutes, the position p = " + str(posEval) + " kilometers")

