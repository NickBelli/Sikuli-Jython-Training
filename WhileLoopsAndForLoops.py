## Counter Controlled Loop ##

counter = 0
while counter < 5:
    print counter
    counter += 1

## Sentinel Controlled Loop ##

sentinel = ''
while sentinel != "0":
    sentinel = input("Enter a number: ")
    popup("You entered " + sentinel)

## For Loop ##

for myNum in range(5):
   print "For " + str(myNum) 