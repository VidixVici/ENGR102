# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 4.18 LAB: How many gadgets
# Date: 13 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
dayIn = int(input("Please enter a positive value for day: "))
if (dayIn < 1):
    print("You entered an invalid number!")
day = dayIn
if (day >= 101):
    day = 100
answer = 0
if (dayIn > 10):
    answer = day * 10
    day -= 10
    if dayIn > 50:
        answer += 40 * (day - 50 + 11)
        day = 39
    answer += ((1/2)*day**2)+(1/2)*day
else:
    answer = dayIn * 10
if dayIn > 0:
    print("The sum total number of gadgets produced on day " + str(dayIn) + " is " + str(int(answer)))

