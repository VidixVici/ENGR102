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
# Assignment: 4.13 LAB: Make change
# Date: 12 SEPTEMBER 2023
#
#
# YOUR CODE HERE
#
paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
print()
recievedChange = round(paid - cost,2)
diffPC = round(paid - cost,2)
diffPC = diffPC * 100
quarters = int(diffPC/25)
diffPC = diffPC - quarters * 25
if diffPC > 10:
    dimes = int(diffPC / 10)
    diffPC = diffPC - dimes*10
else: 
    dimes = 0
if diffPC > 5:
    nickels = int(diffPC / 5)
    diffPC = diffPC - nickels*5
else: 
    nickels = 0
pennies = int(diffPC)
if pennies >= 5:
    nickels += 1
    pennies -= 5
print("You received $" + str(format(recievedChange,'0.2f')) + " in change. That is...")
if (quarters > 0) and (quarters < 2):
    print(str(quarters) + " quarter")
if quarters >= 2:
    print(str(quarters) + " quarters")

if (dimes > 0) and (dimes < 2):
    print(str(dimes) + " dime")
if dimes >= 2:
    print(str(dimes) + " dimes")

if (nickels > 0) and (nickels < 2):
    print(str(nickels) + " nickel")
if nickels >= 2:
    print(str(nickels) + " nickels")

if (pennies > 0) and (pennies < 2):
    print(str(pennies) + " penny")
if pennies >= 2:
    print(str(pennies) + " pennies")