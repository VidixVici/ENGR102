# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 2.9 LAB: Using Variables
# Date: 29 AUGUST 2023
#
#
# YOUR CODE HERE
#
import math

mass = 27.0
acceleration = 1.5
force = mass * acceleration

theta = 35 * (math.pi/180)
distance = 0.025
wavelength = 2* distance * math.sin(theta)

initialAmount = 27.0
time = 5
halfLife = 3.8
radonLeft = initialAmount * 2**(-time / halfLife)

moles = 5.0
volume = 0.270
temperature = 415.0
idealGasConstant = 8.314
pressure = (temperature * idealGasConstant * moles) / (volume)

print("Force is " + str(force) + " N")
print("Wavelength is " + str(wavelength) + " nm")
print("Radon-222 left is " + str(radonLeft) + " g")
print("Pressure is " + str(pressure/1000.0) + " kPa")