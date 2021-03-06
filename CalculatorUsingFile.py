################################################################
##   Simple Calculator App with File Usage (Jython)           ##
##   Author: Nick Belli                                       ##
##   Date: 04/25/2018                                         ##
##   Uncomment popup boxes for testing and training purposes  ##
##   Docs are delimited with "## ", commented code is "#"     ##
################################################################

## Import csv module to be able to open Excel (csv) files ##
import _csv

## Define program functions in small actionable parts ##
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

def returnMessage2(myResult):
    return 'My result is: ' + str(myResult)

## Welcome users to the application ##
popup("Welcome to the Calculator!")

##Read a row of data from the selected csv file into an array, and then pass the array to readable variables ##
with open("C:\Users\BELLN014\Desktop\Sikuli Scripts\CalculatorTest.csv") as csvfile:
    getRow = _csv.reader(csvfile)
    #getRow.next()
    currentRow = []
    for row in getRow:
        currentRow = row
        myNum1 = currentRow[0]
        myNum2 = currentRow[1]
        userSelection = currentRow[2]
    
    ## Popup boxes to unit test each of file inputs ##
                    
        popup('My first number is: ' + myNum1)
        popup('My second number is: ' + myNum2)
        popup('My selection is: ' + userSelection)
    
        if myNum1.isnumeric() and myNum2.isnumeric():
            if userSelection == "Add":
                myResult = addTwoNumbers(myNum1, myNum2)
                popup(returnMessage())
            elif userSelection == "Subtract":
                myResult = subtractTwoNumbers(myNum1, myNum2)
                popup(returnMessage())
            elif userSelection == "Multiply":
                popup(returnMessage2(multiplyTwoNumbers(myNum1, myNum2)))
            elif userSelection == "Divide":
                if int(myNum2) == 0:
                    popup("You can't divide by Zero!")
                else:
                    myResult = divideTwoNumbers(myNum1, myNum2)
                    popup(returnMessage())
        else: 
            popup("Please check the file")

    ## Thank the user to signify the end of the application run ##
    popup("Thank you for using the simple calculator")