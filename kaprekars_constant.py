# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 7.28 LAB: Kaprekar's constant
# Date: 4 OCTOBER 2023
#
#
# YOUR CODE HERE
#
number = int(input("Enter a four-digit integer: "))
print()
original = number
temp = number
one = []
four = []
sum1 = 0
sum4 = 0
it = 0
s = ""
t = True
one = temp // 1000
temp = number % 1000
two = temp // 100
temp = temp % 100
three = temp // 10
four = number % 10
if one == two and one == three and one == four:
    print(f'{original} > 0')
    it = 1
    print(f"\n{original} reaches 0 via Kaprekar's routine in {it} iterations")
    t = False
else:
    print(f'{original} >',end=" ")

while(number != 6174 and t):
    one=[]
    four=[]
    one.append(number//1000)
    number = number%1000
    one.append(number//100)
    number = number%100
    one.append(number//10)
    number = number%10
    one.append(number)
    one.sort()
    four = one[::-1]
    s=[str(i) for i in one]
    asc = (int)("".join(s))
    s=[str(i) for i in four]
    desc = (int)("".join(s))
    number = desc - asc
    if(number != 6174):
        print(f'{number} >',end=" ")
    else:
        print(f'{number}')
    it += 1
if not one == two and not one == three and not one == four:  
    print(f"\n{original} reaches 6174 via Kaprekar's routine in {it} iterations")
