# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Zach Harbert
# Eli Guzman
# Avery Elaine Huey
# Alex K Kapoor
# Section: 562
# Assignment: 6.11 LAB: Pyramid area (part 1)
# Date: 27 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math

sLength = float(input("Enter the side length in meters: "))
layers = int(float(input("Enter the number of layers: ")))
area = 0
n = 1
while n <= layers:
    area += n * 3 * sLength**2
    n += 1
area += 3**0.5 / 4 * (sLength * layers) ** 2
print("You need " + str(format(area, "0.2f")) + " m^2 of gold foil to cover the pyramid")
