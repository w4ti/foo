#Problem Statement:
#Write an if-elif-else statement that does the following:
#Prints "This is a good number." if x is a single digit number.
#Print “This the best number” if x is a double digit number and divisible by 2.
#Prints "Horrible number" otherwise.

x = int(input('Please enter the Thunderdome by Choosing a Number Wisely: '))

if x <= 9 and x >= 0:
    print('This is a good number!')
elif x >= 10:
    print('This is a better number!')
elif (x > 10) / 2:
    print('This is the best number!')
else:
    print('This is a horrible number!')
