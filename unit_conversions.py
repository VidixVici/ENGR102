# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Alexis Cline
# Brennon Sherrod
# Drew Viner
# Zachary Harbert
# Section: 562
# Assignment: 3.15 LAB: Unit Conversions
# Date: 1 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math
global dataInput
dataInput = float(input("Please enter the quantity to be converted: "))
print()
def lbsToNewtons():
    global dataInput
    newtonsInLbs = 4.44822
    newtons = dataInput * newtonsInLbs
    print(str(format(dataInput, '0.2f')) + " pounds force is equivalent to " + str(format(newtons, '0.2f')) + " Newtons")

def metersToFeet():
    global dataInput
    feetInMeters = 3.28084
    feet = dataInput * feetInMeters
    print(str(format(dataInput, '0.2f')) + " meters is equivalent to " + str(format(feet, '0.2f')) + " feet")

def atmToKpa():
    global dataInput
    kpaInAtm = 101.325
    kpa = dataInput * kpaInAtm
    print(str(format(dataInput, '0.2f')) + " atmospheres is equivalent to " + str(format(kpa, '0.2f')) + " kilopascals")

def wattsToBTU():
    global dataInput
    BTUinWatts = 3.412142
    btu = dataInput * BTUinWatts
    print(str(format(dataInput, '0.2f')) + " watts is equivalent to " + str(format(btu, '0.2f')) + " BTU per hour")

def lpsToUSgpm():
    global dataInput
    USgpmInLps = 15.8503287894
    USgpm = dataInput * USgpmInLps
    print(str(format(dataInput, '0.2f')) + " liters per second is equivalent to " + str(format(USgpm, '0.2f')) + " US gallons per minute")

def cToF():
    global dataInput
    fInC = 32
    fahrenheit = dataInput * (9/5) + fInC
    print(str(format(dataInput, '0.2f')) + " degrees Celsius is equivalent to " + str(format(fahrenheit, '0.2f')) + " degrees Fahrenheit")

lbsToNewtons()
metersToFeet()
atmToKpa()
wattsToBTU()
lpsToUSgpm()
cToF()