import math
from sympy import diff, symbols
function = input("f(x)= ")
x = symbols('x')
f = eval(function)
interval = input("Interval:     NOTE!!!: seperate the intervals by space and not commas")

theRange = input("Range: ")



#number of iterations that the GSS would run for 
p = 0.61803


  # split input into a list of strings 
number = interval.split()
    #convert the string to integers 
a0, b0 = map(int, number)
    #test split intervaL

# finding the derivative of the equation 
def findDerivative():
    dfdx = diff(f,x) 
    print("differentation of f(x) = ", dfdx) 
#function that gets range 
def getRange():
    print("Range requested: " + theRange)

#function that gets the intervals 
def getInterval():
    print("Interval requested: ", interval)

#to calculate the number of iterations
def numOfIterations():
    try:
        theRange_value = float(theRange)
        if b0-a0 != 0:
            NoIterations = math.log( theRange_value/(b0-a0), p)
            NoIterations = round(NoIterations)
            print("your number of iterations would be ",NoIterations) 
        else: 
            print("thats not a valid one blud")
    except:
        print("enter a valid number as")

#creating a for loop for the number of iterations 
a1 = a0 + p*(b0-a0)
b1 = a0 + (1-p) *(b0 -a0)



#test out range
findDerivative()
getRange()
#test: interval
getInterval()
numOfIterations()
