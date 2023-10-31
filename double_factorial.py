# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 6.14 LAB: Double factorial
# Date: 27 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math
def doublefactorial(num):
    num = num
    temp = num
    doublefactorial = 0
    if num == 0:
        num = 1
    else:
        while temp >= 3:
            temp -= 2
            num *= temp
    return num
