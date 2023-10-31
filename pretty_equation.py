# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: 
# Noah Willows, 
# Caleb Anders, 
# Dan Le, 
# Zachary Harbert
# Section: 562
# Assignment: 4.14 LAB: Pretty equation
# Date: 12 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
import math
a_input = float(input('Please enter the coefficient A: '))
b_input = float(input('Please enter the coefficient B: '))
c_input = float(input('Please enter the coefficient C: '))
a_out = int(a_input)
b_out = int(b_input)
c_out = int(c_input)


if abs(a_input) >= 0:

    if abs(a_input) == 1.0:
        a_out = ""
    if abs(b_input) == 1.0:
        b_out = ""
    # All numbers Positive
    if (a_input >= 0) and (b_input >= 0) and (c_input >= 0):
        abcPos = "The quadratic equation is " + str(a_out) + "x^2 + " + str(b_out) + "x + " + str(c_out) + " = 0"

        if a_input == 0:
            abcPos = "The quadratic equation is " + str(b_out) + "x + " + str(c_out) + " = 0"
        if b_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2 + " + str(c_out) + " = 0"
        if c_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2 + " + str(b_out) + "x" + " = 0"
        if b_input == 0 and c_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2" + " = 0"
    # B and C Positive
    if (a_input <= 0) and (b_input >= 0) and (c_input >= 0):
        a_out = int(abs(a_input))
        b_out = int(abs(b_input))
        c_out = int(abs(c_input))
        if abs(a_input) == 1.0:
            a_out = ""
        if abs(b_input) == 1.0:
            b_out = ""
        abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 + " + str(b_out) + "x + " + str(c_out) + " = 0"

        if a_input == 0:
            abcPos = "The quadratic equation is " + str(b_out) + "x + " + str(c_out) + " = 0"
        if b_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 + " + str(c_out) + " = 0"
        if c_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 + " + str(b_out) + "x" + " = 0"
        if b_input == 0 and c_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2" + " = 0"
    # C Positive
    if (a_input <= 0) and (b_input <= 0) and (c_input >= 0):
        a_out = int(abs(a_input))
        b_out = int(abs(b_input))
        c_out = int(abs(c_input))
        if abs(a_input) == 1.0:
            a_out = ""
        if abs(b_input) == 1.0:
            b_out = ""
        abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 - " + str(b_out) + "x + " + str(c_out) + " = 0"

        if a_input == 0:
            abcPos = "The quadratic equation is " + "-" + str(b_out) + "x + " + str(c_out) + " = 0"
        if b_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 + " + str(c_out) + " = 0"
        if c_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 - " + str(b_out) + "x" + " = 0"
        if b_input == 0 and c_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2" + " = 0"
    # All Numbers negative
    if (a_input <= 0) and (b_input <= 0) and (c_input <= 0):
        a_out = int(abs(a_input))
        b_out = int(abs(b_input))
        c_out = int(abs(c_input))
        if abs(a_input) == 1.0:
            a_out = ""
        if abs(b_input) == 1.0:
            b_out = ""
        abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 - " + str(b_out) + "x - " + str(c_out) + " = 0"

        if a_input == 0:
            abcPos = "The quadratic equation is " + "-" + str(b_out) + "x - " + str(c_out) + " = 0"
        if b_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 - " + str(c_out) + " = 0"
        if c_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 - " + str(b_out) + "x" + " = 0"
        if b_input == 0 and c_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2" + " = 0"

    # B Positive
    if (a_input <= 0) and (b_input >= 0) and (c_input <= 0):
        a_out = int(abs(a_input))
        b_out = int(abs(b_input))
        c_out = int(abs(c_input))
        if abs(a_input) == 1.0:
            a_out = ""
        if abs(b_input) == 1.0:
            b_out = ""
        abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 + " + str(b_out) + "x - " + str(c_out) + " = 0"

        if a_input == 0:
            abcPos = "The quadratic equation is " + str(b_out) + "x - " + str(c_out) + " = 0"
        if b_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 - " + str(c_out) + " = 0"
        if c_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2 + " + str(b_out) + "x" + " = 0"
        if b_input == 0 and c_input == 0:
            abcPos = "The quadratic equation is " + "- " + str(a_out) + "x^2" + " = 0"

    # A and C Positive
    if (a_input >= 0) and (b_input <= 0) and (c_input >= 0):
        a_out = int(abs(a_input))
        b_out = int(abs(b_input))
        c_out = int(abs(c_input))
        if abs(a_input) == 1.0:
            a_out = ""
        if abs(b_input) == 1.0:
            b_out = ""
        abcPos = "The quadratic equation is " + str(a_out) + "x^2 - " + str(b_out) + "x + " + str(c_out) + " = 0"

        if a_input == 0:
            abcPos = "The quadratic equation is " + "-" + str(b_out) + "x + " + str(c_out) + " = 0"
        if b_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2 + " + str(c_out) + " = 0"
        if c_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2 - " + str(b_out) + "x" + " = 0"
        if b_input == 0 and c_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2" + " = 0"
    
    # A Positive
    if (a_input >= 0) and (b_input <= 0) and (c_input <= 0):
        a_out = int(abs(a_input))
        b_out = int(abs(b_input))
        c_out = int(abs(c_input))
        if abs(a_input) == 1.0:
            a_out = ""
        if abs(b_input) == 1.0:
            b_out = ""
        abcPos = "The quadratic equation is " + str(a_out) + "x^2 - " + str(b_out) + "x - " + str(c_out) + " = 0"

        if a_input == 0:
            abcPos = "The quadratic equation is " + "-" + str(b_out) + "x - " + str(c_out) + " = 0"
        if b_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2 - " + str(c_out) + " = 0"
        if c_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2 - " + str(b_out) + "x" + " = 0"
        if b_input == 0 and c_input == 0:
            abcPos = "The quadratic equation is " + str(a_out) + "x^2" + " = 0"
    print(abcPos)
