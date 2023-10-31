# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 7.25 LAB: Pig latin
# Date: 4 OCTOBER 2023
#
#
# YOUR CODE HERE
#
vowels = "aeiouy"
inputString = input("Enter word(s) to convert to Pig Latin: ")
words = inputString.split()
answerList = []
print('In Pig Latin, "' + str(inputString) + '" is: ')
for word in words:
    if word[0].lower() in vowels:
        word = word + "yay"
    else:
        index = next((i for i, char in enumerate(word) if char.lower() in vowels), None)
        if index is not None:
            word =  word[index:] + word[:index] + "ay"
        else:
            word =  word + "ay"
    answerList.append(word)
print(*answerList)