# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 2.10 LAB: More Linear Interpolation
# Date: 30 AUGUST 2023
#
#
# YOUR CODE HERE
#
time1 = 12
time2 = 85
tInterpolate = 30
x1, y1, z1 = 8, 6, 7
x2, y2, z2 = -5, 30, 9
point1 = (x1,y1,z1)
point2 = (x2,y2,z2)

pInterpolate = (((x2 - x1)/(time2 - time1)) * (tInterpolate - time1) + x1,
                ((y2 - y1)/(time2 - time1)) * (tInterpolate - time1) + y1,
                ((z2 - z1)/(time2 - time1)) * (tInterpolate - time1) + z1)
print("At time 30.0 seconds:")
print("x1 = " + str(pInterpolate[0]) + " m")
print("y1 = " + str(pInterpolate[1]) + " m")
print("z1 = " + str(pInterpolate[2]) + " m")
print('-' * 23)

tInterpolate = 37.5
pInterpolate = (((x2 - x1)/(time2 - time1)) * (tInterpolate - time1) + x1,
                ((y2 - y1)/(time2 - time1)) * (tInterpolate - time1) + y1,
                ((z2 - z1)/(time2 - time1)) * (tInterpolate - time1) + z1)
print("At time 37.5 seconds:")
print("x2 = " + str(pInterpolate[0]) + " m")
print("y2 = " + str(pInterpolate[1]) + " m")
print("z2 = " + str(pInterpolate[2]) + " m")

print('-' * 23)

tInterpolate = 45
pInterpolate = (((x2 - x1)/(time2 - time1)) * (tInterpolate - time1) + x1,
                ((y2 - y1)/(time2 - time1)) * (tInterpolate - time1) + y1,
                ((z2 - z1)/(time2 - time1)) * (tInterpolate - time1) + z1)
print("At time 45.0 seconds:")
print("x3 = " + str(pInterpolate[0]) + " m")
print("y3 = " + str(pInterpolate[1]) + " m")
print("z3 = " + str(pInterpolate[2]) + " m")

print('-' * 23)

tInterpolate = 52.5
pInterpolate = (((x2 - x1)/(time2 - time1)) * (tInterpolate - time1) + x1,
                ((y2 - y1)/(time2 - time1)) * (tInterpolate - time1) + y1,
                ((z2 - z1)/(time2 - time1)) * (tInterpolate - time1) + z1)
print("At time 52.5 seconds:")
print("x4 = " + str(pInterpolate[0]) + " m")
print("y4 = " + str(pInterpolate[1]) + " m")
print("z4 = " + str(pInterpolate[2]) + " m")

print('-' * 23)

tInterpolate = 60
pInterpolate = (((x2 - x1)/(time2 - time1)) * (tInterpolate - time1) + x1,
                ((y2 - y1)/(time2 - time1)) * (tInterpolate - time1) + y1,
                ((z2 - z1)/(time2 - time1)) * (tInterpolate - time1) + z1)
print("At time 60.0 seconds:")
print("x5 = " + str(pInterpolate[0]) + " m")
print("y5 = " + str(pInterpolate[1]) + " m")
print("z5 = " + str(pInterpolate[2]) + " m")