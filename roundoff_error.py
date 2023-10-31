# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 4.17 LAB: Roundoff error
# Date: 7 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
############ Part A ############
a = 1 / 7
print(f'a = {a}')
b = a * 7
print(f'b = a * 7 = {b}')
# The answer should be 1, and it is!! Yay
c = 2 * a
d = 5 * a
f = c + d
print(f'f = 2 * a + 5 * a = {f}')
# The answer should be 1, and it is not, it is .99 repeating :/
from math import sqrt
x = sqrt(1 / 3)
print(f'x = {x}')
y = x * x * 3
print(f'y = x * x * 3 = {y}')
z = x * 3 * x
print(f'z = x * 3 * x = {z}')
# Why does not have roundoff error, but z does :/   
############ Part B ############
TOL = 1e-10
# check if b and f are equal within specified tolerance
if abs(b-f) < TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are not equal within the tolerance of {TOL}')
if abs(y-z) < TOL:
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print(f'y and z are not equal within the tolerance of {TOL}')
############ Part C ############
m = 0.1 
print(f'm = {m}')
n = 3 * m
print(f'n = 3 * m = 0.3 {n == 0.3}')
p = 7 * m
print(f'p = 7 * m = 0.7 {p == 0.7}')
q = n + p
print(f'q = n + p = 1 {q == 1}')
