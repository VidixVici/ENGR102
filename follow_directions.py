# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 1.13 LAB: Follow directions
# Date: 22 AUGUST 2023
#
#
# YOUR CODE HERE
#
import math

print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print("My guess is 1.99 repeating")
n = 0
x = 0.0
m = 1
while n < 9:
    if n == 0:
        x = 0
        n += 1
    else:
        x = 1 + (1 * 10**(-1 * m))
        m += 1
        n += 1
        equation = math.sin(x - 1)/(x - 1)
        print(equation)
print("")