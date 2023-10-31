# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 7.27 LAB: Split list
# Date: 4 OCTOBER 2023
#
#
# YOUR CODE HERE
#
import math
number = (input("Enter numbers: "))
x = number.split()
number = [int(i) for i in x]
L = []
R = []
LeftSum = 0
RightSum = 0
i=0
index = -1
while i < len(x):
    LeftSum = 0
    RightSum = 0
    for j in range(i):
        LeftSum += int(x[j])
    for j in range(i, len(x)):
        RightSum += int(x[j])
    if LeftSum == RightSum:
        index = i
        break
    i+=1
if index >= 0:
    print("Left: ",number[:index])
    print("Right: ",number[index:])
    print(f'Both sum to {RightSum}')
else:    
    print("Cannot split evenly")
    