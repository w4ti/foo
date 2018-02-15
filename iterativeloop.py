# Write a loop that adds the numbers 1 through 50.
# At some point the total value will be greater than 100.
# Have the loop print the number that makes the total
# greater than 100 and print the message "The sum exceeded the max value of 100."

x = 1
total = 0

while x <= 51:
  if total > 100:
    total = 100
    print('The sum exceeded the max value of 100!')
    break
  total += x
  x += 1

print('The interation by which the total of previous in the series completed the jump past the limit asked is ' ,x-1) # The reason this is - 1 is because the trigger was set once the count
           # went past 100 and explicitly added 1, which is then printed. The actual
           # solution is a result of line 15 being reduced by 1.
