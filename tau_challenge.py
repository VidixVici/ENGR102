# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 3.19.1: LAB: Challenge program
# Date: 31 AUGUST 2023
#
#
# YOUR CODE HERE
#
import math
tauDigit = input("Please enter the number of digits of precision for tau: ")
tauDigits = "0." + str(tauDigit) + "f"
answer = format(math.tau, tauDigits)
print("The value of tau to "+ tauDigit + " digits is: " + answer)