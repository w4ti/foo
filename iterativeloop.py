#Write a loop that adds the numbers 1 through 50.
#At some point the total value will be greater than 100.
#Have the loop print the number that makes the total
#greater than 100 and print the message "The sum exceeded the max value of 100."

x = 1
total = 0

while x <= 51:
  if total > 100:
    total = 100
    print('The sum exceeded the max value of 100!')
    break
  total += x
  x += 1

print(x)
