################################################################
##   Simple Calculator App (Jython)                           ##
##   Author: Nick Belli                                       ##
##   Date: 04/18/2018                                         ##
##   Uncomment popup boxes for testing and training purposes  ##
##   Docs are delimited with "## ", commented code is "#"     ##
################################################################

def printMenu():
    userSelection = input("Please select an operation: \n" +
            "1: Add \n" +
            "2: Subtract \n" +
            "3: Multiply \n" +
            "4: Divide \n" + 
            "0: Exit " )
    return userSelection

def addTwoNumbers(myNum1, myNum2):
    return int(myNum1) + int(myNum2)

def subtractTwoNumbers(myNum1, myNum2):
    return int(myNum1) - int(myNum2)

def multiplyTwoNumbers(myNum1, myNum2):
    return int(myNum1) * int(myNum2)

def divideTwoNumbers(myNum1, myNum2):
    return int(myNum1) / int(myNum2)

def returnMessage():
    return 'My result is: ' + str(myResult)

## Welcome users to the application ##
popup("Welcome to the Calculator!")

## Begin the program by setting the sentinel value userSelection                ##
## userSelection has to be instantiated to something in order to begin the loop ##
userSelection = ''
while userSelection != "0":

## Prompt user for variables and instantiate the result to null ##
    myNum1 = input("Please enter your first number: ")
    myNum2 = input("Please enter your second number: ")
    myResult = ''

## Popup boxes to unit test acceptance of input ##
#popup('My first number is: ' + myNum1)
#popup('My second number is: ' + myNum2)

## Show the variables being stored as strings                              ##
## Strings concatenate expressions instead of using arithmetic expressions ##
#myResult = myNum1 + myNum2

## Show the conversion to integer for use of arithmetic expressions ##
#myResult = int(myNum1) + int(myNum2)

## Popup a menu and ask the user to select an operation ##
    userSelection = printMenu()
    
    ## Unit test to show that a userSelection exists ##
    #popup(userSelection)
    
    if userSelection == "1":
        myResult = addTwoNumbers(myNum1, myNum2)
        popup(returnMessage())
    elif userSelection == "2":
        myResult = subtractTwoNumbers(myNum1, myNum2)
        popup('My result is: ' + str(myResult))
    elif userSelection == "3":
        myResult =  multiplyTwoNumbers(myNum1, myNum2)
        popup('My result is: ' + str(myResult))
    elif userSelection == "4":
        if int(myNum2) == 0:
            popup("You can't divide by Zero!")
        else:
            myResult = divideTwoNumbers(myNum1, myNum2)
            popup('My result is: ' + str(myResult))
    elif userSelection == "0":
        popup("Thank you for using the simple calculator")
    else:
        ## Catch everything that is not a provided option and loop again ##
        popup("Please select a valid option")
