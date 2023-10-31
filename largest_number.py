# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 4.16 LAB: Largest number
# Date: 7 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math
x = 1
numberCompare1 = -math.inf
while x < 4:
    numberCompare2 = float(input("Enter number "+ str(x) + ": "))
    print()
    if numberCompare1 < numberCompare2:
        numberCompare1 = numberCompare2
    else:
        numberCompare1 = numberCompare1
    x += 1
print("The largest number is", float(numberCompare1))
