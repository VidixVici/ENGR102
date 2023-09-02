# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 3.17 LAB: Using input
# Date: 31 AUGUST 2023
#
#
# YOUR CODE HERE
#
import math

print("This program calculates the applied force given mass and acceleration")
mass = input("Please enter the mass (kg): ")
print("")
acceleration = input("Please enter the acceleration (m/s^2): ")
print("")
force = float(mass) * float(acceleration)
print("Force is " + str(format(force, '0.1f')) + " N")
print("")

print("This program calculates the wavelength given distance and angle")
distance = input("Please enter the distance (nm): ")
print("")
theta = float(input("Please enter the angle (degrees): ")) * (math.pi/180)
print("")
wavelength = 2* float(distance) * math.sin(float(theta))
print("Wavelength is " + str(format(wavelength, '0.4f')) + " nm")
print("")

print("This program calculates how much Radon-222 is left given time and initial amount")
time = float((input("Please enter the time (days): ")))
print("")
initialAmount = float(input("Please enter the initial amount (g): "))
halfLife = 3.8
radonLeft = initialAmount * 2**(-time / halfLife)
print("Radon-222 left is " + str(format(radonLeft, '0.2f')) + " g")
print("")

print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
print("")
volume = float(input("Please enter the volume (m^3): "))
print("")
temperature = float(input("Please enter the temperature (K): "))
idealGasConstant = 8.314
pressure = (temperature * idealGasConstant * moles) / (volume)
print("Pressure is " + str(format(pressure/1000.0, '0.0f')) + " kPa")
print("")