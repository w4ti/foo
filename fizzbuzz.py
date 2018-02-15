# Create a loop that prints numbers 1-100. If a number divisible by three,
# replace the number with the word fizz. If a number divisible by five,
# replacethe number with the word buzz. Numbers divisible by
# both become fizz buzz.


x = list(range(101))
for x % 3 == 0 #and x % 5 == 0:
    print('fizzbuzz')
# elif x % 3 == 0:
#     print('fizz')
# elif x % 5 ==0:
#     print('buzz')
