# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 6.15 LAB: Juggler sequence
# Date: 27 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math
count = 0
inputNum = int(input("Enter a positive integer: "))
print()
originalNum = inputNum
listNum = [inputNum,]
while inputNum > 1:
    if inputNum % 2 == 0:
        inputNum = math.floor(math.sqrt(inputNum))
        listNum.append(inputNum)
        count += 1
    else:
        inputNum = math.floor(inputNum ** (3 / 2))
        listNum.append(inputNum)
        count += 1
listToPrint = str(listNum).replace('[', '').replace(']', '')
print("The Juggler sequence starting at "+ str(originalNum) + " is:")
print(listToPrint)
print("It took "+ str(count) + " iterations to reach 1")
