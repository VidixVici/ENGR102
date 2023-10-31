# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 6.13 LAB: Howdy Whoop
# Date: 26 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))
print()
for i in range (1,101):
    if i % int1 == 0 and i % int2 == 0:
        print("Howdy")
        print("Whoop")
    elif i % int1 == 0:
        print("Howdy")
    elif i % int2 == 0:
        print("Whoop")
    else:
        print(i)