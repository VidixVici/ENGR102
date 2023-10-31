# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 6.16 LAB: Balancing numbers
# Date: 25 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math
inData = int(input("Enter a value for n: "))
below = inData - 1
above = inData + 1
checkNum = 0
checkHigh = 0
r = 0
x = 1
while below > 0:
    checkNum += below
    below -= 1
while x != 0:
    if checkHigh < checkNum:
        checkHigh += above
        above += 1
        r += 1
    elif checkHigh == checkNum:
        print(str(inData) + " is a balancing number with r=" + str(r))
        x = 0
    else:
        print(str(inData) + " is not a balancing number")
        x = 0

