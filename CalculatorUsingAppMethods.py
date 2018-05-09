################################################################
##   Calculator Using Apps and Libraries (Jython)             ##
##   Author: Nick Belli                                       ##
##   Date: 05/04/2018                                         ##
##   Uncomment popup boxes for testing and training purposes  ##
##   Docs are delimited with "## ", commented code is "#"     ##
################################################################

## Import csv module to be able to open Excel (csv) files ##
import _csv
import os
import MathFunctions2

## Welcome users to the application ##
popup("Welcome to the Calculator!")

#Creating an instance of an app and opening it for use
calc = App("C:\WINDOWS\system32\calc.exe")
calc.open()
sleep(5)

##Read a row of data from the selected csv file into an array, and then pass the array to readable variables ##
with open("C:\Users\BELLN014\Desktop\Sikuli Scripts\CalculatorTest.csv") as csvfile:
    getRow = _csv.reader(csvfile)
    currentRow = []
    for row in getRow:
        currentRow = row
        myNum1 = currentRow[0]
        myNum2 = currentRow[1]
        userSelection = currentRow[2]
    
    ## Popup boxes to unit test each of file inputs ##
                    
        print('My first number is: ' + myNum1)
        print('My second number is: ' + myNum2)
        print('My selection is: ' + userSelection)
    
        if myNum1.isnumeric() and myNum2.isnumeric():
            if userSelection == "Add":
                MathFunctions2.addTwoNumbers(myNum1, myNum2)
            elif userSelection == "Subtract":
                MathFunctions2.subtractTwoNumbers(myNum1, myNum2)
            elif userSelection == "Multiply":
                MathFunctions2.multiplyTwoNumbers(myNum1, myNum2)
            elif userSelection == "Divide":
                if int(myNum2) == 0:
                    print("You can't divide by Zero!")
                else:
                    MathFunctions2.divideTwoNumbers(myNum1, myNum2)
        else: 
            print("Please check the file")

    ## Thank the user to signify the end of the application run ##
    popup("Thank you for using the simple calculator")
    #Make sure to close the app!
    calc.close()
