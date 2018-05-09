from sikuli import *

## Define program functions in small actionable parts ##
def addTwoNumbers(myNum1, myNum2):
    click(Pattern("1525442737897.png").targetOffset(107,70),10)
    print("I clicked it!")
    sleep(1)
    type(myNum1)
    sleep(1)
    type("+")
    sleep(1)
    type(myNum2)
    sleep(1)
    type(Key.ENTER) 
    myResult = int(myNum1) + int(myNum2)
    print(returnMessage2(myResult))

def subtractTwoNumbers(myNum1, myNum2):
    click(Pattern("1525435111239.png").targetOffset(118,70))
    print("I clicked it!")
    sleep(1)
    type(myNum1)
    sleep(1)
    type("-")
    sleep(1)
    type(myNum2)
    sleep(1)
    type(Key.ENTER) 
    myResult = int(myNum1) - int(myNum2)
    print(returnMessage2(myResult))

def multiplyTwoNumbers(myNum1, myNum2):
    click(Pattern("1525435111239.png").targetOffset(118,70))
    print("I clicked it!")
    sleep(1)
    type(myNum1)
    sleep(1)
    type("*")
    sleep(1)
    type(myNum2)
    sleep(1)
    type(Key.ENTER) 
    myResult = int(myNum1) * int(myNum2)
    print(returnMessage2(myResult))

def divideTwoNumbers(myNum1, myNum2):
    click(Pattern("1525435111239.png").targetOffset(118,70))
    print("I clicked it!")
    sleep(1)
    type(myNum1)
    sleep(1)
    type("/")
    sleep(1)
    type(myNum2)
    sleep(1)
    type(Key.ENTER) 
    myResult = int(myNum1) / int(myNum2)
    print(returnMessage2(myResult))

def returnMessage():
    return 'My result is: ' + str(myResult)

def returnMessage2(myResult):
    return 'My result is: ' + str(myResult)