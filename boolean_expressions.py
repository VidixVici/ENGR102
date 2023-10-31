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
# Assignment: 4.15 LAB: Boolean expressions
# Date: 13 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#

############ Part A ############
a = input("Enter True or False for a: ")
if a == "True":
    a_out = True
elif a == "T":
    a_out = True
elif a == "t":
    a_out = True
elif a == "False":
    a_out = False
elif a == "F":
    a_out = False
elif a == "f":
    a_out = False

b = input("Enter True or False for b: ")
if b == "True":
    b_out = True
elif b == "T":
    b_out = True
elif b == "t":
    b_out = True
elif b == "False":
    b_out = False
elif b == "F":
    b_out = False
elif b == "f":
    b_out = False

c = input("Enter True or False for c: ")
if c == "True":
    c_out = True
elif c == "T":
    c_out = True
elif c == "t":
    c_out = True
elif c == "False":
    c_out = False
elif c == "F":
    c_out = False
elif c == "f":
    c_out = False

############ Part B ############
answer = a_out and b_out and c_out
print("a and b and c: " + str(answer))

answer = a_out or b_out or c_out
print("a or b or c: " + str(answer))

############ Part C ############
answer = (a_out and not b_out) or (not a_out and b_out)
print("XOR: " + str(answer))

answer = (a_out and not b_out and not c_out) or (a_out and b_out and c_out) or (not a_out and not b_out and c_out) or (not a_out and b_out and not c_out)
print("Odd number: " + str(answer))

############ Part D ############
answer = (not (a_out and not b_out) or (not c_out and b_out)) and (not b_out) or (not a_out and b_out and not c_out) or (a_out and not b_out)
print("Complex 1: " + str(answer))

answer = (not ((b_out or not c_out) and (not a_out or not c_out))) or (not (c_out or not (b_out and c_out))) or (a_out and not c_out) and (not a_out or (a_out and b_out
and c_out) or (a_out and ((b_out and not c_out) or (not b_out))))
print("Complex 2: " + str(answer))

answer = (not a_out and not c_out) or not b_out
print("Simple 1: " + str(answer))

answer = a_out or (not b_out and c_out)
print("Simple 2: " + str(answer))