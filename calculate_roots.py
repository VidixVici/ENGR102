# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 4.19 LAB: Calculate roots
# Date: 13 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math

a = int(input("Please enter the coefficient A: "))
print()
b = int(input("Please enter the coefficient B: "))
print()
c = int(input("Please enter the coefficient C: "))
print()

if a == 0 and b == 0:
    print("You entered an invalid combination of coefficients!")
elif a == 0:
    root = (-1 * c) / b
    print("The root is x = " + str(root))
else:
    if b**2 - 4 * a * c > 0:
        root1 = (-(b) + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        root2 = (-(b) - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        if root1 == root2:
            root1 = format(root1, "0.1f")
            print("The root is x = " + root1)
        else:
            root1 = format(root1, "0.1f")
            root2 = format(root2, "0.1f")
            print("The roots are x = " + root1 + " and x = " + root2)
    else:
        root = -b / (2 * a)
        root1 = abs(((b**2) - 4 * a * c) ** (1 / 2) / (2 * a))
        root2 = abs(((b**2) - 4 * a * c) ** (1 / 2) / (2 * a))
        if ((-(b**2 - 4**a * c)) ** (1 / 2) / (2 * a)) == 0:
            print("The root is x = " + str(root))
        elif root < 0:
            print(
                "The roots are x = "
                + str(format(root, "0.1f"))
                + " + "
                + str(format(root1, "0.1f"))
                + "i and x = "
                + str(format(root, "0.1f"))
                + " - "
                + str(format(root2, "0.1f"))
                + "i"
            )
        elif root1 == root2:
            print("The roots is x = " + str(format(root1, "0.1f")))
