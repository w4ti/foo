#Problem Statement:
#Write an if-elif-else statement that does the following:
#If a number is odd, print “odd”
#If a number is even, print “even"
#If a number is odd and divisible by 3,  print “odd and divisible by 3”
#If a number is even and divisible by 3, print “even and divisible by 3”


x = int(input('Please enter the Thunderdome by Choosing a Number Wisely: '))
#if (x % 3) == 0 and (x % 2) != 0:
#    print('That number is odd and divisable by three!')

#elif (x % 3) == 0 and (x % 2) == 0:
#    print('That number is even and divisable by three!')

if (x % 2) == 0:
    if  (x % 3) == 0:
        print('That number is even and divisable by three!')
    else:
        print('That number is even, fool!')
elif (x % 2) != 0:
    if (x % 3) == 0:
        print('That number is odd and divisable, chump!')
    else:
        print('That number is odd, sucka!')

#elif (x % 2) != 0:
#    print('That number is odd, sucka!')
