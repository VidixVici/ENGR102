# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 7.26 LAB: Leet speak
# Date: 4 OCTOBER 2023
#
#
# YOUR CODE HERE
#
leetdict = {'a': '4', 'e': '3', 'o': '0', 's': '5', 't': '7'}
leettext = ''
userinput = input("Enter some text: ")
print()
print('In leet speak, "' + str(userinput) + '" is:')
for char in userinput:
        leettext += leetdict.get(char.lower(), char)
print(leettext)
