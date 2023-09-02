# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 3.18 LAB: Writing functions
# Date: 31 AUGUST 2023
#
#
# YOUR CODE HERE
#
import math
global sideLength 
global triangleArea
global squareArea  
global pentagonArea
global dodecagonArea
sideLength = float(input("Please enter the side length: "))
print("")

def triangleArea():
    global sideLength
    global triangleArea
    triangleArea = format((math.sqrt(3/4) * sideLength**2) / 2, '0.3f')
    

def squareArea():
    global sideLength
    global squareArea
    squareArea = format(sideLength**2, '0.3f')
    
    

def pentagonArea():
    global sideLength
    global pentagonArea
    pentagonArea = format(0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * sideLength**2, '0.3f')
    

def dodecagonArea():
    global sideLength
    global dodecagonArea
    dodecagonArea = format(3 * sideLength**2 * (2 + math.sqrt(3)), '0.3f')
    
triangleArea()
squareArea()
pentagonArea()
dodecagonArea()
sideLength = format(sideLength, '0.2f')
print("A triangle with side " + str(sideLength) + " has area " + str(triangleArea))
print("A square with side " + str(sideLength) + " has area " + str(squareArea))
print("A pentagon with side " + str(sideLength) + " has area " + str(pentagonArea))
print("A dodecagon with side " + str(sideLength) + " has area " + str(dodecagonArea))