# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 5.4: LAB: Boiling curve
# Date: 20 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
# MATH IMPORT
import math

#TAKING INPUT FROM USER
excess = float(input("Enter the excess temperature: "))

# VARIABLE DECLARATION FOR DIFFERENT LINE SEGMENTS
A = (1.3, 1000)
B = (5, 7000)
C = (30, 1500000)
D = (120, 25000)
E = (1200, 1500000)

xA = A[0]
yA = A[1]

xB = B[0]
yB = B[1]

xC = C[0]
yC = C[1]

xD = D[0]
yD = D[1]

xE = E[0]
yE = E[1]

x = excess

# LOGIC AND DECISIONS FOR DIFFERENT M VALUES + Y FUNCTIONS
if (excess >= 1.3) and (excess < 5):
    m = (math.log10(yB / yA)) / (math.log10(xB / xA))
    y = yA * ((x / xA) ** m)
    print("The surface heat flux is approximately " + str(format(y, "0.0f")) + " W/m^2")

elif (excess >= 5) and (excess < 30):
    m = (math.log10(yC / yB)) / (math.log10(xC / xB))
    y = yB * ((x / xB) ** m)
    print("The surface heat flux is approximately " + str(format(y, "0.0f")) + " W/m^2")

elif (excess >= 30) and (excess < 120):
    m = (math.log10(yD / yC)) / (math.log10(xD / xC))
    y = yC * ((x / xC) ** m)
    print("The surface heat flux is approximately " + str(format(y, "0.0f")) + " W/m^2")

elif (excess >= 120) and (excess < 1200):
    m = (math.log10(yE / yD)) / (math.log10(xE / xD))
    y = yD * ((x / xD) ** m)
    print("The surface heat flux is approximately " + str(format(y, "0.0f")) + " W/m^2")

else:
    print("Surface heat flux is not available")
